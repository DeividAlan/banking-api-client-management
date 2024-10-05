from flask import Blueprint, jsonify, request
from flasgger import swag_from
from src.views.http_types.http_request import HttpRequest
from src.main.composer.legal_entity_client_create_composer import (
    legal_entity_client_create_composer,
)
from src.main.composer.legal_entity_client_list_composer import legal_entity_client_list_composer
from src.main.composer.legal_entity_client_find_composer import legal_entity_client_find_composer
from src.main.composer.legal_entity_client_withdraw_composer import (
    legal_entity_client_withdraw_composer,
)
from src.errors.error_handler import handle_errors

legal_entity_client_routes_bp = Blueprint("legal_entity_client_routes", __name__)


@legal_entity_client_routes_bp.route("/legal_entity_client", methods=["POST"])
@swag_from(
    {
        "tags": ["Legal Entity Client"],
        "description": "Create a new legal entity client",
        "parameters": [
            {
                "name": "body",
                "in": "body",
                "required": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "email": {"type": "string"},
                        "phone": {"type": "string"},
                        "business_name": {"type": "string"},
                        "revenue": {"type": "number"},
                        "corporate_email": {"type": "string"},
                        "category": {"type": "string"},
                        "balance": {"type": "number"},
                    },
                    "required": [
                        "name",
                        "email",
                        "business_name",
                        "revenue",
                        "corporate_email",
                        "category",
                        "balance",
                    ],
                },
            }
        ],
        "responses": {
            "200": {"description": "Client created successfully"},
            "400": {"description": "Invalid request"},
        },
    }
)
def create_legal_entity_client():
    try:
        http_request = HttpRequest(body=request.json)
        view = legal_entity_client_create_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@legal_entity_client_routes_bp.route("/legal_entity_client", methods=["GET"])
@swag_from(
    {
        "tags": ["Legal Entity Client"],
        "description": "List all legal entity clients",
        "responses": {
            "200": {
                "description": "A list of clients",
            },
            "404": {"description": "No clients found"},
        },
    }
)
def list_legal_entity_clients():
    try:
        http_request = HttpRequest()
        view = legal_entity_client_list_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@legal_entity_client_routes_bp.route("/legal_entity_client/<int:client_id>", methods=["GET"])
@swag_from(
    {
        "tags": ["Legal Entity Client"],
        "description": "Find legal entity client by ID",
        "parameters": [
            {
                "name": "client_id",
                "in": "path",
                "required": True,
                "type": "integer",
                "description": "The ID of the client",
            }
        ],
        "responses": {
            "200": {"description": "Client details"},
            "404": {"description": "Client not found"},
        },
    }
)
def find_legal_entity_client(client_id):
    try:
        http_request = HttpRequest(param={"client_id": client_id})
        view = legal_entity_client_find_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@legal_entity_client_routes_bp.route("/legal_entity_client/withdraw", methods=["POST"])
@swag_from(
    {
        "tags": ["Legal Entity Client"],
        "description": "Withdraw money from legal entity client account",
        "parameters": [
            {
                "name": "body",
                "in": "body",
                "required": True,
                "schema": {
                    "type": "object",
                    "properties": {"client_id": {"type": "integer"}, "amount": {"type": "number"}},
                    "required": ["client_id", "amount"],
                },
            }
        ],
        "responses": {
            "200": {"description": "Withdrawal successful"},
            "400": {"description": "Invalid request or insufficient funds"},
        },
    }
)
def withdraw_legal_entity_client():
    try:
        http_request = HttpRequest(body=request.json)
        view = legal_entity_client_withdraw_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
