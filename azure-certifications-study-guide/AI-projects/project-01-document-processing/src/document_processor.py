"""
Document processor using Azure Document Intelligence.
Extracts text, tables, and structured data from documents.
"""

from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeResult, AnalyzeDocumentRequest
from azure.core.credentials import AzureKeyCredential
from config import settings


class DocumentProcessor:
    """Processes documents using Azure Document Intelligence."""

    def __init__(self):
        """Initialize the Document Intelligence client."""
        self.client = DocumentIntelligenceClient(
            endpoint=settings.document_intelligence_endpoint,
            credential=AzureKeyCredential(settings.document_intelligence_key),
        )

    def analyze_document(self, document_url: str) -> AnalyzeResult:
        """
        Analyze a document using the prebuilt-layout model.

        Args:
            document_url: URL to the document (with SAS token if needed)

        Returns:
            AnalyzeResult containing extracted content
        """
        poller = self.client.begin_analyze_document(
            "prebuilt-layout",
            AnalyzeDocumentRequest(url_source=document_url),
        )
        return poller.result()

    def analyze_invoice(self, document_url: str) -> AnalyzeResult:
        """
        Analyze an invoice using the prebuilt-invoice model.

        Args:
            document_url: URL to the invoice document

        Returns:
            AnalyzeResult containing invoice fields
        """
        poller = self.client.begin_analyze_document(
            "prebuilt-invoice",
            AnalyzeDocumentRequest(url_source=document_url),
        )
        return poller.result()

    def analyze_receipt(self, document_url: str) -> AnalyzeResult:
        """
        Analyze a receipt using the prebuilt-receipt model.

        Args:
            document_url: URL to the receipt document

        Returns:
            AnalyzeResult containing receipt fields
        """
        poller = self.client.begin_analyze_document(
            "prebuilt-receipt",
            AnalyzeDocumentRequest(url_source=document_url),
        )
        return poller.result()

    def extract_text(self, result: AnalyzeResult) -> str:
        """
        Extract all text content from an analysis result.

        Args:
            result: AnalyzeResult from document analysis

        Returns:
            Concatenated text content
        """
        text_parts = []
        if result.content:
            text_parts.append(result.content)

        return "\n".join(text_parts)

    def extract_tables(self, result: AnalyzeResult) -> list[dict]:
        """
        Extract tables from an analysis result.

        Args:
            result: AnalyzeResult from document analysis

        Returns:
            List of tables as dictionaries
        """
        tables = []
        if result.tables:
            for table in result.tables:
                table_data = {
                    "row_count": table.row_count,
                    "column_count": table.column_count,
                    "cells": [],
                }
                for cell in table.cells:
                    table_data["cells"].append(
                        {
                            "row_index": cell.row_index,
                            "column_index": cell.column_index,
                            "content": cell.content,
                            "kind": cell.kind if hasattr(cell, "kind") else "content",
                        }
                    )
                tables.append(table_data)
        return tables

    def extract_key_value_pairs(self, result: AnalyzeResult) -> list[dict]:
        """
        Extract key-value pairs from an analysis result.

        Args:
            result: AnalyzeResult from document analysis

        Returns:
            List of key-value pair dictionaries
        """
        pairs = []
        if result.key_value_pairs:
            for kvp in result.key_value_pairs:
                key = kvp.key.content if kvp.key else ""
                value = kvp.value.content if kvp.value else ""
                confidence = kvp.confidence if hasattr(kvp, "confidence") else 0.0
                pairs.append({"key": key, "value": value, "confidence": confidence})
        return pairs

    def extract_invoice_fields(self, result: AnalyzeResult) -> dict:
        """
        Extract structured fields from an invoice analysis.

        Args:
            result: AnalyzeResult from invoice analysis

        Returns:
            Dictionary with invoice fields
        """
        invoice_data = {}
        if result.documents:
            for doc in result.documents:
                fields = doc.fields
                if fields:
                    invoice_data = {
                        "vendor_name": self._get_field_value(fields.get("VendorName")),
                        "vendor_address": self._get_field_value(
                            fields.get("VendorAddress")
                        ),
                        "customer_name": self._get_field_value(
                            fields.get("CustomerName")
                        ),
                        "invoice_id": self._get_field_value(fields.get("InvoiceId")),
                        "invoice_date": self._get_field_value(fields.get("InvoiceDate")),
                        "due_date": self._get_field_value(fields.get("DueDate")),
                        "subtotal": self._get_field_value(fields.get("SubTotal")),
                        "total_tax": self._get_field_value(fields.get("TotalTax")),
                        "invoice_total": self._get_field_value(
                            fields.get("InvoiceTotal")
                        ),
                        "amount_due": self._get_field_value(fields.get("AmountDue")),
                    }
        return invoice_data

    def _get_field_value(self, field) -> str | None:
        """Extract value from a document field."""
        if field is None:
            return None
        if hasattr(field, "content"):
            return field.content
        if hasattr(field, "value"):
            return str(field.value)
        return None


# Module-level instance for convenience
document_processor = DocumentProcessor()
