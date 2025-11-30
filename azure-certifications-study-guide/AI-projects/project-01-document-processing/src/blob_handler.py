"""
Azure Blob Storage handler for document operations.
Provides upload, download, and management functions.
"""

import uuid
from datetime import datetime, timedelta
from azure.storage.blob import (
    BlobServiceClient,
    generate_blob_sas,
    BlobSasPermissions,
)
from config import settings


class BlobHandler:
    """Handles all Azure Blob Storage operations."""

    def __init__(self):
        """Initialize the Blob Storage client."""
        self.blob_service_client = BlobServiceClient.from_connection_string(
            settings.storage_connection_string
        )
        self.container_name = settings.storage_container_name
        self._ensure_container_exists()

    def _ensure_container_exists(self) -> None:
        """Create container if it doesn't exist."""
        container_client = self.blob_service_client.get_container_client(
            self.container_name
        )
        if not container_client.exists():
            container_client.create_container()

    def upload_document(
        self, file_content: bytes, filename: str, content_type: str = "application/pdf"
    ) -> dict:
        """
        Upload a document to blob storage.

        Args:
            file_content: The file content as bytes
            filename: Original filename
            content_type: MIME type of the file

        Returns:
            dict with blob_name, url, and upload_time
        """
        # Generate unique blob name
        blob_name = f"{datetime.utcnow().strftime('%Y/%m/%d')}/{uuid.uuid4()}/{filename}"

        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name, blob=blob_name
        )

        # Upload with metadata
        blob_client.upload_blob(
            file_content,
            content_settings={"content_type": content_type},
            metadata={
                "original_filename": filename,
                "upload_time": datetime.utcnow().isoformat(),
            },
            overwrite=True,
        )

        return {
            "blob_name": blob_name,
            "url": blob_client.url,
            "upload_time": datetime.utcnow().isoformat(),
        }

    def download_document(self, blob_name: str) -> bytes:
        """
        Download a document from blob storage.

        Args:
            blob_name: The blob name/path

        Returns:
            File content as bytes
        """
        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name, blob=blob_name
        )
        download_stream = blob_client.download_blob()
        return download_stream.readall()

    def list_documents(self, prefix: str = "") -> list[dict]:
        """
        List documents in the container.

        Args:
            prefix: Optional path prefix to filter results

        Returns:
            List of document metadata dictionaries
        """
        container_client = self.blob_service_client.get_container_client(
            self.container_name
        )
        blobs = container_client.list_blobs(name_starts_with=prefix)

        return [
            {
                "name": blob.name,
                "size": blob.size,
                "last_modified": blob.last_modified.isoformat(),
                "content_type": blob.content_settings.content_type,
            }
            for blob in blobs
        ]

    def generate_sas_url(self, blob_name: str, expiry_hours: int = 1) -> str:
        """
        Generate a SAS URL for secure document access.

        Args:
            blob_name: The blob name/path
            expiry_hours: Hours until the SAS token expires

        Returns:
            Full URL with SAS token
        """
        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name, blob=blob_name
        )

        # Generate SAS token
        sas_token = generate_blob_sas(
            account_name=self.blob_service_client.account_name,
            container_name=self.container_name,
            blob_name=blob_name,
            account_key=self.blob_service_client.credential.account_key,
            permission=BlobSasPermissions(read=True),
            expiry=datetime.utcnow() + timedelta(hours=expiry_hours),
        )

        return f"{blob_client.url}?{sas_token}"

    def delete_document(self, blob_name: str) -> bool:
        """
        Delete a document from blob storage.

        Args:
            blob_name: The blob name/path

        Returns:
            True if deleted successfully
        """
        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name, blob=blob_name
        )
        blob_client.delete_blob()
        return True


# Module-level instance for convenience
blob_handler = BlobHandler()
