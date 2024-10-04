from src.controllers.interfaces.legal_entity_client_create_controller import (
    LegalEntityClientCreateControllerInterface,
)
from src.validators.legal_entity_client_validator import legal_entity_client_validator
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class LegalEntityClientCreateView(ViewInterface):
    def __init__(self, controller: LegalEntityClientCreateControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        legal_entity_client_validator(http_request)

        client_info = http_request.body

        self.__controller.create(client_info)

        return HttpResponse(
            status_code=201, body={"message": "Legal entity client created successfully."}
        )
