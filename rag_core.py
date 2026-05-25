"""
rag_core.py  —  Shared RAG logic for Tech YouTube RAG
======================================================
Import this module in app.py (and optionally in RAG.ipynb) to avoid
duplicating the core pipeline functions.

Usage:
    from rag_core import (
        calculate_score,
        fetch_top_comments,
        generate_summary,
        query_product_topic_summary,
        query_product_overall_summary,
    )
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import torch
import numpy as np
import pandas as pd
from pymongo import MongoClient
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer as SentTokenizer,
)
from groq import Groq

from config_rag import (
    MONGO_URI, MONGO_DB_NAME,
    COLLECTION_FINAL,
    GROQ_API_KEY,          # ← Add GROQ_API_KEY to your config_rag.py
)
from config import (
    SENTIMENT_MODEL,       # SUMMARIZATION_MODEL no longer needed
)

# ── MongoDB ───────────────────────────────────────────────────────────────────
_client           = MongoClient(MONGO_URI)
_db               = _client[MONGO_DB_NAME]
final_collection  = _db[COLLECTION_FINAL]

# ── Models (loaded once at import time) ───────────────────────────────────────
print(f"[rag_core] Loading sentiment model: {SENTIMENT_MODEL} …")
sent_tokenizer   = SentTokenizer.from_pretrained(SENTIMENT_MODEL)
sent_model       = AutoModelForSequenceClassification.from_pretrained(SENTIMENT_MODEL)
SENTIMENT_LABELS = ["Negative", "Neutral", "Positive"]

print("[rag_core] Initialising Groq client (Llama 3) …")
groq_client = Groq(api_key=GROQ_API_KEY)

print("[rag_core] All models ready.")


# ── Core functions ────────────────────────────────────────────────────────────

def calculate_score(row: dict, query_topic: str) -> float:
    """Compute a relevance score for a single comment row."""
    score = 0.0

    # Sentiment weight
    if row["sentiment"] in ("Positive", "Negative"):
        score += 3.0
    else:
        score += 0.8  # Neutral

    # Topic match bonus
    if query_topic.lower() in str(row["topic_label"]).lower():
        score += 2.0

    # Direct mention in comment text
    if query_topic.lower() in str(row["translated_comment"]).lower():
        score += 0.7

    # Length bonus (capped at 2)
    score += min(len(str(row["translated_comment"]).split()) // 10, 2)

    return score


def fetch_top_comments(df: pd.DataFrame, product_name: str,
                       query_topic: str, max_comments: int = 15) -> pd.DataFrame:
    """Filter comments by product and topic, score them, return top-N rows."""
    product_df = df[df["product_name"].str.contains(product_name, case=False, na=False)].copy()

    if product_df.empty:
        return pd.DataFrame()

    # Strict text match first
    topic_df = product_df[
        product_df["translated_comment"].str.contains(query_topic, case=False, na=False)
    ].copy()

    # Fall back to topic_label if too few hits
    if len(topic_df) < 5:
        topic_df = product_df[
            product_df["topic_label"].str.contains(query_topic, case=False, na=False)
        ].copy()

    if len(topic_df) < 3:
        return pd.DataFrame()

    topic_df["score"] = topic_df.apply(
        lambda r: calculate_score(r, query_topic), axis=1
    )
    return topic_df.sort_values("score", ascending=False).head(max_comments)[
        ["translated_comment", "topic_label", "sentiment", "score"]
    ]


def generate_summary(comment_list: list, product_name: str,
                     query_topic: str, format_type: str = "bullet") -> str:
    """Summarise a list of comments using Groq (Llama 3)."""
    if not comment_list:
        return f"No relevant comments to summarise for {product_name} – {query_topic}."

    combined = "\n".join([f"- {c}" for c in comment_list])

    if format_type == "bullet":
        instruction = (
            f"Analyze these YouTube comments about {product_name} regarding '{query_topic}'.\n"
            f"Summarize in bullet points. Format strictly as:\n\n"
            f"Pros:\n- point\n- point\n\n"
            f"Cons:\n- point\n- point\n\n"
            f"Be specific and concise. Do not repeat points.\n\n"
            f"Comments:\n{combined}"
        )
    else:
        instruction = (
            f"Analyze these YouTube comments about {product_name} regarding '{query_topic}'.\n"
            f"Write 2-3 clear paragraphs covering: what users love, what they dislike, overall verdict.\n"
            f"Be specific and concise. Do not repeat points.\n\n"
            f"Comments:\n{combined}"
        )

    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": instruction}],
        max_tokens=1024,
        temperature=0.3,
    )
    summary = response.choices[0].message.content
    return f"Summary for {product_name} — {query_topic}:\n{summary}"


def query_product_topic_summary(product_name: str, query_topic: str,
                                format_type: str = "bullet") -> str:
    """End-to-end RAG: load data → retrieve top comments → generate summary."""
    df = pd.DataFrame(list(final_collection.find({}, {"_id": 0})))

    if df.empty:
        return "No data found in the database. Please run the RAG pipeline first."

    top_df = fetch_top_comments(df, product_name, query_topic)

    if top_df.empty:
        return (
            f"Not enough data for '{product_name}' – '{query_topic}'. "
            "Try a broader product name or topic."
        )

    comment_list = top_df["translated_comment"].tolist()
    return generate_summary(comment_list, product_name, query_topic, format_type)


def query_product_overall_summary(product_name: str, format_type: str = "bullet") -> str:
    """End-to-end RAG: load data → retrieve all comments → generate overall summary."""
    df = pd.DataFrame(list(final_collection.find({}, {"_id": 0})))

    if df.empty:
        return "No data found in the database."

    product_df = df[df["product_name"].str.contains(product_name, case=False, na=False)].copy()

    if product_df.empty:
        return f"No comments found for '{product_name}'."

    # ── SENTIMENT BREAKDOWN ───────────────────────────────────────────────────
    total    = len(product_df)
    positive = (product_df["sentiment"] == "Positive").sum()
    negative = (product_df["sentiment"] == "Negative").sum()
    neutral  = (product_df["sentiment"] == "Neutral").sum()

    # ── TOP COMMENTS — filter short/low quality ───────────────────────────────
    def is_good(text):
        words = str(text).split()
        return 8 <= len(words) <= 60

    good_df      = product_df[product_df["translated_comment"].apply(is_good)]
    top_positive = good_df[good_df["sentiment"] == "Positive"]["translated_comment"].head(15).tolist()
    top_negative = good_df[good_df["sentiment"] == "Negative"]["translated_comment"].head(15).tolist()
    top_neutral  = good_df[good_df["sentiment"] == "Neutral"]["translated_comment"].head(10).tolist()
    all_comments = top_positive + top_negative + top_neutral

    # ── TOP TOPICS — exclude Uncategorized ───────────────────────────────────
    top_topics = (
        product_df[product_df["topic_label"] != "Uncategorized"]["topic_label"]
        .value_counts().head(5).index.tolist()
    )

    # ── BUILD PROMPT & CALL GROQ ──────────────────────────────────────────────
    combined = "\n".join([f"- {c}" for c in all_comments])

    if format_type == "bullet":
        instruction = (
            f"Analyze these YouTube comments about {product_name}.\n"
            f"Summarize the OVERALL user experience. Format strictly as:\n\n"
            f"Pros:\n- point\n- point\n\n"
            f"Cons:\n- point\n- point\n\n"
            f"Overall Verdict:\n- one line summary\n\n"
            f"Focus on battery, camera, performance, price, design.\n"
            f"Be specific. Do not repeat points.\n\n"
            f"Comments:\n{combined}"
        )
    else:
        instruction = (
            f"Analyze these YouTube comments about {product_name}.\n"
            f"Write a 3 paragraph summary of overall user experience.\n"
            f"Paragraph 1: What users love\n"
            f"Paragraph 2: What users dislike\n"
            f"Paragraph 3: Overall verdict\n"
            f"Be specific and concise. Do not repeat points.\n\n"
            f"Comments:\n{combined}"
        )

    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": instruction}],
        max_tokens=1024,
        temperature=0.3,
    )
    summary = response.choices[0].message.content

    # ── FORMAT FINAL RESPONSE ─────────────────────────────────────────────────
    result = (
        f"📊 Overall User Experience — {product_name}\n"
        f"{'='*50}\n"
        f"Total Comments  : {total}\n"
        f"😊 Positive     : {positive} ({positive/total*100:.1f}%)\n"
        f"😐 Neutral      : {neutral}  ({neutral/total*100:.1f}%)\n"
        f"😠 Negative     : {negative} ({negative/total*100:.1f}%)\n"
        f"\n🔥 Top Topics   : {', '.join(top_topics)}\n"
        f"{'='*50}\n\n"
        f"{summary}"
    )

    return result