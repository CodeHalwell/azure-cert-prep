"""
Sentiment analysis service using Azure AI Language.
"""

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from config import settings


class SentimentAnalyzer:
    """Azure AI Language sentiment analysis client."""

    def __init__(self):
        credential = AzureKeyCredential(settings.language_key)
        self.client = TextAnalyticsClient(
            endpoint=settings.language_endpoint,
            credential=credential,
        )

    def analyze_sentiment(self, text: str, language: str = "en") -> dict:
        """
        Analyze sentiment of text.

        Args:
            text: Text to analyze
            language: Text language code

        Returns:
            Sentiment analysis result
        """
        documents = [{"id": "1", "language": language, "text": text}]
        
        response = self.client.analyze_sentiment(documents)
        result = response[0]

        if result.is_error:
            raise ValueError(f"Analysis error: {result.error}")

        return {
            "sentiment": result.sentiment,
            "confidence_scores": {
                "positive": result.confidence_scores.positive,
                "neutral": result.confidence_scores.neutral,
                "negative": result.confidence_scores.negative,
            },
            "sentences": [
                {
                    "text": sentence.text,
                    "sentiment": sentence.sentiment,
                    "confidence_scores": {
                        "positive": sentence.confidence_scores.positive,
                        "neutral": sentence.confidence_scores.neutral,
                        "negative": sentence.confidence_scores.negative,
                    },
                }
                for sentence in result.sentences
            ],
        }

    def analyze_with_opinions(self, text: str, language: str = "en") -> dict:
        """
        Analyze sentiment with opinion mining (aspect-based sentiment).

        Args:
            text: Text to analyze
            language: Text language code

        Returns:
            Sentiment with opinions
        """
        documents = [{"id": "1", "language": language, "text": text}]
        
        response = self.client.analyze_sentiment(
            documents,
            show_opinion_mining=True,
        )
        result = response[0]

        if result.is_error:
            raise ValueError(f"Analysis error: {result.error}")

        opinions = []
        for sentence in result.sentences:
            for mined_opinion in sentence.mined_opinions:
                target = mined_opinion.target
                for assessment in mined_opinion.assessments:
                    opinions.append({
                        "target": target.text,
                        "target_sentiment": target.sentiment,
                        "assessment": assessment.text,
                        "assessment_sentiment": assessment.sentiment,
                    })

        return {
            "sentiment": result.sentiment,
            "confidence_scores": {
                "positive": result.confidence_scores.positive,
                "neutral": result.confidence_scores.neutral,
                "negative": result.confidence_scores.negative,
            },
            "opinions": opinions,
        }

    def extract_key_phrases(self, text: str, language: str = "en") -> list[str]:
        """
        Extract key phrases from text.

        Args:
            text: Text to analyze
            language: Text language code

        Returns:
            List of key phrases
        """
        documents = [{"id": "1", "language": language, "text": text}]
        
        response = self.client.extract_key_phrases(documents)
        result = response[0]

        if result.is_error:
            raise ValueError(f"Extraction error: {result.error}")

        return result.key_phrases

    def analyze_batch(self, texts: list[str], language: str = "en") -> list[dict]:
        """
        Analyze sentiment for multiple texts.

        Args:
            texts: List of texts to analyze
            language: Text language code

        Returns:
            List of sentiment results
        """
        documents = [
            {"id": str(i), "language": language, "text": text}
            for i, text in enumerate(texts)
        ]
        
        response = self.client.analyze_sentiment(documents)
        
        results = []
        for result in response:
            if result.is_error:
                results.append({"error": str(result.error)})
            else:
                results.append({
                    "sentiment": result.sentiment,
                    "confidence_scores": {
                        "positive": result.confidence_scores.positive,
                        "neutral": result.confidence_scores.neutral,
                        "negative": result.confidence_scores.negative,
                    },
                })
        
        return results


sentiment_analyzer = SentimentAnalyzer()
