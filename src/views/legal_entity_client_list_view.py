from src.controllers.interfaces.legal_entity_client_list_controller import (
    LegalEntityClientListControllerInterface,
)
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class LegalEntityClientListView(ViewInterface):
    def __init__(self, controller: LegalEntityClientListControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            clients_data = self.__controller.list()
            return HttpResponse(status_code=200, body=clients_data)
        except Exception as e:
            return HttpResponse(
                status_code=500,
                body={"message": "An error occurred while retrieving clients.", "error": str(e)},
            )
