from src.controllers.interfaces.individual_client_check_balance_controller import (
    IndividualClientCheckBalanceControllerInterface,
)
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.errors.errors_types.http_not_found import HttpNotFoundError
from .interfaces.view_interface import ViewInterface


class IndividualClientCheckBalanceView(ViewInterface):
    def __init__(self, controller: IndividualClientCheckBalanceControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        client_id = http_request.path_params.get("client_id")

        if client_id is None or not client_id.isdigit():
            return HttpResponse(status_code=400, body={"message": "Invalid client ID."})

        client_id = int(client_id)

        try:
            balance = self.__controller.check_balance(client_id)
            return HttpResponse(status_code=200, body={"balance": balance})
        except HttpNotFoundError as e:
            return HttpResponse(status_code=404, body={"message": str(e)})
