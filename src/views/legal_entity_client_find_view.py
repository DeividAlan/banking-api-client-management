from src.controllers.interfaces.legal_entity_client_find_controller import (
    LegalEntityClientFindControllerInterface,
)
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.errors.errors_types.http_not_found import HttpNotFoundError
from .interfaces.view_interface import ViewInterface


class LegalEntityClientFindView(ViewInterface):
    def __init__(self, controller: LegalEntityClientFindControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        client_id = http_request.params.get("client_id")

        if client_id is None:
            return HttpResponse(status_code=400, body={"message": "Client ID is required."})

        try:
            client_data = self.__controller.find_by_id(int(client_id))
            return HttpResponse(status_code=200, body=client_data)
        except ValueError:
            return HttpResponse(status_code=400, body={"message": "Client ID must be an integer."})
        except HttpNotFoundError as e:
            return HttpResponse(status_code=404, body={"message": str(e)})
