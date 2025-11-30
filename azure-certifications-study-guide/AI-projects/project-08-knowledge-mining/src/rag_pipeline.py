"""
RAG pipeline for knowledge mining.
"""

from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
from azure.core.credentials import AzureKeyCredential
from openai import AzureOpenAI
import os


class RAGPipeline:
    """Retrieval Augmented Generation pipeline."""

    def __init__(self):
        self.search_client = SearchClient(
            endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
            index_name="knowledge-index",
            credential=AzureKeyCredential(os.getenv("AZURE_SEARCH_KEY")),
        )
        self.openai_client = AzureOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            api_version="2024-02-15-preview",
        )

    def get_embedding(self, text: str) -> list[float]:
        """Get embedding for text."""
        response = self.openai_client.embeddings.create(
            model="text-embedding-3-large",
            input=[text],
        )
        return response.data[0].embedding

    def search(self, query: str, top_k: int = 5) -> list[dict]:
        """Search for relevant documents."""
        query_vector = self.get_embedding(query)
        
        results = self.search_client.search(
            search_text=query,
            vector_queries=[
                VectorizedQuery(
                    vector=query_vector,
                    k_nearest_neighbors=top_k,
                    fields="content_vector",
                )
            ],
            select=["content", "title", "source"],
            top=top_k,
        )
        
        return [
            {
                "content": r["content"],
                "title": r.get("title", ""),
                "source": r.get("source", ""),
                "score": r["@search.score"],
            }
            for r in results
        ]

    def generate_answer(self, query: str, context: list[dict]) -> str:
        """Generate answer based on retrieved context."""
        context_text = "\n\n".join([
            f"Source: {doc['source']}\n{doc['content']}"
            for doc in context
        ])
        
        system_prompt = """You are a helpful assistant that answers questions based on the provided context.
Only use information from the context. If the answer isn't in the context, say so.
Always cite your sources."""

        response = self.openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Context:\n{context_text}\n\nQuestion: {query}"},
            ],
            temperature=0.3,
        )
        
        return response.choices[0].message.content

    def query(self, question: str) -> dict:
        """Full RAG query: search + generate."""
        context = self.search(question)
        answer = self.generate_answer(question, context)
        
        return {
            "question": question,
            "answer": answer,
            "sources": [{"title": c["title"], "source": c["source"]} for c in context],
        }


if __name__ == "__main__":
    import argparse
    from dotenv import load_dotenv
    
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True, help="Question to ask")
    args = parser.parse_args()
    
    pipeline = RAGPipeline()
    result = pipeline.query(args.query)
    
    print(f"Question: {result['question']}")
    print(f"\nAnswer: {result['answer']}")
    print(f"\nSources: {result['sources']}")
