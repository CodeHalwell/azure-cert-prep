"""
Azure Translator service wrapper.
"""

import requests
import uuid
from config import settings


class Translator:
    """Azure Translator service client."""

    def __init__(self):
        self.endpoint = settings.translator_endpoint
        self.key = settings.translator_key
        self.region = settings.translator_region

    def translate(
        self, text: str, from_lang: str, to_langs: list[str]
    ) -> list[dict]:
        """
        Translate text to multiple languages.

        Args:
            text: Text to translate
            from_lang: Source language code
            to_langs: List of target language codes

        Returns:
            List of translations
        """
        path = "/translate"
        url = f"{self.endpoint}{path}"

        params = {
            "api-version": "3.0",
            "from": from_lang,
            "to": to_langs,
        }

        headers = {
            "Ocp-Apim-Subscription-Key": self.key,
            "Ocp-Apim-Subscription-Region": self.region,
            "Content-type": "application/json",
            "X-ClientTraceId": str(uuid.uuid4()),
        }

        body = [{"text": text}]

        response = requests.post(url, params=params, headers=headers, json=body)
        response.raise_for_status()

        result = response.json()
        translations = []
        for translation in result[0]["translations"]:
            translations.append({
                "language": translation["to"],
                "text": translation["text"],
            })

        return translations

    def detect_language(self, text: str) -> dict:
        """
        Detect the language of input text.

        Args:
            text: Text to analyze

        Returns:
            Detected language info
        """
        path = "/detect"
        url = f"{self.endpoint}{path}"

        params = {"api-version": "3.0"}

        headers = {
            "Ocp-Apim-Subscription-Key": self.key,
            "Ocp-Apim-Subscription-Region": self.region,
            "Content-type": "application/json",
        }

        body = [{"text": text}]

        response = requests.post(url, params=params, headers=headers, json=body)
        response.raise_for_status()

        result = response.json()
        return {
            "language": result[0]["language"],
            "score": result[0]["score"],
        }

    def get_languages(self) -> dict:
        """
        Get list of supported languages.

        Returns:
            Dictionary of supported languages
        """
        path = "/languages"
        url = f"{self.endpoint}{path}"

        params = {"api-version": "3.0", "scope": "translation"}

        response = requests.get(url, params=params)
        response.raise_for_status()

        return response.json()["translation"]


translator = Translator()
