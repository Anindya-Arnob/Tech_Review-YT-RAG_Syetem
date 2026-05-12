# Tech YouTube Sentiment RAG Model


## Overview
This project is a Retrieval-Augmented Generation (RAG) based sentiment analysis and summarization model for YouTube comments related to tech products. The goal is to process large-scale comments, perform sentiment classification, topic modeling, and generate summarized insights using Flan-T5. The project follows a structured pipeline to clean, analyze, and extract meaningful insights from YouTube comments. You can check my [blog here](https://medium.com/@sriamirdhasudha/how-ai-reads-customer-feedback-a-rag-powered-approach-to-sentiment-analysis-f5900429cbbf).

- <img width="810" alt="Screenshot 2025-03-10 at 5 36 08 PM" src="https://github.com/user-attachments/assets/262f12a6-d644-476d-a177-ffcea7d408d7" />
- <img width="578" alt="Screenshot 2025-03-10 at 5 41 23 PM" src="https://github.com/user-attachments/assets/de712836-e8e6-4353-8a15-e94e3232cb9e" />
- <img width="568" alt="Screenshot 2025-03-10 at 5 36 50 PM" src="https://github.com/user-attachments/assets/c5b485cd-c869-4930-9d8a-90bc57534b54" />


## Project Workflow (Sections Overview)
The project is divided into eight major sections, each focusing on a critical part of the analysis:

1. MongoDB Setup - Fetching and storing YouTube comments for analysis.

2. Data Cleaning - Handling null values, detecting languages, and translating comments.

3. Text Processing - Stopword removal, tokenization, and preprocessing.

4. Topic Modeling - Using BERTopic for clustering similar topics from comments.

5. Sentiment Analysis - Classifying user comments into sentiment categories.

6. Product Classification - Identifying product mentions in comments.

7. Scoring & Insights Generation - Assigning scores to sentiments and extracting key insights.

8. Summarization with RAG - Using Flan-T5 to generate concise summaries.

## Tech Stack Used

### Programming Language & Environment

* Python - The primary language used for data processing, NLP, and model training.

* Jupyter Notebook - For interactive development and visualization.

### Data Storage & Retrieval

* MongoDB - NoSQL database for storing and retrieving YouTube comments efficiently.

### Natural Language Processing (NLP)

* Hugging Face Transformers - Used for RoBERTa-based Sentiment Analysis.

* RoBERTa - A transformer-based model used for sentiment classification.

* DeepL API - For translating non-English comments into English.

* BERTopic - An advanced topic modeling technique for clustering similar discussions.

* NLTK / SpaCy - Used for text cleaning, stopword removal, and tokenization.

### Machine Learning & Deep Learning

* Flan-T5 (Google’s T5 Model) - Used for text summarization within the RAG framework.

* Scikit-learn - Used for text preprocessing and feature extraction.

* Pandas & NumPy - For handling structured comment data.

### Visualization & Analysis

* Matplotlib & Seaborn - For generating data visualizations.

## Initial MongoDB Setup for YouTube Comments

This section focuses on fetching YouTube comments and storing them in a MongoDB database for efficient querying and retrieval. The goal is to create a structured dataset that can be used for further analysis.

### Tasks Performed:

* Connect to YouTube API (or dataset) to fetch comments.

* Store raw comments in MongoDB for structured access.

* Ensure efficient handling of large-scale text data.

## Data Cleaning

Raw YouTube comments often contain noise like special characters, non-English text, and unnecessary data. This section ensures that only meaningful and properly formatted data is used for further processing.

### Tasks Performed:

* Null Value Handling - Removing empty or incomplete comments.

* Language Detection - Identifying and translating non-English comments using DeepL API.

* Removing special characters and emojis to standardize text.

### Stopword Removal & Tokenization

To improve NLP processing efficiency, we preprocess the text by removing unnecessary words and tokenizing them into meaningful components.

### Tasks Performed:

* Removing Stopwords - Common words that do not contribute to sentiment or topic understanding.

* Tokenization - Breaking text into individual meaningful words or phrases.

* Text Normalization - Converting text to lowercase and standardizing it.

## Topic Modeling with BERTopic

Understanding what people are talking about is crucial. BERTopic is used to group similar comments into topics and identify key discussion points.

### Tasks Performed:

* Applying BERTopic to cluster comments based on content.

* Visualizing major topics using bar charts and word clouds.

* Filtering out irrelevant or generic topics to refine insights.

## Sentiment Analysis

We analyze the emotional tone behind each comment and classify it into Positive, Neutral, or Negative sentiment using RoBERTa.

### Tasks Performed:

* Using Hugging Face’s RoBERTa model for sentiment classification.

* Visualizing sentiment distribution across different topics.

* Deriving meaningful insights from the sentiment breakdown.

## Product Classification

Many comments mention specific tech products. This section attempts to identify product mentions in comments.

### Tasks Performed:

* Keyword-based product extraction from text.

* Matching product names against a predefined list.

* Categorizing comments based on mentioned products.

## Scoring & Insights Generation

To quantify and better understand user sentiment, we assign scores to comments and analyze trends over time.

### Tasks Performed:

* Assigning sentiment scores (e.g., Positive = +1, Neutral = 0, Negative = -1).

* Calculating overall sentiment trends across different tech topics.

* Generating summary statistics for sentiment distribution.

## Summarization with Flan-T5 & RAG

Using Flan-T5, we summarize large volumes of comments into concise insights.

### Tasks Performed:

* Retrieval-Augmented Generation (RAG) framework to enhance summaries.

* Generating key takeaways from thousands of comments.

* Summarizing topic-wise insights for better readability.

##  Installation & Setup

Clone the repository:

`bash 
git clone https://github.com/your-repo/RAG-YouTube-Sentiment.git
cd RAG-YouTube-Sentiment
`
Install dependencies:

`bash
pip install -r requirements.txt
`
## Running the Model

Execute the Jupyter Notebook:

`bash
jupyter notebook Tech_Youtube_Sentiment_RAG_Model.ipynb
`
## Future Enhancements

- More Accurate Summarization - Fine-tuning Flan-T5 for domain-specific summaries.

- Real-Time Sentiment Analysis - Live tracking of YouTube discussions.

- Improved Product Classification - Using NLP-based entity recognition.

## Follow me

- LinkedIn (https://www.linkedin.com/in/sri-amirdha-sudha/)
- Medium (https://medium.com/@sriamirdhasudha)
