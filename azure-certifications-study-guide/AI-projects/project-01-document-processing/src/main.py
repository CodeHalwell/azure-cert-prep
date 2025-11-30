"""
Main application entry point for Document Processing.
Orchestrates the complete document processing pipeline.
"""

import argparse
import json
import logging
import sys
from pathlib import Path

from blob_handler import blob_handler
from document_processor import document_processor
from openai_client import openai_client
from config import settings

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.log_level),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def process_document(file_path: str, document_type: str = "general") -> dict:
    """
    Process a document through the complete pipeline.

    Args:
        file_path: Path to the document file
        document_type: Type of document (general, invoice, receipt)

    Returns:
        Dictionary containing all processing results
    """
    logger.info(f"Starting document processing: {file_path}")
    results = {"status": "processing", "file": file_path}

    try:
        # Step 1: Read and upload document
        logger.info("Step 1: Uploading document to Azure Blob Storage")
        with open(file_path, "rb") as f:
            file_content = f.read()

        filename = Path(file_path).name
        content_type = _get_content_type(filename)
        upload_result = blob_handler.upload_document(file_content, filename, content_type)
        results["upload"] = upload_result
        logger.info(f"Upload complete: {upload_result['blob_name']}")

        # Step 2: Generate SAS URL for Document Intelligence
        logger.info("Step 2: Generating SAS URL")
        sas_url = blob_handler.generate_sas_url(upload_result["blob_name"])
        results["sas_url"] = sas_url

        # Step 3: Analyze document with Document Intelligence
        logger.info("Step 3: Analyzing document with Azure Document Intelligence")
        if document_type == "invoice":
            analysis_result = document_processor.analyze_invoice(sas_url)
            extracted_fields = document_processor.extract_invoice_fields(analysis_result)
            results["invoice_fields"] = extracted_fields
        elif document_type == "receipt":
            analysis_result = document_processor.analyze_receipt(sas_url)
            results["receipt_analysis"] = True
        else:
            analysis_result = document_processor.analyze_document(sas_url)

        # Extract text and tables
        extracted_text = document_processor.extract_text(analysis_result)
        extracted_tables = document_processor.extract_tables(analysis_result)
        extracted_kvp = document_processor.extract_key_value_pairs(analysis_result)

        results["extraction"] = {
            "text_length": len(extracted_text),
            "table_count": len(extracted_tables),
            "key_value_pairs": len(extracted_kvp),
        }
        logger.info(f"Extraction complete: {len(extracted_text)} chars, {len(extracted_tables)} tables")

        # Step 4: Enhance with OpenAI
        logger.info("Step 4: Enhancing with Azure OpenAI")

        # Summarization
        summary = openai_client.summarize_document(extracted_text)
        results["summary"] = summary

        # Entity extraction
        entities = openai_client.extract_entities(extracted_text)
        results["entities"] = entities

        # Classification
        classification = openai_client.classify_document(extracted_text)
        results["classification"] = classification

        # Generate insights
        insights = openai_client.generate_insights(
            extracted_text,
            {
                "tables": extracted_tables,
                "key_value_pairs": extracted_kvp,
                "entities": entities,
            },
        )
        results["insights"] = insights

        results["status"] = "completed"
        logger.info("Document processing completed successfully")

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        results["status"] = "error"
        results["error"] = str(e)
    except Exception as e:
        logger.error(f"Processing error: {e}")
        results["status"] = "error"
        results["error"] = str(e)

    return results


def _get_content_type(filename: str) -> str:
    """Determine content type from filename."""
    ext = Path(filename).suffix.lower()
    content_types = {
        ".pdf": "application/pdf",
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".tiff": "image/tiff",
        ".bmp": "image/bmp",
    }
    return content_types.get(ext, "application/octet-stream")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Intelligent Document Processing with Azure AI"
    )
    parser.add_argument("file", help="Path to the document to process")
    parser.add_argument(
        "--type",
        choices=["general", "invoice", "receipt"],
        default="general",
        help="Document type for specialized processing",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output file for results (JSON)",
    )

    args = parser.parse_args()

    # Process the document
    results = process_document(args.file, args.type)

    # Output results
    output_json = json.dumps(results, indent=2, default=str)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output_json)
        print(f"Results written to: {args.output}")
    else:
        print(output_json)

    # Exit with appropriate code
    sys.exit(0 if results["status"] == "completed" else 1)


if __name__ == "__main__":
    main()
