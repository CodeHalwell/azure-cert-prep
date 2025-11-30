"""
Azure Functions app for Content Moderation.
"""

import azure.functions as func
import json
import logging

from content_moderator import content_moderator
from blocklist_manager import blocklist_manager

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="moderate-text", methods=["POST"])
def moderate_text(req: func.HttpRequest) -> func.HttpResponse:
    """Moderate text content."""
    logging.info("Text moderation request received")

    try:
        body = req.get_json()
        text = body.get("text")
        blocklists = body.get("blocklists", [])

        if not text:
            return func.HttpResponse(
                json.dumps({"error": "Missing 'text' field"}),
                status_code=400,
                mimetype="application/json",
            )

        result = content_moderator.analyze_text(text, blocklists)

        return func.HttpResponse(
            json.dumps(result),
            status_code=200,
            mimetype="application/json",
        )

    except Exception as e:
        logging.error(f"Moderation error: {e}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json",
        )


@app.route(route="moderate-image", methods=["POST"])
def moderate_image(req: func.HttpRequest) -> func.HttpResponse:
    """Moderate image content."""
    logging.info("Image moderation request received")

    try:
        image_data = req.get_body()

        if not image_data:
            return func.HttpResponse(
                json.dumps({"error": "No image data provided"}),
                status_code=400,
                mimetype="application/json",
            )

        result = content_moderator.analyze_image(image_data)

        return func.HttpResponse(
            json.dumps(result),
            status_code=200,
            mimetype="application/json",
        )

    except Exception as e:
        logging.error(f"Image moderation error: {e}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json",
        )


@app.route(route="blocklists", methods=["GET"])
def list_blocklists(req: func.HttpRequest) -> func.HttpResponse:
    """List all blocklists."""
    try:
        blocklists = blocklist_manager.list_blocklists()
        return func.HttpResponse(
            json.dumps({"blocklists": blocklists}),
            status_code=200,
            mimetype="application/json",
        )
    except Exception as e:
        logging.error(f"Error listing blocklists: {e}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json",
        )


@app.route(route="blocklists/{name}", methods=["PUT"])
def create_blocklist(req: func.HttpRequest) -> func.HttpResponse:
    """Create a new blocklist."""
    try:
        name = req.route_params.get("name")
        body = req.get_json()
        description = body.get("description", "")

        result = blocklist_manager.create_blocklist(name, description)

        return func.HttpResponse(
            json.dumps(result),
            status_code=201,
            mimetype="application/json",
        )
    except Exception as e:
        logging.error(f"Error creating blocklist: {e}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json",
        )


@app.route(route="blocklists/{name}/terms", methods=["POST"])
def add_blocklist_terms(req: func.HttpRequest) -> func.HttpResponse:
    """Add terms to a blocklist."""
    try:
        name = req.route_params.get("name")
        body = req.get_json()
        terms = body.get("terms", [])

        if not terms:
            return func.HttpResponse(
                json.dumps({"error": "Missing 'terms' field"}),
                status_code=400,
                mimetype="application/json",
            )

        result = blocklist_manager.add_terms(name, terms)

        return func.HttpResponse(
            json.dumps(result),
            status_code=200,
            mimetype="application/json",
        )
    except Exception as e:
        logging.error(f"Error adding terms: {e}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json",
        )
