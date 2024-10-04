from flask import Blueprint, jsonify, request
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
def create_individual_client():
    try:
        http_request = HttpRequest(body=request.json)
        view = individual_client_create_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@individual_client_routes_bp.route("/individual_client", methods=["GET"])
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
def withdraw_individual_client():
    try:
        http_request = HttpRequest(body=request.json)
        view = individual_client_withdraw_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
