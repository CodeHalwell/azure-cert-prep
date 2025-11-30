"""
Blocklist management for Content Safety.
"""

import requests
from config import settings


class BlocklistManager:
    """Manage custom blocklists for content moderation."""

    def __init__(self):
        self.endpoint = settings.content_safety_endpoint
        self.key = settings.content_safety_key
        self.api_version = "2024-02-15-preview"

    def create_blocklist(self, name: str, description: str = "") -> dict:
        """
        Create a new blocklist.

        Args:
            name: Blocklist name
            description: Optional description

        Returns:
            Created blocklist info
        """
        url = f"{self.endpoint}/contentsafety/text/blocklists/{name}?api-version={self.api_version}"

        headers = {
            "Ocp-Apim-Subscription-Key": self.key,
            "Content-Type": "application/json",
        }

        body = {"description": description}

        response = requests.patch(url, headers=headers, json=body)
        response.raise_for_status()

        return response.json()

    def add_terms(self, blocklist_name: str, terms: list[str]) -> dict:
        """
        Add terms to a blocklist.

        Args:
            blocklist_name: Name of the blocklist
            terms: List of terms to add

        Returns:
            Operation result
        """
        url = f"{self.endpoint}/contentsafety/text/blocklists/{blocklist_name}:addOrUpdateBlocklistItems?api-version={self.api_version}"

        headers = {
            "Ocp-Apim-Subscription-Key": self.key,
            "Content-Type": "application/json",
        }

        body = {
            "blocklistItems": [{"text": term} for term in terms]
        }

        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()

        return response.json()

    def remove_terms(self, blocklist_name: str, item_ids: list[str]) -> None:
        """
        Remove terms from a blocklist.

        Args:
            blocklist_name: Name of the blocklist
            item_ids: List of item IDs to remove
        """
        url = f"{self.endpoint}/contentsafety/text/blocklists/{blocklist_name}:removeBlocklistItems?api-version={self.api_version}"

        headers = {
            "Ocp-Apim-Subscription-Key": self.key,
            "Content-Type": "application/json",
        }

        body = {"blocklistItemIds": item_ids}

        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()

    def list_blocklists(self) -> list[dict]:
        """
        List all blocklists.

        Returns:
            List of blocklist info
        """
        url = f"{self.endpoint}/contentsafety/text/blocklists?api-version={self.api_version}"

        headers = {"Ocp-Apim-Subscription-Key": self.key}

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return response.json().get("value", [])

    def get_blocklist_items(self, blocklist_name: str) -> list[dict]:
        """
        Get items in a blocklist.

        Args:
            blocklist_name: Name of the blocklist

        Returns:
            List of blocklist items
        """
        url = f"{self.endpoint}/contentsafety/text/blocklists/{blocklist_name}/blocklistItems?api-version={self.api_version}"

        headers = {"Ocp-Apim-Subscription-Key": self.key}

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return response.json().get("value", [])


blocklist_manager = BlocklistManager()
