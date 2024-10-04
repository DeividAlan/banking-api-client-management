from src.controllers.interfaces.individual_client_create_controller import (
    IndividualClientCreateControllerInterface,
)
from src.validators.individual_client_validator import individual_client_validator
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class IndividualClientCreatorView(ViewInterface):
    def __init__(self, controller: IndividualClientCreateControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        individual_client_validator(http_request)
        client_info = http_request.body
        self.__controller.create(client_info)

        return HttpResponse(
            status_code=201, body={"message": "Individual client created successfully."}
        )
