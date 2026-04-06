# AI Sentiment Analysis
# 🧠 AI Sentiment Analysis Web App

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)](https://flask.palletsprojects.com/)
[![Status](https://img.shields.io/badge/Status-Active-success)]()

---

## 📌 Overview

This project is a **web-based sentiment analysis application** that uses **IBM Watson NLP (BERT model)** to classify text as:

- ✅ Positive  
- ❌ Negative  
- ⚖️ Neutral  

The application is built with:

- **Flask** (backend)
- **JavaScript (Fetch API)** (frontend interaction)
- **Watson NLP API** (AI model)

---

## 🚀 Features

- 🔍 Real-time sentiment analysis
- 🌐 Web interface (HTML + JS)
- ⚠️ Robust error handling for invalid inputs
- 🧪 Unit testing with mocking (no API dependency)
- 🧹 Static code analysis using `pylint`
- 📦 Modular Python package structure

---

## 🗂️ Project Structure


Simple Flask app using Watson NLP for sentiment analysis.


AI-sentiment-final/
├── SentimentAnalysis/
│ ├── init.py
│ └── sentiment_analysis.py
├── templates/
│ └── index.html
├── static/
│ └── mywebscript.js
├── server.py
├── test_sentiment_analysis.py
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/kayorde25/AI-sentiment-final.git
cd AI-sentiment-final

Install dependencies
pip install -r requirements.txt

2. Install dependencies
pip install -r requirements.txt
▶️ Running the Application
python server.py

Then open your browser:

http://127.0.0.1:5000
🧪 Running Unit Tests
python test_sentiment_analysis.py

✔ Uses mocking to simulate API responses
✔ Does not depend on external API availability

🧹 Static Code Analysis

Run pylint:

python -m pylint server.py
python -m pylint SentimentAnalysis/sentiment_analysis.py

✔ Ensures code quality and PEP8 compliance

⚠️ Error Handling

The application gracefully handles:

❌ Invalid input text
🌐 API failures
⏱️ Network timeouts

Example response:

Invalid input! Try again.
🧠 How It Works
User enters text in the browser
JavaScript sends a GET request to Flask
Flask calls Watson NLP API
API returns sentiment + confidence score
Result is displayed to the user
📷 Example Output
The given text has been identified as SENT_POSITIVE with a confidence score of 0.9976.

🔮 Future Improvements
🌍 Multi-language support
📊 Sentiment visualization dashboard
🐳 Docker containerization
☁️ Cloud deployment (Render / AWS / GCP)
🔐 API key security and environment variables

👨‍💻 Author

Abiola Olaleye

GitHub: https://github.com/kayorde25
