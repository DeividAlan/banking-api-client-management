from flask import Blueprint, jsonify, request
from flasgger import swag_from
from src.views.http_types.http_request import HttpRequest
from src.main.composer.individual_client_create_composer import individual_client_create_composer
from src.main.composer.individual_client_list_composer import individual_client_list_composer
from src.main.composer.individual_client_find_composer import individual_client_find_composer
from src.main.composer.individual_client_withdraw_composer import (
    individual_client_withdraw_composer,
)
from src.errors.error_handler import handle_errors

individual_client_routes_bp = Blueprint("individual_client_routes", __name__)


@individual_client_routes_bp.route("/individual_client", methods=["POST"])
@swag_from(
    {
        "tags": ["Individual Client"],
        "description": "Create a new individual client",
        "parameters": [
            {
                "name": "body",
                "in": "body",
                "required": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "full_name": {"type": "string"},
                        "monthly_income": {"type": "number"},
                        "age": {"type": "integer"},
                        "phone": {"type": "string"},
                        "category": {"type": "string"},
                        "balance": {"type": "number"},
                    },
                    "required": [
                        "full_name",
                        "monthly_income",
                        "age",
                        "phone",
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
def create_individual_client():
    try:
        body = request.json
        http_request = HttpRequest(body=body)
        view = individual_client_create_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@individual_client_routes_bp.route("/individual_client", methods=["GET"])
@swag_from(
    {
        "tags": ["Individual Client"],
        "description": "List all individual clients",
        "responses": {
            "200": {
                "description": "A list of clients",
            },
            "404": {"description": "No clients found"},
        },
    }
)
def list_individual_clients():
    try:
        http_request = HttpRequest()
        view = individual_client_list_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@individual_client_routes_bp.route("/individual_client/<int:client_id>", methods=["GET"])
@swag_from(
    {
        "tags": ["Individual Client"],
        "description": "Find individual client by ID",
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
def find_individual_client(client_id):
    try:
        http_request = HttpRequest(param={"client_id": client_id})
        view = individual_client_find_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@individual_client_routes_bp.route("/individual_client/withdraw", methods=["POST"])
@swag_from(
    {
        "tags": ["Individual Client"],
        "description": "Withdraw money from individual client account",
        "parameters": [
            {
                "name": "body",
                "in": "body",
                "required": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "amount": {"type": "number"},
                    },
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
def withdraw_individual_client():
    try:
        body = request.json
        http_request = HttpRequest(body=body)

        view = individual_client_withdraw_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
