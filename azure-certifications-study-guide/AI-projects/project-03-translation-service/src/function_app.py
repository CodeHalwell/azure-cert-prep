"""
Azure Functions app for Translation Service.
"""

import azure.functions as func
import json
import logging

from translator import translator
from speech_service import speech_service

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="translate", methods=["POST"])
def translate(req: func.HttpRequest) -> func.HttpResponse:
    """Translate text to target languages."""
    logging.info("Translation request received")

    try:
        body = req.get_json()
        text = body.get("text")
        from_lang = body.get("from", "en")
        to_langs = body.get("to", ["es"])

        if not text:
            return func.HttpResponse(
                json.dumps({"error": "Missing 'text' field"}),
                status_code=400,
                mimetype="application/json",
            )

        if isinstance(to_langs, str):
            to_langs = [to_langs]

        translations = translator.translate(text, from_lang, to_langs)

        return func.HttpResponse(
            json.dumps({"translations": translations}),
            status_code=200,
            mimetype="application/json",
        )

    except Exception as e:
        logging.error(f"Translation error: {e}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json",
        )


@app.route(route="detect", methods=["POST"])
def detect_language(req: func.HttpRequest) -> func.HttpResponse:
    """Detect the language of input text."""
    logging.info("Language detection request received")

    try:
        body = req.get_json()
        text = body.get("text")

        if not text:
            return func.HttpResponse(
                json.dumps({"error": "Missing 'text' field"}),
                status_code=400,
                mimetype="application/json",
            )

        result = translator.detect_language(text)

        return func.HttpResponse(
            json.dumps(result),
            status_code=200,
            mimetype="application/json",
        )

    except Exception as e:
        logging.error(f"Detection error: {e}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json",
        )


@app.route(route="languages", methods=["GET"])
def get_languages(req: func.HttpRequest) -> func.HttpResponse:
    """Get list of supported languages."""
    try:
        languages = translator.get_languages()
        return func.HttpResponse(
            json.dumps(languages),
            status_code=200,
            mimetype="application/json",
        )
    except Exception as e:
        logging.error(f"Error getting languages: {e}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json",
        )


@app.route(route="speech-to-text", methods=["POST"])
def speech_to_text(req: func.HttpRequest) -> func.HttpResponse:
    """Convert speech audio to text."""
    logging.info("Speech-to-text request received")

    try:
        audio_data = req.get_body()
        language = req.params.get("language", "en-US")
        translate_to = req.params.get("translateTo")

        if not audio_data:
            return func.HttpResponse(
                json.dumps({"error": "No audio data provided"}),
                status_code=400,
                mimetype="application/json",
            )

        text = speech_service.speech_to_text(audio_data, language)

        result = {"text": text, "language": language}

        # Optionally translate
        if translate_to:
            translations = translator.translate(text, language[:2], [translate_to])
            result["translations"] = translations

        return func.HttpResponse(
            json.dumps(result),
            status_code=200,
            mimetype="application/json",
        )

    except Exception as e:
        logging.error(f"Speech-to-text error: {e}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json",
        )


@app.route(route="text-to-speech", methods=["POST"])
def text_to_speech(req: func.HttpRequest) -> func.HttpResponse:
    """Convert text to speech audio."""
    logging.info("Text-to-speech request received")

    try:
        body = req.get_json()
        text = body.get("text")
        language = body.get("language", "en-US")
        voice = body.get("voice")

        if not text:
            return func.HttpResponse(
                json.dumps({"error": "Missing 'text' field"}),
                status_code=400,
                mimetype="application/json",
            )

        audio_data = speech_service.text_to_speech(text, language, voice)

        return func.HttpResponse(
            audio_data,
            status_code=200,
            mimetype="audio/wav",
        )

    except Exception as e:
        logging.error(f"Text-to-speech error: {e}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json",
        )
