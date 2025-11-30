"""
Azure Computer Vision service for image analysis.
"""

import requests
from config import settings


class VisionService:
    """Azure Computer Vision client."""

    def __init__(self):
        self.endpoint = settings.vision_endpoint
        self.key = settings.vision_key
        self.api_version = "2024-02-01"

    def get_embedding(self, image_url: str) -> list[float]:
        """
        Get vector embedding for an image.

        Args:
            image_url: URL of the image

        Returns:
            1024-dimensional embedding vector
        """
        url = f"{self.endpoint}/computervision/retrieval:vectorizeImage?api-version={self.api_version}"

        headers = {
            "Ocp-Apim-Subscription-Key": self.key,
            "Content-Type": "application/json",
        }

        body = {"url": image_url}

        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()

        return response.json()["vector"]

    def get_embedding_from_bytes(self, image_data: bytes) -> list[float]:
        """
        Get vector embedding from image bytes.

        Args:
            image_data: Image as bytes

        Returns:
            1024-dimensional embedding vector
        """
        url = f"{self.endpoint}/computervision/retrieval:vectorizeImage?api-version={self.api_version}"

        headers = {
            "Ocp-Apim-Subscription-Key": self.key,
            "Content-Type": "application/octet-stream",
        }

        response = requests.post(url, headers=headers, data=image_data)
        response.raise_for_status()

        return response.json()["vector"]

    def analyze_image(self, image_url: str) -> dict:
        """
        Analyze image for tags, objects, and text.

        Args:
            image_url: URL of the image

        Returns:
            Analysis results
        """
        url = f"{self.endpoint}/computervision/imageanalysis:analyze?api-version={self.api_version}"

        headers = {
            "Ocp-Apim-Subscription-Key": self.key,
            "Content-Type": "application/json",
        }

        params = {
            "features": "tags,objects,read,caption",
        }

        body = {"url": image_url}

        response = requests.post(url, headers=headers, params=params, json=body)
        response.raise_for_status()

        result = response.json()

        return {
            "caption": result.get("captionResult", {}).get("text", ""),
            "tags": [tag["name"] for tag in result.get("tagsResult", {}).get("values", [])],
            "objects": [obj["tags"][0]["name"] for obj in result.get("objectsResult", {}).get("values", []) if obj.get("tags")],
            "text": " ".join([line["text"] for block in result.get("readResult", {}).get("blocks", []) for line in block.get("lines", [])]),
        }


vision_service = VisionService()
