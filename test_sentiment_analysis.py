import unittest
from unittest.mock import patch
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    """Test sentiment analyzer using mocked API responses."""

    @patch("SentimentAnalysis.sentiment_analysis.requests.post")
    def test_positive(self, mock_post):
        """Mock a positive response."""
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = '{"documentSentiment": {"label": "SENT_POSITIVE", "score": 0.99}}'
        result = sentiment_analyzer("I love this")
        self.assertEqual(result["label"], "SENT_POSITIVE")

if __name__ == "__main__":
    unittest.main()