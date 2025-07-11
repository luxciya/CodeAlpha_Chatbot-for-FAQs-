import json
import string
from nltk.corpus import stopwords
from nltk.tokenize import TreebankWordTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk

# Download stopwords only (skip punkt to avoid issue)
nltk.download('stopwords')

tokenizer = TreebankWordTokenizer()
stop_words = set(stopwords.words("english"))

# Sample FAQs
faqs = {
    "What is AI?": "AI stands for Artificial Intelligence.",
    "What is machine learning?": "Machine learning is a subset of AI.",
    "What is deep learning?": "Deep learning is a type of machine learning using neural networks."
}

# Preprocess text
def preprocess(text):
    tokens = tokenizer.tokenize(text.lower())
    return " ".join([t for t in tokens if t not in stop_words and t not in string.punctuation])

# Preprocess corpus
corpus = [preprocess(q) for q in faqs.keys()]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

# Find the most similar FAQ
def get_answer(query):
    query_vec = vectorizer.transform([preprocess(query)])
    similarity = cosine_similarity(query_vec, X)
    idx = similarity.argmax()
    return list(faqs.values())[idx]

# CLI Chat Loop
if __name__ == "__main__":
    print("💬 Welcome to the FAQ Chatbot!")
    print("Type 'exit' to quit.\n")
    while True:
        user_input = input("Ask a question: ")
        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break
        print("Answer:", get_answer(user_input), "\n")
