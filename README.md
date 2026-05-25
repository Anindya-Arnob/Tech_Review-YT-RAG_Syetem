<div align="center">

<br/>

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║        🎬  T E C H   Y O U T U B E   R A G                  ║
║                                                              ║
║   AI-powered sentiment analysis over YouTube tech reviews    ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![MongoDB](https://img.shields.io/badge/MongoDB_Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/atlas)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co)
[![Groq](https://img.shields.io/badge/Groq_LLaMA_3-F55036?style=for-the-badge&logo=meta&logoColor=white)](https://groq.com)

<br/>

> **Ask any question about any tech product — and get instant AI-generated insights from thousands of real YouTube comments.**

<br/>

</div>

---

## ✨ What It Does

This project builds a **full end-to-end Retrieval-Augmented Generation (RAG) pipeline** on top of YouTube tech review comments. It:

1. **Fetches** YouTube video comments for 100+ tech products (iPhones, Samsung Galaxy, Google Pixel, MacBooks, and more)
2. **Translates** all non-English comments to English using Microsoft Azure Translator
3. **Analyses topics** with BERTopic to understand what users are talking about
4. **Classifies sentiment** using a RoBERTa model fine-tuned on social media text
5. **Stores** everything in MongoDB Atlas across dedicated clusters
6. **Serves** a beautiful web UI where you can query any product + topic and get an AI-generated summary powered by Groq (LLaMA 3)

---

## 🖥️ Screenshots

<br/>

### 🔍 Topic Search — iPhone 17 Pro · Camera

<table>
<tr>
<td><img src="Screenshot_2026-05-26_002415.png" width="400"/></td>
<td><img src="Screenshot_2026-05-26_002438.png" width="400"/></td>
</tr>
<tr>
<td align="center"><i>Query input with autocomplete</i></td>
<td align="center"><i>AI-generated Pros & Cons summary</i></td>
</tr>
</table>

<br/>

### 📊 Overall Experience — Samsung Galaxy S26 · Paragraph Mode

<table>
<tr>
<td><img src="Screenshot_2026-05-26_002648.png" width="400"/></td>
<td><img src="Screenshot_2026-05-26_002752.png" width="400"/></td>
</tr>
<tr>
<td align="center"><i>Sentiment breakdown with top topics</i></td>
<td align="center"><i>Topic search — iMac M4 price analysis</i></td>
</tr>
</table>

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        DATA PIPELINE                            │
│                                                                 │
│  YouTube API  ──►  Comments Fetch  ──►  Translation (Azure)     │
│                                              │                  │
│                                              ▼                  │
│                                      Topic Modelling            │
│                                      (BERTopic)                 │
│                                              │                  │
│                                              ▼                  │
│                                    Sentiment Analysis           │
│                                    (RoBERTa / HuggingFace)      │
│                                              │                  │
│                                              ▼                  │
│                                      MongoDB Atlas              │
│                                    (youtube_final_data)         │
└─────────────────────────────────────────────────────────────────┘
                                              │
                                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                         RAG LAYER                               │
│                                                                 │
│   User Query  ──►  Fetch Top Comments  ──►  Groq LLaMA 3        │
│  (product +         (scored by topic,         │                 │
│   topic)             sentiment, length)        │                 │
│                                               ▼                 │
│                                        AI Summary               │
│                                    (Bullet / Paragraph)         │
└─────────────────────────────────────────────────────────────────┘
                                              │
                                              ▼
                               tech_yt_rag.html  ◄──  Flask API
```

---

## 📁 Project Structure

```
tech-youtube-rag/
│
├── 📓 YouTube_comments_fetching.ipynb      # Stage 1: Fetch videos & comments
├── 📓 Data_Cleaning_and_Processing.ipynb   # Stage 2: Clean → Translate → Topic → Sentiment
│
├── 🐍 app.py                               # Flask backend (API server)
├── 🐍 rag_core.py                          # Core RAG logic (retrieval + generation)
├── 🐍 config.py                            # Pipeline config (clusters, keys, product list)
├── 🐍 config_rag.py                        # RAG-specific config (production cluster)
│
└── 🌐 tech_yt_rag.html                     # Frontend UI (open in browser)
```

---

## ⚙️ Pipeline Stages

### Stage 1 — `YouTube_comments_fetching.ipynb`

| Step | What Happens |
|------|-------------|
| 1 | Connect to MongoDB Cluster |
| 2 | Search YouTube API for product review videos |
| 3 | Deduplicate videos by `video_id` |
| 4 | Fetch up to 500 top-level comments per video |
| 5 | Store raw comments in `youtube_comments` collection |

### Stage 2 — `Data_Cleaning_and_Processing.ipynb`

| Section | What Happens |
|---------|-------------|
| 1–3 | Load raw comments, deduplicate, clean text |
| 4 | Detect language, translate non-English → English (Azure) |
| 5 | Tokenise with spaCy |
| 6 | BERTopic topic modelling + label assignment |
| 7 | Sentiment classification (Negative / Neutral / Positive) |
| 8 | Product name normalisation (exact + fuzzy matching) |
| 9 | Assemble & save final dataset to `youtube_final_data` |
| 10 | *(Optional)* Merge new cluster data into production cluster |

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/your-username/tech-youtube-rag.git
cd tech-youtube-rag
```

### 2. Install dependencies

```bash
pip install flask flask-cors pymongo transformers torch groq \
            bertopic sentence-transformers spacy tqdm pandas \
            requests langdetect
python -m spacy download en_core_web_sm
```

### 3. Configure credentials

Edit `config.py` and `config_rag.py` with your own:
- MongoDB Atlas connection strings
- YouTube Data API keys
- Microsoft Azure Translator keys
- Groq API key

### 4. Run the pipeline *(skip if DB is already populated)*

```bash
# Open and run all cells in order:
jupyter notebook YouTube_comments_fetching.ipynb
jupyter notebook Data_Cleaning_and_Processing.ipynb
```

### 5. Start the Flask server

```bash
python app.py
```

### 6. Open the UI

```
Open tech_yt_rag.html in your browser
```

> The UI auto-connects to `http://localhost:5000` and loads product suggestions from your database.

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/health` | Health check + record count |
| `GET` | `/api/products` | List of all products in DB (for autocomplete) |
| `POST` | `/api/summary` | Topic-specific summary `{ product, topic, format }` |
| `POST` | `/api/overall` | Overall experience summary `{ product, format }` |

---

## 🛍️ Supported Products (100+)

<details>
<summary>Click to expand full product list</summary>

**Apple** — iPhone 14–17 series · MacBook Air/Pro M3–M5 · iMac M4 · Mac Mini M4 · iPad Pro/Air/Mini · Apple Watch Series 9–11 · AirPods Pro 2/3 · Apple Vision Pro

**Samsung** — Galaxy S24/S25/S26 series · Z Fold 6/7 · Z Flip 6/7 · Galaxy Z Trifold · Tab S10 series · Galaxy Watch 7/8 · Galaxy Ring · Galaxy Buds 3/4 Pro

**Google** — Pixel 8–10 series · Pixel Watch 3/4 · Pixel Buds Pro 2 · Pixel Tablet

**OnePlus** — 13 · 13R · 15 · 15R · Open 2 · Nord 4 · Nord CE 4

**Xiaomi** — 15/17 series · Mix Fold 4 · Mix Flip 2 · Redmi Note 13/14 Pro+ · Pad 7 Pro

**Oppo** — Find X8/X9 series · Find N5 · Reno 14 Pro

**Realme** — GT 6/7/8 Pro · 14/15 Pro+

**Others** — Sony WH-1000XM6 · Sony PS5 Pro · Nintendo Switch 2 · Steam Deck OLED

</details>

---

## 🧠 Models Used

| Task | Model |
|------|-------|
| Sentiment Analysis | `cardiffnlp/twitter-roberta-base-sentiment` |
| Topic Modelling | `BERTopic` + `sentence-transformers` |
| Text Generation | `Groq — llama-3.1-8b-instant` |
| Translation | `Microsoft Azure Cognitive Translator` |
| NLP Tokenisation | `spaCy — en_core_web_sm` |

---

## 🗄️ MongoDB Schema

Each document in `youtube_final_data`:

```json
{
  "video_id":           "dQw4w9WgXcQ",
  "translated_comment": "The camera on this phone is absolutely incredible...",
  "topic_label":        "camera, quality, video",
  "sentiment":          "Positive",
  "product_name":       "iphone 17 pro"
}
```

---

## 📜 License

MIT License — free to use, modify, and distribute.

---

<div align="center">

<br/>

**Built with Python · Flask · MongoDB · HuggingFace · Groq · BERTopic**

<br/>

*If this project helped you, give it a ⭐ on GitHub!*

</div>
