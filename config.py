# ============================================================
# config.py  —  Centralized Configuration
# All credentials and settings for the YouTube Review Pipeline.
# ============================================================

# ── CLUSTER 1: Processing Cluster (tech_reviews) ─────────────────────────────
MONGO_URI_CLUSTER1  = "your mongodb uri here"
MONGO_DB_CLUSTER1   = "your mongodb database name here"

# ── CLUSTER 2: RAG / Production Cluster (youtube_rag) ────────────────────────
MONGO_URI_CLUSTER2  = "your mongodb uri here"
MONGO_DB_CLUSTER2   = "your mongodb database name here"

# ── CLUSTER 3: New Products Cluster ──────────────────────────────────────────
MONGO_URI_CLUSTER3  = "your mongodb uri here"
MONGO_DB_CLUSTER3   = "your mongodb database name here"

# ── Collection Names (shared across both clusters where applicable) ───────────
COLLECTION_VIDEOS       = "youtube_videos"
COLLECTION_COMMENTS     = "youtube_comments"
COLLECTION_TRANSLATED   = "youtube_translated_comments_main"
COLLECTION_TOPIC        = "youtube_topic_model"
COLLECTION_SENTIMENT    = "youtube_Sentiment_Analysis"
COLLECTION_FINAL        = "youtube_final_data"

# ── YouTube Data API Keys (rotated to avoid quota limits)*(I used 8 keys) ────────────────────
YOUTUBE_API_KEYS = [
    "api 1 key here",
    "api 2 key here",
    "api 3 key here",
    "api 4 key here",
    "api 5 key here",
    "api 6 key here",
    "api 7 key here",
    "api 8 key here",
]



# ── HuggingFace Model Names ───────────────────────────────────────────────────
SENTIMENT_MODEL     = "cardiffnlp/twitter-roberta-base-sentiment"
SUMMARIZATION_MODEL = "google/flan-t5-base"
SPACY_MODEL         = "en_core_web_sm"

