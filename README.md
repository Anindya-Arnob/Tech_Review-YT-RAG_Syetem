# 🎬 Tech YouTube Sentiment RAG Model

> Retrieval-Augmented Generation (RAG) pipeline for sentiment analysis,
> topic modeling, and AI-powered summarization of tech product YouTube comments.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow?style=for-the-badge&logo=huggingface&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-NoSQL-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![RAG](https://img.shields.io/badge/RAG-Flan--T5-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-Open%20Source-brightgreen?style=for-the-badge)

---

## 📌 Overview

Tech products generate **thousands of YouTube comments daily** — but manually
reading them all is impossible. This project builds an end-to-end **RAG-powered
NLP pipeline** that automatically:

- 🧹 Cleans and translates multilingual comments
- 🗂️ Clusters discussions into topics using **BERTopic**
- 🎭 Classifies sentiment using **RoBERTa**
- 🏷️ Identifies product mentions automatically
- 📝 Generates concise AI summaries using **Flan-T5**

---

## 🏗️ Project Architecture
---

## ✨ Key Features

- ☁️ **MongoDB Integration** — scalable NoSQL storage for large-scale comment data
- 🌍 **Multilingual Support** — auto-detects and translates non-English comments
  via DeepL API
- 🗂️ **BERTopic Clustering** — groups comments into meaningful discussion topics
- 🎭 **RoBERTa Sentiment** — transformer-based 3-class classification
  (Positive / Neutral / Negative)
- 🏷️ **Product Detection** — extracts and categorizes tech product mentions
- 📊 **Sentiment Scoring** — quantifies trends across topics and time
- 📝 **RAG Summarization** — Flan-T5 generates concise, readable insight summaries

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| **Language** | Python 3.10+ |
| **Environment** | Jupyter Notebook |
| **Data Storage** | MongoDB (NoSQL) |
| **Sentiment Model** | RoBERTa (Hugging Face Transformers) |
| **Summarization** | Flan-T5 (Google, via Hugging Face) |
| **Topic Modeling** | BERTopic |
| **Translation** | DeepL API |
| **NLP Utilities** | NLTK, SpaCy |
| **ML / Data** | Scikit-learn, Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |

---

## 🔄 Pipeline Walkthrough

### 1️⃣ MongoDB Setup
- Connect to YouTube API to fetch comments at scale
- Store raw comments in MongoDB for structured querying
- Handles large-scale text data efficiently

### 2️⃣ Data Cleaning
- Remove null, empty, and malformed entries
- Detect comment language automatically
- Translate non-English comments to English via **DeepL API**
- Strip special characters, emojis, and noise

### 3️⃣ Text Processing
- **Stopword Removal** — eliminate low-signal filler words
- **Tokenization** — split text into meaningful units
- **Normalization** — lowercase, standardize, clean whitespace

### 4️⃣ Topic Modeling with BERTopic
- Cluster semantically similar comments into topics
- Visualize major discussion themes with bar charts and word clouds
- Filter irrelevant or generic topics for cleaner insights

### 5️⃣ Sentiment Analysis with RoBERTa
- Classify each comment as **Positive**, **Neutral**, or **Negative**
- Visualize sentiment distribution per topic
- Extract sentiment breakdown statistics

### 6️⃣ Product Classification
- Keyword-based extraction of tech product mentions
- Match against a predefined product list
- Categorize comments by product for targeted analysis

### 7️⃣ Scoring & Insights Generation
- Assign numeric sentiment scores per comment
  (`Positive = +1`, `Neutral = 0`, `Negative = -1`)
- Calculate overall sentiment trends across topics
- Generate summary statistics and trend reports

### 8️⃣ RAG Summarization with Flan-T5
- **Retrieval-Augmented Generation** framework for context-aware summaries
- Summarize thousands of comments into concise key takeaways
- Generate topic-wise insight reports for easy readability

---

## ⚙️ Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/Anindya-Arnob/RAG-YouTube-Sentiment.git
cd RAG-YouTube-Sentiment

```

---

## 🚀 Running the Model

```bash
jupyter notebook Tech_Youtube_Sentiment_RAG_Model.ipynb
```

Run cells sequentially from top to bottom — each section builds on the previous.

---

## 📁 Project Structure
---

## 🔑 Key Concepts Demonstrated

| Concept | Implementation |
|---------|---------------|
| **RAG (Retrieval-Augmented Generation)** | Flan-T5 summarization with retrieved comment context |
| **Transformer Sentiment Analysis** | Fine-tuned RoBERTa for 3-class classification |
| **Topic Modeling** | BERTopic for unsupervised comment clustering |
| **Vector Embeddings** | Sentence embeddings used in BERTopic clustering |
| **Tokenization** | NLTK / SpaCy text preprocessing pipeline |
| **Multilingual NLP** | DeepL API for language detection and translation |
| **NoSQL at Scale** | MongoDB for efficient large-scale comment storage |

---

## 🔮 Future Enhancements

- [ ] Fine-tune Flan-T5 for domain-specific tech summarization
- [ ] Real-time sentiment tracking of live YouTube discussions
- [ ] NLP-based Named Entity Recognition for product classification
- [ ] Dashboard UI for interactive sentiment exploration
- [ ] Support for additional platforms (Reddit, Twitter/X)

---

## 👤 Author

**Anindya Roy Chowdhury**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/anindya-roy-chowdhury-929bb1255)


---

## 📜 License

This project is open-source. For inquiries or contributions,
please open an issue in the repository.

---

⭐ **If this project helped you, please give it a star!**
