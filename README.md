# toneshift-ai
An AI-powered message rewriting app built with Python, Streamlit, and Google Gemini. Supports multiple writing tones and uses TF-IDF-based retrieval to incorporate relevant writing guidance through a simple RAG pipeline.
## ⚙️ Installation

    git clone https://github.com/<your-username>/toneshift-ai.git
    cd toneshift-ai
    pip install -r requirements.txt
    streamlit run app.py

## 🚀 Features
- Five tones: Professional, Friendly, Polite, Confident, Concise
- Length control: same length, shorter, or a little more detail

## 🧠 How It Works
1. **Input:** enter a message, choose tone and length
2. **Retrieval (RAG):** the guide is split into passages and ranked with TF-IDF (unigrams + bigrams) and cosine similarity; the top 3 are selected
3. **Prompt engineering:** message, tone, length and retrieved context are combined
4. **Generation:** Gemini returns the rewritten message