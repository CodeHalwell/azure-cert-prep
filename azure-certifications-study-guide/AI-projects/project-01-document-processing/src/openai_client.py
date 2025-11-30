"""
Azure OpenAI client for document enhancement.
Provides summarization, entity extraction, and classification.
"""

import json
from openai import AzureOpenAI
from config import settings


class OpenAIClient:
    """Client for Azure OpenAI operations on documents."""

    def __init__(self):
        """Initialize the Azure OpenAI client."""
        self.client = AzureOpenAI(
            azure_endpoint=settings.openai_endpoint,
            api_key=settings.openai_api_key,
            api_version=settings.openai_api_version,
        )
        self.deployment_name = settings.openai_deployment_name

    def summarize_document(self, text: str, max_sentences: int = 3) -> str:
        """
        Generate a summary of the document text.

        Args:
            text: The document text to summarize
            max_sentences: Maximum sentences in summary

        Returns:
            Summary string
        """
        system_prompt = f"""You are a document summarization assistant.
Summarize the following document in {max_sentences} concise sentences.
Focus on the key points and main topics."""

        response = self.client.chat.completions.create(
            model=self.deployment_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Summarize this document:\n\n{text}"},
            ],
            temperature=0.3,
            max_tokens=500,
        )

        return response.choices[0].message.content

    def extract_entities(self, text: str) -> dict:
        """
        Extract named entities from the document.

        Args:
            text: The document text

        Returns:
            Dictionary with entity categories
        """
        system_prompt = """You are a named entity recognition assistant.
Extract entities from the document and categorize them.
Return a JSON object with these categories:
- people: List of person names
- organizations: List of organization names
- locations: List of location names
- dates: List of dates mentioned
- amounts: List of monetary amounts
- products: List of product names

Return ONLY valid JSON, no markdown formatting."""

        response = self.client.chat.completions.create(
            model=self.deployment_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Extract entities from:\n\n{text}"},
            ],
            temperature=0.1,
            max_tokens=1000,
        )

        content = response.choices[0].message.content
        try:
            # Clean up potential markdown formatting
            if content.startswith("```"):
                content = content.split("```")[1]
                if content.startswith("json"):
                    content = content[4:]
            return json.loads(content)
        except json.JSONDecodeError:
            return {
                "people": [],
                "organizations": [],
                "locations": [],
                "dates": [],
                "amounts": [],
                "products": [],
                "raw_response": content,
            }

    def classify_document(self, text: str) -> dict:
        """
        Classify the document type.

        Args:
            text: The document text

        Returns:
            Dictionary with classification and confidence
        """
        system_prompt = """You are a document classification assistant.
Classify the document into one of these categories:
- invoice
- receipt
- contract
- report
- letter
- form
- other

Return a JSON object with:
- category: The document category
- confidence: Your confidence level (high, medium, low)
- reasoning: Brief explanation for the classification

Return ONLY valid JSON, no markdown formatting."""

        response = self.client.chat.completions.create(
            model=self.deployment_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Classify this document:\n\n{text[:2000]}"},
            ],
            temperature=0.1,
            max_tokens=200,
        )

        content = response.choices[0].message.content
        try:
            if content.startswith("```"):
                content = content.split("```")[1]
                if content.startswith("json"):
                    content = content[4:]
            return json.loads(content)
        except json.JSONDecodeError:
            return {
                "category": "other",
                "confidence": "low",
                "reasoning": "Failed to parse classification",
                "raw_response": content,
            }

    def generate_insights(self, text: str, extracted_data: dict) -> str:
        """
        Generate insights based on document content and extracted data.

        Args:
            text: The document text
            extracted_data: Previously extracted structured data

        Returns:
            Insights as formatted text
        """
        context = f"""Document text (truncated): {text[:1500]}

Extracted data: {json.dumps(extracted_data, indent=2)}"""

        system_prompt = """You are a document analysis assistant.
Based on the document content and extracted data, provide:
1. Key observations about the document
2. Any notable patterns or concerns
3. Suggested next actions or follow-ups

Be concise and practical."""

        response = self.client.chat.completions.create(
            model=self.deployment_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": context},
            ],
            temperature=0.5,
            max_tokens=500,
        )

        return response.choices[0].message.content


# Module-level instance for convenience
openai_client = OpenAIClient()
