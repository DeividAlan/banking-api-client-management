from pydantic import BaseModel, condecimal, ValidationError
from src.controllers.interfaces.legal_entity_client_withdraw_controller import (
    LegalEntityClientWithdrawControllerInterface,
)
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .interfaces.view_interface import ViewInterface


class LegalEntityClientWithdrawView(ViewInterface):
    def __init__(self, controller: LegalEntityClientWithdrawControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        self.withdrawal_validator(http_request)

        client_id = http_request.body["client_id"]
        amount = http_request.body["amount"]

        self.__controller.withdraw(client_id, amount)

        return HttpResponse(
            status_code=200,
            body={"message": "Withdrawal successful."},
        )

    def withdrawal_validator(self, http_request: HttpRequest) -> None:
        class WithdrawalData(BaseModel):
            client_id: int
            amount: condecimal(gt=0)

        try:
            WithdrawalData(**http_request.body)
        except ValidationError as e:
            raise HttpUnprocessableEntityError(e.errors()) from e
