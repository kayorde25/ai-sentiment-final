"""
Flask app for AI sentiment analysis.
"""

from flask import Flask, render_template, request

from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask(__name__)


@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")


@app.route("/sentimentAnalyzer")
def analyze():
    """Analyze submitted text and return formatted sentiment output."""
    text = request.args.get("textToAnalyze", "")
    result = sentiment_analyzer(text)

    if result["label"] is None:
        return "Invalid input! Try again."

    return (
        f"The given text has been identified as {result['label']} "
        f"with a confidence score of {result['score']:.4f}."
    )


if __name__ == "__main__":
    app.run(debug=True)
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)