# ── Product Catalogue ─────────────────────────────────────────────────────────
# Used in Section 11 for product name normalisation (exact + fuzzy matching).
PRODUCT_NAMES = [
    # ── Apple — iPhone ────────────────────────────────────────────────────────
    "iphone 17 pro max", "iphone 17 pro", "iphone 17", "iphone air",
    "iphone 17e", "iphone 16 pro max", "iphone 16 pro",
    "iphone 16", "iphone 16 plus", "iphone 16e",
    "iphone 15 pro max", "iphone 15 plus", "iphone 14 pro",
    # ── Apple — MacBook & Mac ──────────────────────────────────────────────────
    "macbook air m4", "macbook air m3",
    "macbook pro m5", "macbook pro m4", "macbook pro m3",
    "macbook neo", "mac mini m4", "mac studio m4 max", "imac m4",
    # ── Apple — iPad ──────────────────────────────────────────────────────────
    "ipad pro m5", "ipad air m4", "ipad air m3",
    "ipad mini a17 pro", "ipad 11th generation",
    # ── Apple — Watch ─────────────────────────────────────────────────────────
    "apple watch series 11", "apple watch ultra 3",
    "apple watch se 3", "apple watch series 10",
    "apple watch ultra 2", "apple watch series 9",
    # ── Apple — Audio & Accessories ───────────────────────────────────────────
    "airpods pro 3", "airpods pro 2", "airpods 4",
    "airpods max 2", "airpods max",
    "apple vision pro", "apple pencil pro", "airtag 2",
    # ── Samsung — Galaxy S ────────────────────────────────────────────────────
    "samsung galaxy s26 ultra", "samsung galaxy s26+", "samsung galaxy s26",
    "samsung galaxy s25 ultra", "samsung galaxy s25+", "samsung galaxy s25",
    "samsung galaxy s25 edge",
    "samsung galaxy s24 ultra", "samsung galaxy s24",
    # ── Samsung — Foldables ───────────────────────────────────────────────────
    "samsung galaxy z fold 7", "samsung galaxy z flip 7",
    "samsung galaxy z fold 6 special edition",
    "samsung galaxy z fold 6", "samsung galaxy z flip 6",
    "samsung galaxy z trifold",
    # ── Samsung — A Series ────────────────────────────────────────────────────
    "samsung galaxy a56", "samsung galaxy a55",
    "samsung galaxy a36", "samsung galaxy a35", "samsung galaxy a26",
    # ── Samsung — Tablets ─────────────────────────────────────────────────────
    "samsung galaxy tab s10 ultra", "samsung galaxy tab s10 plus",
    "samsung galaxy tab s10 fe",
    # ── Samsung — Watch & Ring ────────────────────────────────────────────────
    "samsung galaxy watch 8 ultra", "samsung galaxy watch 8",
    "samsung galaxy watch ultra", "samsung galaxy watch 7",
    "samsung galaxy ring 2", "samsung galaxy ring",
    # ── Samsung — Buds & Laptops ──────────────────────────────────────────────
    "samsung galaxy buds 4 pro", "samsung galaxy buds 3 pro", "samsung galaxy buds 3",
    "samsung galaxy book6 ultra", "samsung galaxy book6 pro", "samsung galaxy book6",
    # ── Google — Pixel Phones ────────────────────────────────────────────────
    "google pixel 10 pro xl", "google pixel 10 pro fold",
    "google pixel 10 pro", "google pixel 10",
    "google pixel 9 pro xl", "google pixel 9 pro fold",
    "google pixel 9 pro", "google pixel 9",
    "google pixel 10a", "google pixel 9a", "google pixel 8a", 
    "google pixel 8",
    # ── Google — Pixel Watch ─────────────────────────────────────────────────
    "google pixel watch 4", "google pixel watch 3",
    # ── Google — Pixel Buds & Tablet ─────────────────────────────────────────
    "google pixel buds pro 2", "google pixel buds 2a", "google pixel buds pro",
    "google pixel tablet 2", "google pixel tablet",
    # ── OnePlus ───────────────────────────────────────────────────────────────
    "oneplus 15r", "oneplus 15", "oneplus 13r", "oneplus 13",
    "oneplus open 2", "oneplus nord ce 4", "oneplus nord 4",
    "oneplus ace 5 pro", "oneplus watch 3",
    # ── Xiaomi ────────────────────────────────────────────────────────────────
    "xiaomi 17 ultra", "xiaomi 17 pro", "xiaomi 17",
    "xiaomi 15 ultra", "xiaomi 15 pro", "xiaomi 15",
    "xiaomi mix flip 2", "xiaomi mix fold 4",
    "xiaomi redmi note 14 pro plus", "xiaomi redmi note 13 pro plus",
    "xiaomi pad 7 pro", "xiaomi pad 7",
    # ── Oppo ──────────────────────────────────────────────────────────────────
    "oppo find x9 ultra", "oppo find x9 pro",
    "oppo find x8 ultra", "oppo find x8 pro",
    "oppo find n5", "oppo reno 14 pro",
    # ── Realme ────────────────────────────────────────────────────────────────
    "realme gt 8 pro", "realme gt 7 pro", "realme gt 6",
    "realme 15 pro", "realme 14 pro plus",
    # ── Others ────────────────────────────────────────────────────────────────
    "sony wh-1000xm6", "sony ps5 pro",
    "nintendo switch 2", "steam deck oled",
]

# ── Bad / Junk Topic Labels ────────────────────────────────────────────────────
# Topics to drop from the final dataset (low-signal / language-detection noise).
BAD_TOPIC_LABELS = [
    "the, is, to",
    "the, to, is",
    "the, iphone, is",
    "hai, anna, bhai",
    "file, save, changes",
    "background, lamp, light",
    "mustache, moustache, hair",
    "love, side, him",
    "side, right, left",
    "whiteboard, event, whether",
    "temporary, folder, licence",
    "sorry, don, re",
    "re, don, talking",
    "apl77x, amazons, opportunity",
    "xai308k, crypto, xai315k",
    "dot44h, btc, eth",
    "woods, hug, tree",
]