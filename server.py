"""
Flask backend for AI Sentiment Analysis Web App.
"""

import os
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask(__name__)


@app.route("/")
def home():
    """Render the homepage."""
    return render_template("index.html")


@app.route("/sentimentAnalyzer")
def analyze():
    """Analyze input text and return sentiment output."""
    text = request.args.get("textToAnalyze", "")

    if not text.strip():
        return "Invalid input! Please enter some text."

    result = sentiment_analyzer(text)

    if result["label"] is None:
        return "Unable to analyze sentiment. Please try again later."

    return (
        f"The given text has been identified as {result['label']} "
        f"with a confidence score of {result['score']:.4f}."
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)