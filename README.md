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

🧹Running Unit Tests
python test_sentiment_analysis.py
Uses mocked API responses
Ensures tests pass even if the Watson API is unavailable
🧹 Static Code Analysis

Run Pylint:

python -m pylint server.py
python -m pylint SentimentAnalysis/sentiment_analysis.py
Ensures code quality and PEP8 compliance
All functions now have docstrings and final newlines
⚠️ Error Handling

The application gracefully handles:

❌ Empty or invalid text input
🌐 API request failure
⏱️ Network timeouts

Example response:

Invalid input! Please enter some text.
Unable to analyze sentiment. Please try again later.
🧠 How It Works
User enters text in the web page input field
JavaScript sends a GET request to the Flask backend
Flask calls Watson NLP API for sentiment analysis
Result (label + confidence score) is returned and displayed

🔮 Future Improvements
🌍 Multi-language support
📊 Sentiment visualization dashboard
🐳 Docker containerization for easier deployment
🔐 Environment variables for API keys
☁️ Continuous deployment and CI/CD via GitHub Actions

👨‍💻 Author

Abiola Olaleye

GitHub: https://github.com/kayorde25

⭐ Acknowledgements

This project uses IBM Watson NLP BERT model for sentiment analysis and is deployed using Render.