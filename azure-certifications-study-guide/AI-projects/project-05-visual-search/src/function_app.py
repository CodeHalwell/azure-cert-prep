"""
Azure Functions app for Visual Search.
"""

import azure.functions as func
import json
import logging
import uuid
from datetime import datetime

from vision_service import vision_service
from search_service import search_service

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="search", methods=["POST"])
def search_by_image(req: func.HttpRequest) -> func.HttpResponse:
    """Search for similar images using a query image."""
    logging.info("Visual search request received")

    try:
        image_data = req.get_body()
        top_k = int(req.params.get("top", 10))

        if not image_data:
            return func.HttpResponse(
                json.dumps({"error": "No image data provided"}),
                status_code=400,
                mimetype="application/json",
            )

        # Get embedding for query image
        embedding = vision_service.get_embedding_from_bytes(image_data)

        # Search for similar images
        results = search_service.vector_search(embedding, top_k)

        return func.HttpResponse(
            json.dumps({"results": results}),
            status_code=200,
            mimetype="application/json",
        )

    except Exception as e:
        logging.error(f"Search error: {e}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json",
        )


@app.route(route="search/hybrid", methods=["POST"])
def hybrid_search(req: func.HttpRequest) -> func.HttpResponse:
    """Hybrid search with text and optional image."""
    logging.info("Hybrid search request received")

    try:
        body = req.get_json()
        query_text = body.get("text", "")
        top_k = body.get("top", 10)

        results = search_service.hybrid_search(query_text, top_k=top_k)

        return func.HttpResponse(
            json.dumps({"results": results}),
            status_code=200,
            mimetype="application/json",
        )

    except Exception as e:
        logging.error(f"Hybrid search error: {e}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json",
        )


@app.route(route="index", methods=["POST"])
def index_image(req: func.HttpRequest) -> func.HttpResponse:
    """Index an image from URL."""
    logging.info("Index image request received")

    try:
        body = req.get_json()
        image_url = body.get("imageUrl")

        if not image_url:
            return func.HttpResponse(
                json.dumps({"error": "Missing 'imageUrl' field"}),
                status_code=400,
                mimetype="application/json",
            )

        # Get embedding
        embedding = vision_service.get_embedding(image_url)

        # Analyze image
        analysis = vision_service.analyze_image(image_url)

        # Create document
        doc = {
            "id": str(uuid.uuid4()),
            "imageUrl": image_url,
            "embedding": embedding,
            "tags": analysis["tags"],
            "objects": analysis["objects"],
            "text": analysis["text"],
            "caption": analysis["caption"],
            "uploadedAt": datetime.utcnow().isoformat(),
        }

        # Index document
        search_service.index_document(doc)

        return func.HttpResponse(
            json.dumps({"id": doc["id"], "status": "indexed"}),
            status_code=201,
            mimetype="application/json",
        )

    except Exception as e:
        logging.error(f"Index error: {e}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json",
        )


@app.route(route="index/create", methods=["POST"])
def create_index(req: func.HttpRequest) -> func.HttpResponse:
    """Create the search index."""
    try:
        search_service.create_index()
        return func.HttpResponse(
            json.dumps({"status": "index created"}),
            status_code=201,
            mimetype="application/json",
        )
    except Exception as e:
        logging.error(f"Create index error: {e}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json",
        )
