from src.models.sqlite.interface.client import ClientInterface
from .interfaces.legal_entity_client_withdraw_controller import (
    LegalEntityClientWithdrawControllerInterface,
)


class LegalEntityClientWithdrawController(LegalEntityClientWithdrawControllerInterface):
    def __init__(self, client_repository: ClientInterface) -> None:
        self.__client_repository = client_repository

    def withdraw(self, client_id: int, amount: float) -> None:
        self.__client_repository.withdraw_money(client_id, amount)
