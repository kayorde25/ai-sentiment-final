"""
Sentiment analysis module for the Watson NLP API.
"""

import json

import requests


def sentiment_analyzer(text_to_analyze):
    """
    Analyze the sentiment of input text using the Watson NLP API.

    Args:
        text_to_analyze (str): The text to analyze.

    Returns:
        dict: A dictionary containing:
            - label: sentiment label or None
            - score: confidence score or None
    """
    url = (
        "https://sn-watson-sentiment-bert.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/SentimentPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow"
    }
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=10,
        )

        if response.status_code == 200:
            data = json.loads(response.text)
            return {
                "label": data["documentSentiment"]["label"],
                "score": data["documentSentiment"]["score"],
            }

        return {"label": None, "score": None}

    except requests.RequestException:
        return {"label": None, "score": None}