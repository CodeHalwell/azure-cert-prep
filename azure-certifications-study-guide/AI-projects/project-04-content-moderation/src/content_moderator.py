"""
Content moderation service using Azure AI Content Safety.
"""

import requests
from config import settings


class ContentModerator:
    """Azure AI Content Safety client."""

    def __init__(self):
        self.endpoint = settings.content_safety_endpoint
        self.key = settings.content_safety_key
        self.api_version = "2024-02-15-preview"

    def analyze_text(self, text: str, blocklist_names: list[str] = None) -> dict:
        """
        Analyze text for harmful content.

        Args:
            text: Text to analyze
            blocklist_names: Optional list of blocklist names to check

        Returns:
            Analysis result with categories and decision
        """
        url = f"{self.endpoint}/contentsafety/text:analyze?api-version={self.api_version}"

        headers = {
            "Ocp-Apim-Subscription-Key": self.key,
            "Content-Type": "application/json",
        }

        body = {
            "text": text,
            "categories": ["Hate", "Violence", "Sexual", "SelfHarm"],
            "outputType": "FourSeverityLevels",
        }

        if blocklist_names:
            body["blocklistNames"] = blocklist_names

        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()

        result = response.json()
        return self._process_result(result)

    def analyze_image(self, image_data: bytes) -> dict:
        """
        Analyze image for harmful content.

        Args:
            image_data: Image bytes

        Returns:
            Analysis result with categories and decision
        """
        url = f"{self.endpoint}/contentsafety/image:analyze?api-version={self.api_version}"

        headers = {
            "Ocp-Apim-Subscription-Key": self.key,
            "Content-Type": "application/json",
        }

        import base64
        image_base64 = base64.b64encode(image_data).decode("utf-8")

        body = {
            "image": {"content": image_base64},
            "categories": ["Hate", "Violence", "Sexual", "SelfHarm"],
        }

        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()

        result = response.json()
        return self._process_result(result)

    def _process_result(self, result: dict) -> dict:
        """Process API result and determine decision."""
        categories = result.get("categoriesAnalysis", [])
        blocklist_matches = result.get("blocklistsMatch", [])

        max_severity = 0
        for category in categories:
            if category.get("severity", 0) > max_severity:
                max_severity = category["severity"]

        # Determine decision based on thresholds
        if blocklist_matches or max_severity >= settings.threshold_block:
            decision = "block"
        elif max_severity >= settings.threshold_review:
            decision = "review"
        elif max_severity >= settings.threshold_safe:
            decision = "log"
        else:
            decision = "approve"

        return {
            "categoriesAnalysis": categories,
            "blocklistsMatch": blocklist_matches,
            "maxSeverity": max_severity,
            "decision": decision,
        }


content_moderator = ContentModerator()
