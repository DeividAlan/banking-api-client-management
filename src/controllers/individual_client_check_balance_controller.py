from src.models.sqlite.interface.client import ClientInterface
from .interfaces.individual_client_check_balance_controller import (
    IndividualClientCheckBalanceControllerInterface,
)


class IndividualClientCheckBalanceController(IndividualClientCheckBalanceControllerInterface):
    def __init__(self, client_repository: ClientInterface) -> None:
        self.__client_repository = client_repository

    def check_balance(self, client_id: int) -> float:
        balance = self.__client_repository.check_balance(client_id)
        return balance
