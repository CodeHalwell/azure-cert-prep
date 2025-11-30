"""
Azure AI Search service for visual search.
"""

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SimpleField,
    SearchableField,
    SearchFieldDataType,
    VectorSearch,
    HnswAlgorithmConfiguration,
    VectorSearchProfile,
    SearchField,
)
from azure.search.documents.models import VectorizedQuery
from config import settings


class SearchService:
    """Azure AI Search client for visual search."""

    def __init__(self):
        self.endpoint = settings.search_endpoint
        self.key = settings.search_key
        self.index_name = settings.search_index
        
        credential = AzureKeyCredential(self.key)
        self.search_client = SearchClient(self.endpoint, self.index_name, credential)
        self.index_client = SearchIndexClient(self.endpoint, credential)

    def create_index(self) -> None:
        """Create the visual search index."""
        fields = [
            SimpleField(name="id", type=SearchFieldDataType.String, key=True),
            SimpleField(name="imageUrl", type=SearchFieldDataType.String),
            SearchField(
                name="embedding",
                type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
                searchable=True,
                vector_search_dimensions=1024,
                vector_search_profile_name="default",
            ),
            SearchableField(name="tags", type=SearchFieldDataType.Collection(SearchFieldDataType.String)),
            SearchableField(name="objects", type=SearchFieldDataType.Collection(SearchFieldDataType.String)),
            SearchableField(name="text", type=SearchFieldDataType.String),
            SearchableField(name="caption", type=SearchFieldDataType.String),
            SimpleField(name="uploadedAt", type=SearchFieldDataType.DateTimeOffset),
        ]

        vector_search = VectorSearch(
            algorithms=[HnswAlgorithmConfiguration(name="default-algorithm")],
            profiles=[VectorSearchProfile(name="default", algorithm_configuration_name="default-algorithm")],
        )

        index = SearchIndex(name=self.index_name, fields=fields, vector_search=vector_search)
        self.index_client.create_or_update_index(index)

    def index_document(self, doc: dict) -> None:
        """
        Index an image document.

        Args:
            doc: Document with id, imageUrl, embedding, tags, objects, text
        """
        self.search_client.upload_documents([doc])

    def vector_search(self, query_vector: list[float], top_k: int = 10) -> list[dict]:
        """
        Search for similar images using vector similarity.

        Args:
            query_vector: Query image embedding
            top_k: Number of results to return

        Returns:
            List of matching documents
        """
        vector_query = VectorizedQuery(
            vector=query_vector,
            k_nearest_neighbors=top_k,
            fields="embedding",
        )

        results = self.search_client.search(
            search_text=None,
            vector_queries=[vector_query],
            select=["id", "imageUrl", "tags", "caption"],
        )

        return [
            {
                "id": result["id"],
                "imageUrl": result["imageUrl"],
                "tags": result.get("tags", []),
                "caption": result.get("caption", ""),
                "score": result["@search.score"],
            }
            for result in results
        ]

    def hybrid_search(
        self, query_text: str, query_vector: list[float] = None, top_k: int = 10
    ) -> list[dict]:
        """
        Hybrid search combining text and vector search.

        Args:
            query_text: Text query
            query_vector: Optional image embedding
            top_k: Number of results

        Returns:
            List of matching documents
        """
        vector_queries = []
        if query_vector:
            vector_queries.append(
                VectorizedQuery(
                    vector=query_vector,
                    k_nearest_neighbors=top_k,
                    fields="embedding",
                )
            )

        results = self.search_client.search(
            search_text=query_text,
            vector_queries=vector_queries if vector_queries else None,
            select=["id", "imageUrl", "tags", "caption"],
            top=top_k,
        )

        return [
            {
                "id": result["id"],
                "imageUrl": result["imageUrl"],
                "tags": result.get("tags", []),
                "caption": result.get("caption", ""),
                "score": result["@search.score"],
            }
            for result in results
        ]


search_service = SearchService()
