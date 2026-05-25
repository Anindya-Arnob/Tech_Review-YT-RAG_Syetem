<div align="center">

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=200&section=header&text=Tech%20YouTube%20RAG&fontSize=60&fontColor=ffffff&fontAlignY=35&desc=AI-Powered%20Sentiment%20Intelligence%20from%20YouTube%20Reviews&descAlignY=58&descSize=18&animation=fadeIn" width="100%"/>

<br/>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=1a1a2e"/></a>
  <a href="#"><img src="https://img.shields.io/badge/Flask-3.x-000000?style=for-the-badge&logo=flask&logoColor=white&labelColor=1a1a2e"/></a>
  <a href="#"><img src="https://img.shields.io/badge/MongoDB_Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white&labelColor=1a1a2e"/></a>
  <a href="#"><img src="https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black&labelColor=1a1a2e"/></a>
  <a href="#"><img src="https://img.shields.io/badge/Groq_LLaMA_3-F55036?style=for-the-badge&logo=meta&logoColor=white&labelColor=1a1a2e"/></a>
  <a href="#"><img src="https://img.shields.io/badge/BERTopic-8A2BE2?style=for-the-badge&logo=pytorch&logoColor=white&labelColor=1a1a2e"/></a>
  <a href="#"><img src="https://img.shields.io/badge/Azure_Translator-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white&labelColor=1a1a2e"/></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/88%2C498+-Records%20in%20DB-success?style=flat-square"/>
  <img src="https://img.shields.io/badge/100+-Products%20Tracked-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/50+-Languages%20Supported-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square"/>
</p>

<br/>

> ### *"What do 88,000 real users actually think about their tech products?"*
> ### *This pipeline answers that — at scale, in real time, with AI.*

<br/>

</div>

---

## 📖 Table of Contents

