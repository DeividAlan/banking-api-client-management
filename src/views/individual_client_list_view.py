from src.controllers.interfaces.individual_client_list_controller import (
    IndividualClientListControllerInterface,
)
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class IndividualClientListView(ViewInterface):
    def __init__(self, controller: IndividualClientListControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        clients_data = self.__controller.list()

        return HttpResponse(status_code=200, body=clients_data)
