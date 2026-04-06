"""
Flask backend for AI Sentiment Analysis Web App
Author: Abiola Olaleye
Purpose: Serve a web interface to analyze text sentiment using Watson NLP API
"""

import os
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# Initialize Flask app
app = Flask(__name__)


@app.route("/")
def home():
    """
    Render the homepage with input field and analyze button.
    """
    return render_template("index.html")


@app.route("/sentimentAnalyzer")
def analyze():
    """
    Receive text input from the frontend, analyze sentiment, and return a formatted result.

    Handles:
    - Invalid input (empty text)
    - API failure (returns label=None)
    """
    text = request.args.get("textToAnalyze", "")

    # Check for empty input
    if not text.strip():
        return "Invalid input! Please enter some text."

    # Call sentiment analyzer
    result = sentiment_analyzer(text)

    # Handle failed analysis
    if result["label"] is None:
        return "Unable to analyze sentiment. Please try again later."

    # Return formatted result
    return (
        f"The given text has been identified as {result['label']} "
        f"with a confidence score of {result['score']:.4f}."
    )


if __name__ == "__main__":
    # Use Render-assigned PORT or fallback to 5000 for local testing
    port = int(os.environ.get("PORT", 5000))

    # Bind to 0.0.0.0 so Render can access the app externally
    # Production-safe: debug=False
    app.run(host="0.0.0.0", port=port, debug=False)