- [🌟 What Is This Project?](#-what-is-this-project)
- [🖥️ Screenshots](#️-screenshots)
- [🏗️ Architecture Overview](#️-architecture-overview)
- [📁 Project Structure](#-project-structure)
- [⚙️ Data Cleaning & Processing Pipeline — Deep Dive](#️-data-cleaning--processing-pipeline--deep-dive)
- [🤖 RAG Engine — Deep Dive](#-rag-engine--deep-dive)
- [🚀 Quick Start](#-quick-start)
- [🌐 API Reference](#-api-reference)
- [🧠 Models & Technologies](#-models--technologies)
- [🛍️ Supported Products](#️-supported-products)
- [📜 License](#-license)

---

<br/>

## 🌟 What Is This Project?

**Tech YouTube RAG** is a production-grade end-to-end pipeline that collects YouTube tech review comments, processes them through a full NLP stack, and serves AI-generated summaries through a beautiful web interface.

Instead of reading hundreds of comment sections yourself, this system fetches, translates, clusters, classifies, and summarises everything — then lets you query any product + topic in seconds.

---

<br/>

## 🖥️ Screenshots

<table>
  <tr>
    <td align="center" width="50%">
      <img src="assets/Screenshot_2026-05-26_002415.png" width="100%"/>
      <br/><b>Topic Search — iPhone 17 Pro · Camera</b>
      <br/><sub>Live query interface with product autocomplete and 88,498 records connected</sub>
    </td>
    <td align="center" width="50%">
      <img src="assets/Screenshot_2026-05-26_002438.png" width="100%"/>
      <br/><b>AI-Generated Pros & Cons Summary</b>
      <br/><sub>LLaMA 3 structured summary grounded in real user comments</sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="50%">
      <img src="assets/Screenshot_2026-05-26_002648.png" width="100%"/>
      <br/><b>Overall Experience — Samsung Galaxy S26</b>
      <br/><sub>1,171 comments · sentiment breakdown · top topics · paragraph narrative</sub>
    </td>
    <td align="center" width="50%">
      <img src="assets/Screenshot_2026-05-26_002752.png" width="100%"/>
      <br/><b>Topic Search — iMac M4 · Price</b>
      <br/><sub>Nuanced pros/cons extracted from real reviewer opinions</sub>
    </td>
  </tr>
</table>

---

<br/>

## 🏗️ Architecture Overview

```
YouTube API  →  Raw Comments  →  [Data Cleaning & Processing Pipeline]
                                          │
                        ┌─────────────────┼──────────────────────┐
                        │                 │                       │
                   Section 3          Section 4              Section 5
                 Text Cleaning     Translation &           Tokenisation
                 Spam Removal     Lang Detection            (spaCy NLP)
                        │                 │                       │
                        └─────────────────┼───────────────────────┘
                                          │
                               ┌──────────┴──────────┐
                               │                     │
                          Section 6              Section 7
                       Topic Modelling         Sentiment Analysis
                         (BERTopic)             (RoBERTa GPU)
                               │                     │
                               └──────────┬──────────┘
                                          │
                                     Section 8
                                  Product Mapping
                                 (Exact + Fuzzy)
                                          │
                                     Section 9
                                  Final Assembly
                                 youtube_final_data
                                          │
                                    MongoDB Atlas
                                     Cluster 2
                                          │
                              ┌───────────┴───────────┐
                              │                       │
                          rag_core.py              app.py
                       (Retrieval + Groq)       (Flask API)
                              │                       │
                              └───────────┬───────────┘
                                          │
                                  tech_yt_rag.html
                                    (Browser UI)
```

---

<br/>

## 📁 Project Structure

```
tech-youtube-rag/
│
├── 📓 YouTube_comments_fetching.ipynb        ← Stage 1: Fetch videos & comments
├── 📓 Data_Cleaning_and_Processing.ipynb     ← Stage 2: Full NLP processing (10 sections)
│
├── 🐍 app.py                                 ← Flask REST API server
├── 🐍 rag_core.py                            ← Core RAG logic
├── 🐍 config.py                              ← Master config (clusters, keys, product list)
├── 🐍 config_rag.py                          ← RAG service config (production cluster)
│
└── 🌐 tech_yt_rag.html                       ← Single-file frontend UI
```

---

<br/>

## ⚙️ Data Cleaning & Processing Pipeline — Deep Dive

> **File:** `Data_Cleaning_and_Processing.ipynb`

This is the heart of the entire system. Raw, multilingual, noisy YouTube comments go in — a clean, structured, sentiment-labelled, topic-tagged, product-mapped dataset comes out. There are **10 sections**, each with a specific responsibility. Here is every single one explained in full detail.

---

### Section 0 — Dependency Installation

Run **once** to bootstrap the entire environment. It programmatically installs every required package using `subprocess` and downloads the spaCy English model.

**Packages installed:**
`pymongo` · `transformers` · `sentencepiece` · `argostranslate` · `emoji` · `langdetect` · `spacy` · `bertopic` · `matplotlib` · `plotly` · `sentence-transformers` · `umap-learn` · `hdbscan` · `scikit-learn` · `torch` · `tqdm` · `rapidfuzz`

```python
import subprocess, sys
packages = ['pymongo','transformers','sentencepiece','argostranslate','emoji',
            'langdetect','spacy','bertopic','matplotlib','plotly',
            'sentence-transformers','umap-learn','hdbscan','scikit-learn',
            'torch','transformers','tqdm','rapidfuzz']
subprocess.run([sys.executable, '-m', 'pip', 'install', *packages])
subprocess.run([sys.executable, '-m', 'spacy', 'download', 'en_core_web_sm'])
```

---

### Section 1 — Imports & Config

Imports the full library stack and loads all credentials and settings from `config.py`. Nothing is hardcoded in the notebook itself — every URI, key, model name, product list, and collection name comes from the central config file.

**Libraries imported across 10 categories:**

| Category | Libraries |
|----------|-----------|
| Standard library | `sys`, `os`, `re`, `time` |
| Data | `pandas`, `numpy`, `collections.Counter` |
| Database | `pymongo.MongoClient` |
| Text cleaning | `emoji`, `re` |
| Language detection | `langdetect.detect` |
| NLP | `spacy` |
| Translation | `transformers.pipeline`, `argostranslate` |
| Topic modelling | `BERTopic`, `KeyBERTInspired`, `UMAP`, `HDBSCAN`, `SentenceTransformer`, `cosine_similarity` |
| Sentiment | `torch`, `AutoModelForSequenceClassification`, `AutoTokenizer` |
| Product mapping | `rapidfuzz.process`, `rapidfuzz.fuzz` |

---

### Section 2 — MongoDB Connection

Establishes connections to the MongoDB cluster(s) with sensible timeout settings and creates handles for all 6 collections used throughout the pipeline.

```python
def get_client(uri: str, timeout_ms: int = 60_000) -> MongoClient:
    return MongoClient(
        uri,
        serverSelectionTimeoutMS=timeout_ms,
        connectTimeoutMS=timeout_ms,
        socketTimeoutMS=None,   # ← No timeout on long read/write operations
    )
```

**Collection handles created:**

| Handle | Collection | Purpose |
|--------|-----------|---------|
| `videos_col` | `youtube_videos` | Source video metadata |
| `comments_col` | `youtube_comments` | Raw comments from YouTube API |
| `translated_col` | `youtube_translated_comments_main` | Post-translation checkpoint |
| `topic_col` | `youtube_topic_model` | Post-BERTopic checkpoint |
| `sentiment_col` | `youtube_Sentiment_Analysis` | Post-sentiment checkpoint |
| `final_col` | `youtube_final_data` | Production-ready final dataset |

---

### Section 3 — Data Cleaning

Loads raw comments from MongoDB and applies a multi-stage cleaning pipeline to remove noise, spam, and unusable entries before any NLP work begins.

**Cleaning steps in order:**

**Step 1 — URL-only spam detection**
Any comment with fewer than 4 real words remaining after URL removal is flagged as spam and dropped. This catches comments that are purely promotional links.

```python
URL_PATTERN = re.compile(
    r'(https?://\S+|www\.\S+|\b\w+\.(com|net|org|io|co|ly|me|tv|gg)\S*)',
    re.IGNORECASE,
)
def is_url_only_spam(text: str) -> bool:
    return len(URL_PATTERN.sub('', str(text)).strip().split()) < 4
```

**Step 2 — Text normalisation via `clean_text()`**
Applied to every comment. Performs in this exact order:
1. Remove all URLs matching the URL pattern
2. Convert emojis to `:code:` format using the `emoji` library
3. Strip all `:code:` emoji tokens
4. Drop all non-ASCII characters (handles Chinese, Arabic, Cyrillic before translation)
5. Strip all punctuation characters
6. Lowercase everything

**Step 3 — Spam keyword filtering**
Drops comments that contain any of **36 predefined spam phrases** covering two categories:

- **Self-promotion:** `"subscribe"`, `"check my channel"`, `"click the link"`, `"visit my channel"`, `"sub4sub"`, `"follow me"`, `"link in bio"`, `"new video"`, `"watch my"`, etc.
- **Generic empty praise:** `"great video"`, `"amazing content"`, `"nice video"`, `"great review"`, `"keep it up"`, `"keep up the good work"`, `"outstanding video"`, `"brilliant video"`, etc.

These comments carry zero signal for product sentiment analysis and would pollute topic modelling results.

**Step 4 — Empty row removal**
Any comment that becomes empty or whitespace-only after cleaning is dropped.

---

### Section 4 — Language Detection & Translation

The most compute-intensive section. Handles the full multilingual translation pipeline: detect → validate → translate → verify → save.

#### 4.1 — Load Helsinki-NLP MarianMT Model

Loads `Helsinki-NLP/opus-mt-mul-en` — a multilingual-to-English sequence-to-sequence translation model. Automatically places it on GPU if available, otherwise CPU.

```python
model_name = "Helsinki-NLP/opus-mt-mul-en"
tokenizer  = MarianTokenizer.from_pretrained(model_name)
model      = MarianMTModel.from_pretrained(model_name)
device     = "cuda" if torch.cuda.is_available() else "cpu"
model      = model.to(device).eval()
```

#### 4.2 — Helper Functions

Three functions are defined here that orchestrate the full translation logic:

**`safe_detect(text)`** — Wraps `langdetect.detect()` in a try/except. Returns `"unknown"` on failure rather than crashing. Essential because `langdetect` can raise exceptions on very short or symbol-only strings.

**`helsinki_translate(texts)`** — Takes a list of strings, tokenises them with padding and truncation to 512 tokens, runs them through the MarianMT model with `torch.no_grad()`, and decodes the output tokens back to strings. All operations happen on the target device (GPU/CPU).

**`translate_batch(texts, langs, batch_size=32)`** — The orchestrator function. Runs Helsinki translation in batches of 32. If any batch fails (OOM, model error, etc.), those indices are recorded. After the main Helsinki pass, any failed translations are retried using **Argos Translate** as a fallback — it dynamically downloads and installs the appropriate language packages on demand. If Argos also fails, the original untranslated text is kept as a last resort.

```
Translation flow for each comment:
  1. Helsinki-NLP (batch_size=32, GPU)     → ~95% success rate
  2. Argos Translate fallback              → handles Helsinki failures
  3. Keep original text                   → absolute last resort
```

#### 4.3 — Detect Languages & Drop Unknown Rows

Runs `safe_detect()` on every comment in the DataFrame. Prints the full language distribution (e.g. `{'en': 45000, 'hi': 8000, 'es': 3000, ...}`). Drops all rows where language detection returned `"unknown"` — these are typically emoji-only or symbol-only comments with no translatable content.

#### 4.4 — Split English vs Non-English & Re-detect

Separates the DataFrame into English and non-English subsets. Then runs a **second language detection pass** on the non-English subset only. This catches mis-detections — for example, `langdetect` sometimes classifies short English phrases like "great phone" as Dutch or Afrikaans. The re-detection pass corrects these before sending anything unnecessary through the expensive translation step.

```
After re-detection:
  - "actually_english" comments → moved back to English subset, no translation needed
  - "truly_foreign" comments   → proceed to translation
```

#### 4.5 — Translate Non-English Comments

Calls `translate_batch()` on the `truly_foreign` subset only. The `translated_comment` column is populated with English translations. The original `comment` column is preserved.

#### 4.6 — Merge All Parts & Remove Duplicates

Concatenates three subsets back into one DataFrame using `pd.concat`:
- `english_df` — originally detected as English
- `actually_english` — rescued from mis-detection
- `truly_foreign` — now translated to English

Then runs `drop_duplicates(subset=['video_id', 'comment'])` to remove any exact duplicate comments that may have appeared across multiple API calls for the same video.

#### 4.7 — Final Language Validation

Runs a **third and final language detection pass** on the `translated_comment` column (not the original). Any comment that is still not in English after translation is dropped. This catches edge cases where the translation model produced garbled output or non-English text.

```python
# Keeps a row only if EITHER:
# - original language was detected as English, OR
# - the translated_comment is now detected as English
df = df[
    (df['language'] == 'en') | (df['_detected_trans'] == 'en')
]
```

#### 4.8 — Save Translated Data (Checkpoint)

Saves the fully translated and validated DataFrame to `youtube_translated_comments_main` in batches of 5,000. This acts as a **checkpoint** — if the pipeline crashes during the expensive BERTopic or sentiment stages, you don't need to re-run the translation. The collection is wiped before saving (`delete_many({})`) to ensure a clean state on re-runs.

---

### Section 5 — Tokenisation & Stopword Removal

Loads the translated data and uses **spaCy `en_core_web_sm`** to tokenise, lemmatise, and clean each comment for downstream analysis.

**What `spacy_tokenize()` does to each comment:**
1. Passes the text through the spaCy `nlp` pipeline
2. For each token, checks 4 conditions — must NOT be a stopword, must NOT be punctuation, must NOT be whitespace, must be longer than 1 character
3. Returns the **lemma** (base form) of qualifying tokens — so "cameras", "camming", "camera" all become "camera"

**Output columns added:**
- `cleaned_tokens` — list of lemmatised tokens e.g. `["camera", "quality", "video", "good"]`
- `cleaned_text` — tokens joined as a string e.g. `"camera quality video good"`

> **Important note:** `cleaned_text` is used for exploratory analysis and word frequency counts. BERTopic in Section 6 uses the raw `translated_comment` (full natural sentences) for embedding — this gives much better semantic clustering than bag-of-words.

After tokenisation, any comment with 5 or fewer characters in `translated_comment` is dropped as too short to carry meaningful signal.

---

### Section 6 — Topic Modelling (BERTopic)

Discovers the hidden topics users discuss across all comments using **BERTopic**, a state-of-the-art neural topic modelling library. This is the most complex section in the entire pipeline.

#### The BERTopic Pipeline — Step by Step

**Step 1 — Filter short comments**
Only comments with 5 or more words are passed to BERTopic. Very short comments like "good phone" don't embed meaningfully.

**Step 2 — Sentence Embeddings**
`SentenceTransformer('all-MiniLM-L6-v2')` converts each comment into a 384-dimensional semantic vector. Comments with similar meaning end up close together in this vector space.

**Step 3 — Dimensionality Reduction (UMAP)**
384 dimensions → 5 dimensions using UMAP with these specific settings:
```python
UMAP(
    n_neighbors=10,      # Local neighbourhood size — lower = more local structure
    n_components=5,      # Output dimensions
    min_dist=0.0,        # Allow tight clusters
    metric='cosine',     # Cosine distance for text embeddings
    random_state=42,
)
```

**Step 4 — Clustering (HDBSCAN)**
HDBSCAN clusters the 5-dimensional UMAP output:
```python
HDBSCAN(
    min_cluster_size=30,              # Minimum 30 comments to form a topic
    min_samples=5,                    # Core point density threshold
    metric='euclidean',
    cluster_selection_method='eom',   # Excess of Mass — finds compact clusters
    prediction_data=True,             # Needed for outlier reduction
)
```

**Step 5 — Topic Representation (KeyBERTInspired)**
For each cluster, `KeyBERTInspired()` extracts the top 10 most representative keywords using a BERT-based relevance scoring approach. The top 3 keywords become the human-readable `topic_label`, e.g. `"camera, quality, video"`.

**Step 6 — Outlier Reduction (Two-Pass)**
HDBSCAN assigns cluster `-1` to points that don't fit any cluster. Two strategies are applied to rescue these outliers:

*Pass 1 — Probability strategy:*
```python
topic_model.reduce_outliers(
    docs, topics, probabilities=probs,
    strategy='probabilities', threshold=0.05
)
# Any comment with ≥5% probability of belonging to a topic gets assigned
```

*Pass 2 — Cosine similarity fallback:*
For any comments still in cluster `-1` after Pass 1, compute their embeddings, calculate cosine similarity to every topic centroid (mean embedding of all assigned comments), and assign each outlier to its nearest topic.

```python
embeddings = embedding_model.encode(docs, batch_size=256)
centroids  = np.array([
    embeddings[[i for i, t in enumerate(topics) if t == tid]].mean(axis=0)
    for tid in topic_ids
])
sims = cosine_similarity(embeddings[remaining_idx], centroids)
# Each outlier → topic with highest cosine similarity
```

**Step 7 — Build Human-Readable Labels**
```python
topic_labels = {
    tid: ', '.join(w[0] for w in topic_model.get_topic(tid)[:3])
    # e.g. topic 4 → "battery, life, charging"
    # e.g. topic 17 → "camera, quality, video"
}
df['topic_label'] = df['dominant_topic'].map(topic_labels)
```

**Step 8 — Visualise & Save**
Plots the top 15 topics by comment count as a horizontal bar chart for inspection. Saves the full DataFrame to `youtube_topic_model` in batches of 5,000.

---

### Section 7 — Sentiment Analysis (RoBERTa)

Classifies every comment as **Positive**, **Neutral**, or **Negative** using a transformer model fine-tuned specifically for social media text.

#### Model Details

**`cardiffnlp/twitter-roberta-base-sentiment`**
- Base architecture: RoBERTa (Robustly Optimised BERT)
- Fine-tuned on 58 million tweets
- 3-class output: label `0` = Negative, label `1` = Neutral, label `2` = Positive
- Chosen specifically because YouTube comments share the informal, emoji-heavy, abbreviation-rich style of tweets — making this model far more appropriate than models fine-tuned on formal reviews

#### How `get_sentiment_batch()` Works

```python
SENTIMENT_LABELS = ['Negative', 'Neutral', 'Positive']

def get_sentiment_batch(texts: list, batch_size: int = 64) -> list:
    results = []
    for start in tqdm(range(0, len(texts), batch_size)):
        batch  = texts[start: start + batch_size]

        # Tokenise with padding + truncation to 128 tokens
        inputs = sent_tokenizer(
            batch, return_tensors='pt',
            truncation=True, padding=True, max_length=128,
        )
        inputs = {k: v.to(DEVICE) for k, v in inputs.items()}

        # Forward pass — no gradient computation needed
        with torch.no_grad():
            logits = sent_model(**inputs).logits
            preds  = torch.argmax(logits, dim=1).cpu().numpy()
            # argmax picks the class with highest raw score

        results.extend(SENTIMENT_LABELS[p] for p in preds)
    return results
```

**Key design decisions:**
- `batch_size=64` — balances GPU memory usage vs throughput
- `max_length=128` — YouTube comments rarely exceed 128 tokens; truncating longer ones loses only tail content
- `torch.no_grad()` — disables gradient tracking to save memory and speed up inference by ~30%
- `torch.argmax` on raw logits — equivalent to argmax on softmax probabilities, avoids unnecessary computation
- GPU auto-detection — runs on CUDA if available, falls back to CPU seamlessly

**After classification**, prints the full sentiment distribution (e.g. `Positive: 41,203 | Neutral: 28,917 | Negative: 18,378`) and saves to `youtube_Sentiment_Analysis` in batches of 5,000 with a 0.5s sleep between batches to avoid overwhelming the MongoDB connection.

---

### Section 8 — Product Name Mapping

Normalises the raw `product` field (scraped from YouTube search queries) to a canonical product name from the `PRODUCT_NAMES` catalogue in `config.py`.

This is necessary because the raw product string might be `"s25 ultra"`, `"galaxy s25ultra"`, `"Samsung S 25 Ultra"`, or `"samsung25ultra"` — all of which need to map to the single canonical `"samsung galaxy s25 ultra"`.

#### How `map_product_name()` Works

```python
def map_product_name(raw_product: str) -> str:
    lower = str(raw_product).lower()

    # Strategy 1: Exact substring match (fast)
    for product in PRODUCT_NAMES:
        if product in lower:
            return product
            # e.g. raw="iphone 17 pro max review" → "iphone 17 pro max"

    # Strategy 2: Fuzzy match using token_sort_ratio (handles reordering)
    result = process.extractOne(lower, PRODUCT_NAMES, scorer=fuzz.token_sort_ratio)
    if result:
        best, score, _ = result
        return best if score >= 85 else 'Unknown'
        # e.g. raw="pro 17 iphone" → score=91 → "iphone 17 pro"
        # e.g. raw="some random phone" → score=42 → "Unknown"

    return 'Unknown'
```

**Why `token_sort_ratio`?**
`token_sort_ratio` sorts both strings alphabetically before comparing, making it robust to word order differences. `"s25 ultra galaxy samsung"` and `"samsung galaxy s25 ultra"` score 100 with `token_sort_ratio` despite reversed word order.

**Threshold of 85** was chosen through experimentation — high enough to reject false positives (e.g. "phone" matching "iphone") but low enough to catch genuine variations.

After mapping, prints all `Unknown` entries with their frequency counts — this is the signal to add new product variants to `PRODUCT_NAMES` in `config.py`.

---

### Section 9 — Final Assembly & Save

Assembles the final production dataset and saves it to `youtube_final_data`.

**9.1 — Drop Intermediate Collection**
Drops `youtube_translated_comments_main` to free up MongoDB Atlas storage (free tier is 512MB). All its data has already been absorbed into the topic and sentiment collections.

**9.2 — Reload Config & Inspect Topics**
Does `importlib.reload(config)` to pick up any changes made to `BAD_TOPIC_LABELS` since the notebook started running. Prints the top 20 topic labels by frequency for manual review.

**9.3 — Drop Junk Topic Labels**
Filters out rows whose `topic_label` appears in `BAD_TOPIC_LABELS`. These are topics that BERTopic created from noise — stopword clusters, language-detection artifacts, spam patterns. Examples:
```python
BAD_TOPIC_LABELS = [
    "the, is, to",          # Stopword cluster — BERTopic clustered short sentences
    "hai, anna, bhai",      # Hindi words that slipped through language detection
    "sorry, don, re",       # Fragment cluster
    "xai308k, crypto, xai315k",   # Crypto spam
    "dot44h, btc, eth",     # Crypto spam
    "woods, hug, tree",     # Completely off-topic cluster
]
```

**9.4 — Select Final Columns & Save**
Validates that all 5 required columns exist, then saves:
```python
KEEP_COLUMNS = ['video_id', 'translated_comment', 'sentiment', 'topic_label', 'product_name']
```
Saves in batches of 5,000 with 0.3s sleep. Verifies final count via `count_documents({})`.

**9.5 — Optional Re-filter & Spot-check**
Provides optional cells to:
- Re-apply the junk filter after updating `BAD_TOPIC_LABELS` without re-running the whole notebook
- Inspect topic distribution of the cleaned dataset
- Print 10 sample comments per topic for manual quality review

---

### Section 10 — Multi-Cluster Merge *(Optional)*

When new products are processed on **Cluster 3** (isolated from the production data), this section safely merges them into **Cluster 2** (the production RAG cluster) with zero data loss guaranteed.

**Safe merge strategy:**
1. Count documents in Cluster 2 before touching anything
2. Fetch all documents from Cluster 3's `youtube_final_data` using `{'_id': 0}` — this strips the Cluster 3 MongoDB `_id` field so new unique IDs are generated on insert, preventing any ID collision errors
3. Insert into Cluster 2 in batches of 5,000 — purely additive, no `drop()` or `delete_many()` anywhere
4. Count documents in Cluster 2 after and verify `after_count >= before_count`

**Duplicate detection (separate cells):**

*Check cell:*
```python
pipeline = [
    {"$group": {"_id": "$translated_comment", "count": {"$sum": 1}, "ids": {"$push": "$_id"}}},
    {"$match": {"count": {"$gt": 1}}}
]
duplicates = list(final_col2.aggregate(pipeline))
# Reports: N duplicate groups, M total documents to delete
```

*Delete cell:*
```python
ids_to_delete = []
for group in duplicates:
    ids_to_delete.extend(group["ids"][1:])  # Keep first occurrence, delete rest
# Deletes in batches of 5,000
```

The two cells are intentionally separate so you can inspect the duplicate report before committing to any deletion.

---

<br/>

## 🤖 RAG Engine — Deep Dive

> **Files:** `rag_core.py` + `app.py`

The RAG (Retrieval-Augmented Generation) layer sits between the MongoDB database and the user. It retrieves the most relevant comments for a given query, scores them, and sends them to an LLM to generate a structured, grounded summary.

---

### Startup — What Happens When `rag_core.py` Is Imported

When `app.py` imports `rag_core`, three things happen immediately at module load time:

**1. MongoDB connection is established**
```python
_client          = MongoClient(MONGO_URI)        # From config_rag.py
_db              = _client[MONGO_DB_NAME]
final_collection = _db[COLLECTION_FINAL]         # Handle to youtube_final_data
```

**2. Sentiment model is loaded into memory**
```python
sent_tokenizer = SentTokenizer.from_pretrained(SENTIMENT_MODEL)
sent_model     = AutoModelForSequenceClassification.from_pretrained(SENTIMENT_MODEL)
```
> Note: The sentiment model is loaded at import time but is currently not used during RAG queries — it was part of an earlier design. All sentiment data is already pre-computed and stored in MongoDB. The model stays loaded for potential future use.

**3. Groq client is initialised**
```python
groq_client = Groq(api_key=GROQ_API_KEY)
```

This startup approach means models are loaded **once** when the Flask server starts, not on every request. A cold start takes 10–15 seconds but every subsequent query is fast.

---

### Function 1 — `calculate_score(row, query_topic)`

This is the relevance scoring engine. It assigns a numeric score to each comment based on how useful it is expected to be for a given product + topic query.

```python
def calculate_score(row: dict, query_topic: str) -> float:
    score = 0.0

    # ── Signal 1: Sentiment weight ─────────────────────────────────────────
    if row["sentiment"] in ("Positive", "Negative"):
        score += 3.0    # Opinionated comments are most useful
    else:
        score += 0.8    # Neutral comments carry less signal

    # ── Signal 2: Topic label match ────────────────────────────────────────
    if query_topic.lower() in str(row["topic_label"]).lower():
        score += 2.0    # BERTopic confirmed this comment is about the topic

    # ── Signal 3: Direct text mention ─────────────────────────────────────
    if query_topic.lower() in str(row["translated_comment"]).lower():
        score += 0.7    # Comment explicitly mentions the query word

    # ── Signal 4: Length bonus ─────────────────────────────────────────────
    score += min(len(str(row["translated_comment"]).split()) // 10, 2)
    # A 30-word comment gets +3 → capped at +2
    # Longer comments tend to be more detailed and informative

    return score
```

**Score range breakdown:**

| Score | What it means |
|-------|--------------|
| 5.7 | Perfect: Positive/Negative + topic_label match + text mention + long (30+ words) |
| 5.0 | Strong: Positive/Negative + topic_label match + long |
| 3.7 | Good: Positive/Negative + text mention |
| 3.0 | Moderate: Positive/Negative only |
| 2.8 | Weak: Neutral + topic_label match + text mention + long |
| 0.8 | Minimal: Neutral with no topic relevance |

The maximum possible score is **5.7**. This scoring ensures the LLM receives the most opinionated, on-topic, and detailed comments available — maximising summary quality.

---

### Function 2 — `fetch_top_comments(df, product_name, query_topic, max_comments=15)`

Retrieves the best comments for a given product and topic using a two-stage filtering + scoring approach.

```python
def fetch_top_comments(df, product_name, query_topic, max_comments=15):

    # ── Stage 1: Product filter ────────────────────────────────────────────
    product_df = df[
        df["product_name"].str.contains(product_name, case=False, na=False)
    ].copy()
    # Case-insensitive substring match — "iphone 17" matches "iphone 17 pro max"
    # na=False ensures NaN values don't cause errors

    if product_df.empty:
        return pd.DataFrame()   # No data for this product at all

    # ── Stage 2a: Strict text match ────────────────────────────────────────
    topic_df = product_df[
        product_df["translated_comment"].str.contains(query_topic, case=False, na=False)
    ].copy()
    # Looks for the exact query word in the comment text

    # ── Stage 2b: Fallback to topic_label if too few strict matches ────────
    if len(topic_df) < 5:
        topic_df = product_df[
            product_df["topic_label"].str.contains(query_topic, case=False, na=False)
        ].copy()
        # Uses BERTopic's assignment — broader but still relevant

    if len(topic_df) < 3:
        return pd.DataFrame()   # Not enough data to generate a meaningful summary

    # ── Stage 3: Score and rank ────────────────────────────────────────────
    topic_df["score"] = topic_df.apply(
        lambda r: calculate_score(r, query_topic), axis=1
    )
    return topic_df.sort_values("score", ascending=False).head(max_comments)[
        ["translated_comment", "topic_label", "sentiment", "score"]
    ]
```

**The two-stage topic matching strategy is critical.** If someone searches for "battery", most comments won't literally say the word "battery" — they'll say "lasts all day" or "drains fast". BERTopic's topic labels capture this semantic meaning. The fallback ensures good coverage even when the query word isn't explicitly written.

**The minimum threshold of 3 comments** prevents the LLM from generating summaries from too little data — a summary based on 1-2 comments would be misleading.

---

### Function 3 — `generate_summary(comment_list, product_name, query_topic, format_type)`

Sends the retrieved comments to Groq's LLaMA 3 API and returns a structured AI-generated summary.

```python
def generate_summary(comment_list, product_name, query_topic, format_type="bullet"):

    combined = "\n".join([f"- {c}" for c in comment_list])
    # Formats each comment as a bullet point for the prompt

    if format_type == "bullet":
        instruction = (
            f"Analyze these YouTube comments about {product_name} regarding '{query_topic}'.\n"
            f"Summarize in bullet points. Format strictly as:\n\n"
            f"Pros:\n- point\n- point\n\n"
            f"Cons:\n- point\n- point\n\n"
            f"Be specific and concise. Do not repeat points.\n\n"
            f"Comments:\n{combined}"
        )
    else:  # paragraph
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
        temperature=0.3,    # Low temperature = consistent, factual output
    )
    return f"Summary for {product_name} — {query_topic}:\n{response.choices[0].message.content}"
```

**Prompt engineering decisions:**
- `"Format strictly as:"` — forces the model to follow the exact Pros/Cons structure
- `"Be specific and concise. Do not repeat points."` — prevents generic padding and duplicate points
- `temperature=0.3` — low temperature produces deterministic, factual summaries rather than creative ones; this is correct for analysis tasks
- `max_tokens=1024` — enough for 6-8 bullet points per section with room to spare

---

### Function 4 — `query_product_topic_summary(product_name, query_topic, format_type)`

The **end-to-end entry point for Topic Search queries**. Called by `app.py`'s `/api/summary` endpoint.

```python
def query_product_topic_summary(product_name, query_topic, format_type="bullet"):

    # 1. Load ALL documents from youtube_final_data
    df = pd.DataFrame(list(final_collection.find({}, {"_id": 0})))

    if df.empty:
        return "No data found in the database."

    # 2. Retrieve top scored comments
    top_df = fetch_top_comments(df, product_name, query_topic)

    if top_df.empty:
        return f"Not enough data for '{product_name}' – '{query_topic}'. Try a broader topic."

    # 3. Generate and return summary
    return generate_summary(top_df["translated_comment"].tolist(), product_name, query_topic, format_type)
```

**Note on loading all documents:** The entire `youtube_final_data` collection is loaded into a pandas DataFrame on every query. This is intentional for simplicity — with 88K documents at ~200 bytes each, the full load is ~17MB and takes under 2 seconds on a local connection. For a larger dataset, this would need to be replaced with a MongoDB query filter.

---

### Function 5 — `query_product_overall_summary(product_name, format_type)`

The **end-to-end entry point for Overall Experience queries**. Called by `app.py`'s `/api/overall` endpoint. More complex than the topic query — it computes statistics and curates a balanced comment set.

```python
def query_product_overall_summary(product_name, format_type="bullet"):

    df = pd.DataFrame(list(final_collection.find({}, {"_id": 0})))
    product_df = df[df["product_name"].str.contains(product_name, case=False, na=False)]

    # ── 1. Compute sentiment breakdown ────────────────────────────────────
    total    = len(product_df)
    positive = (product_df["sentiment"] == "Positive").sum()
    negative = (product_df["sentiment"] == "Negative").sum()
    neutral  = (product_df["sentiment"] == "Neutral").sum()

    # ── 2. Quality filter — only 8–60 word comments ───────────────────────
    def is_good(text):
        words = str(text).split()
        return 8 <= len(words) <= 60
    # Too short → no signal. Too long → often off-topic rants.

    good_df = product_df[product_df["translated_comment"].apply(is_good)]

    # ── 3. Curate a balanced comment set ──────────────────────────────────
    top_positive = good_df[good_df["sentiment"] == "Positive"]["translated_comment"].head(15)
    top_negative = good_df[good_df["sentiment"] == "Negative"]["translated_comment"].head(15)
    top_neutral  = good_df[good_df["sentiment"] == "Neutral"]["translated_comment"].head(10)
    all_comments = top_positive.tolist() + top_negative.tolist() + top_neutral.tolist()
    # Up to 40 comments total — balanced across sentiment classes

    # ── 4. Find top 5 topics (excluding Uncategorized) ────────────────────
    top_topics = (
        product_df[product_df["topic_label"] != "Uncategorized"]["topic_label"]
        .value_counts().head(5).index.tolist()
    )

    # ── 5. Build prompt with context ──────────────────────────────────────
    # Bullet prompt asks for: Pros / Cons / Overall Verdict
    # Paragraph prompt asks for: 3 paragraphs (love / dislike / verdict)
    # Both prompts specify: "Focus on battery, camera, performance, price, design"

    # ── 6. Format final response ──────────────────────────────────────────
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
```

**Why 8–60 words for the quality filter?**
- Under 8 words: "great phone", "love it", "worth buying" — too vague for the LLM to extract specific insights
- Over 60 words: tends to be long personal stories or off-topic paragraphs that dilute the summary

**Why 15+15+10 comment distribution?**
Positive and negative comments are weighted equally (15 each) to prevent the summary from being skewed by whichever sentiment class has more data. Neutral comments get 10 to add nuance without dominating. This gives the LLM a balanced, representative sample.

---

<br/>

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/your-username/tech-youtube-rag.git && cd tech-youtube-rag

# 2. Virtual environment
python -m venv venv && venv\Scripts\activate.bat   # Windows
# source venv/bin/activate                          # macOS/Linux

# 3. Install
pip install flask flask-cors pymongo[srv] transformers torch groq \
            bertopic sentence-transformers spacy tqdm pandas \
            numpy requests langdetect rapidfuzz umap-learn hdbscan
python -m spacy download en_core_web_sm

# 4. Fill in config.py and config_rag.py with your credentials

# 5. Run pipeline (skip if DB already populated)
jupyter notebook   # Run YouTube_comments_fetching.ipynb, then Data_Cleaning_and_Processing.ipynb

# 6. Start server
python app.py

# 7. Open tech_yt_rag.html in your browser
```

---

<br/>

## 🌐 API Reference

| Method | Endpoint | Body | Description |
|--------|----------|------|-------------|
| `GET` | `/api/health` | — | Server health + record count |
| `GET` | `/api/products` | — | All product names for autocomplete |
| `POST` | `/api/summary` | `{product, topic, format}` | Topic-specific RAG summary |
| `POST` | `/api/overall` | `{product, format}` | Overall experience summary |

`format` accepts `"bullet"` (Pros/Cons) or `"paragraph"` (narrative). Defaults to `"bullet"`.

---

<br/>

## 🧠 Models & Technologies

| Task | Model / Tool | Why This Choice |
|------|-------------|----------------|
| Sentiment | `cardiffnlp/twitter-roberta-base-sentiment` | Fine-tuned on 58M tweets — matches YouTube comment style |
| Topic Modelling | `BERTopic` + `all-MiniLM-L6-v2` | Neural topics with human-readable labels, far better than LDA |
| Text Generation | `Groq llama-3.1-8b-instant` | Sub-2s inference, structured output, free tier available |
| Translation | `Helsinki-NLP/opus-mt-mul-en` + Argos fallback | Handles 100+ languages, fully offline capable |
| Fuzzy Matching | `rapidfuzz token_sort_ratio` | Order-invariant matching, handles "s25 ultra samsung" |
| NLP | `spaCy en_core_web_sm` | Fast lemmatisation for token preparation |
| Database | `MongoDB Atlas` | Flexible schema, cloud-hosted, easy scaling |
| API | `Flask + Flask-CORS` | Lightweight, file:// origin support for HTML UI |

---

<br/>

## 🛍️ Supported Products

<details>
<summary><b>🍎 Apple</b></summary>

iPhone 17 Pro Max · iPhone 17 Pro · iPhone 17 · iPhone Air · iPhone 16 series · iPhone 15 series · MacBook Air M3/M4 · MacBook Pro M3/M4/M5 · Mac Mini M4 · iMac M4 · Mac Studio M4 Max · iPad Pro M5 · iPad Air M3/M4 · Apple Watch Series 9–11 · Apple Watch Ultra 2/3 · AirPods Pro 2/3 · AirPods Max · Apple Vision Pro · AirTag 2

</details>

<details>
<summary><b>📱 Samsung</b></summary>

Galaxy S24/S25/S26 series (base, +, Ultra, Edge) · Galaxy Z Fold 6/7 · Galaxy Z Flip 6/7 · Galaxy Z Trifold · Galaxy A26/A35/A36/A55/A56 · Galaxy Tab S10 series · Galaxy Watch 7/8/Ultra · Galaxy Ring · Galaxy Buds 3/4 Pro · Galaxy Book6 series

</details>

<details>
<summary><b>🔵 Google</b></summary>

Pixel 8 · Pixel 8a · Pixel 9/9a · Pixel 9 Pro/Pro XL/Pro Fold · Pixel 10/10a · Pixel 10 Pro/Pro XL/Pro Fold · Pixel Watch 3/4 · Pixel Buds Pro/Pro 2 · Pixel Tablet/Tablet 2

</details>

<details>
<summary><b>Others</b></summary>

OnePlus 13/13R/15/15R · OnePlus Open 2 · Xiaomi 15/17 series · Xiaomi Mix Fold 4 · Redmi Note 13/14 Pro+ · Oppo Find X8/X9 series · Oppo Find N5 · Realme GT 6/7/8 Pro · Sony WH-1000XM6 · Sony PS5 Pro · Nintendo Switch 2 · Steam Deck OLED

</details>

---

<br/>

## 📜 License

MIT License — free to use, modify, and distribute with attribution.

---

<div align="center">

<br/>

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   Built with  🐍 Python · 🍃 MongoDB · 🤗 HuggingFace       ║
║               ⚡ Groq · 🌐 Flask · 🔵 BERTopic              ║
║                                                              ║
║        If this helped you, drop a ⭐ on GitHub!              ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

</div>
