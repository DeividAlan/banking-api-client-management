from src.controllers.interfaces.legal_entity_client_check_balance_controller import (
    LegalEntityClientCheckBalanceControllerInterface,
)
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.errors.errors_types.http_not_found import HttpNotFoundError
from .interfaces.view_interface import ViewInterface


class LegalEntityClientCheckBalanceView(ViewInterface):
    def __init__(self, controller: LegalEntityClientCheckBalanceControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        client_id = http_request.body.get("client_id")

        if not isinstance(client_id, int) or client_id <= 0:
            raise HttpNotFoundError("Client ID must be a positive integer.")

        balance = self.__controller.check_balance(client_id)

        return HttpResponse(
            status_code=200,
            body={"client_id": client_id, "balance": balance},
        )
