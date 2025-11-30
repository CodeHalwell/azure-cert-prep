"""
Azure Functions app for Sentiment Analysis.
"""

import azure.functions as func
import json
import logging
from datetime import datetime
import uuid

from sentiment_analyzer import sentiment_analyzer

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="analyze", methods=["POST"])
def analyze(req: func.HttpRequest) -> func.HttpResponse:
    """Analyze sentiment of a single text."""
    logging.info("Sentiment analysis request received")

    try:
        body = req.get_json()
        text = body.get("text")
        language = body.get("language", "en")
        include_opinions = body.get("include_opinions", False)

        if not text:
            return func.HttpResponse(
                json.dumps({"error": "Missing 'text' field"}),
                status_code=400,
                mimetype="application/json",
            )

        if include_opinions:
            result = sentiment_analyzer.analyze_with_opinions(text, language)
        else:
            result = sentiment_analyzer.analyze_sentiment(text, language)

        # Add key phrases
        result["key_phrases"] = sentiment_analyzer.extract_key_phrases(text, language)
        result["id"] = str(uuid.uuid4())
        result["timestamp"] = datetime.utcnow().isoformat()

        return func.HttpResponse(
            json.dumps(result),
            status_code=200,
            mimetype="application/json",
        )

    except Exception as e:
        logging.error(f"Analysis error: {e}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json",
        )


@app.route(route="analyze/batch", methods=["POST"])
def analyze_batch(req: func.HttpRequest) -> func.HttpResponse:
    """Analyze sentiment of multiple texts."""
    logging.info("Batch sentiment analysis request received")

    try:
        body = req.get_json()
        texts = body.get("texts", [])
        language = body.get("language", "en")

        if not texts:
            return func.HttpResponse(
                json.dumps({"error": "Missing 'texts' field"}),
                status_code=400,
                mimetype="application/json",
            )

        results = sentiment_analyzer.analyze_batch(texts, language)

        return func.HttpResponse(
            json.dumps({"results": results}),
            status_code=200,
            mimetype="application/json",
        )

    except Exception as e:
        logging.error(f"Batch analysis error: {e}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json",
        )


@app.route(route="key-phrases", methods=["POST"])
def extract_phrases(req: func.HttpRequest) -> func.HttpResponse:
    """Extract key phrases from text."""
    logging.info("Key phrase extraction request received")

    try:
        body = req.get_json()
        text = body.get("text")
        language = body.get("language", "en")

        if not text:
            return func.HttpResponse(
                json.dumps({"error": "Missing 'text' field"}),
                status_code=400,
                mimetype="application/json",
            )

        phrases = sentiment_analyzer.extract_key_phrases(text, language)

        return func.HttpResponse(
            json.dumps({"key_phrases": phrases}),
            status_code=200,
            mimetype="application/json",
        )

    except Exception as e:
        logging.error(f"Extraction error: {e}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json",
        )
