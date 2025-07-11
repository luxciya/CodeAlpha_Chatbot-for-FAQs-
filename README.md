# CodeAlpha_Chatbot-for-FAQs
A simple AI-powered FAQ Chatbot built using Python and NLP. It matches user questions with predefined FAQs using TF-IDF and cosine similarity. This project is a part of an internship task at @CodeAlpha.
This project is a simple chatbot that answers frequently asked questions (FAQs) using **Natural Language Processing (NLP)**. It compares user input with predefined questions and returns the most similar answer using **TF-IDF vectorization** and **cosine similarity**.

> ✅ Developed as **Task 2** for an internship at **@CodeAlpha** under the domain **Artificial Intelligence**.

---

## 🚀 Features

- ✅ Text preprocessing with NLTK (stopword removal, tokenization)
- ✅ TF-IDF vectorizer for transforming text to numerical features
- ✅ Cosine similarity to match user query with best FAQ
- ✅ Command-line chatbot interface

---

## 🛠️ Technologies Used

- Python 3.x
- NLTK
- Scikit-learn

---

## 📦 Installation

1. **Clone the repository** or download ZIP:

git clone https://github.com/your-username/faq-chatbot-nlp.git
cd faq-chatbot-nlp
Create a virtual environment (optional but recommended):
python -m venv venv
venv\Scripts\activate   # For Windows
# or
source venv/bin/activate  # For Mac/Linux

Install dependencies:
pip install -r requirements.txt
Run the chatbot:
python faq_chatbot.py
🧪 Example Interaction
Ask a question: What is AI?
Answer: AI stands for Artificial Intelligence.

Ask a question: What is machine learning?
Answer: Machine learning is a subset of AI.

📝 Project Structure
faq-chatbot/
│
├── faq_chatbot.py        
├── requirements.txt      
└── README.md             

💡 Future Improvements
Web interface using Flask or Streamlit
Dynamic FAQ loading from JSON or CSV
Intent classification with ML or transformers

🙌 Acknowledgments
NLTK
Scikit-learn

Internship at @CodeAlpha
