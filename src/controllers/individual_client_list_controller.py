from typing import Dict, List
from src.models.sqlite.interface.client import ClientInterface
from src.models.sqlite.repositories.individual_client_repository import IndividualClientRepository
from .interfaces.individual_client_list_controller import (
    IndividualClientListControllerInterface,
)


class IndividualClientListController(IndividualClientListControllerInterface):
    def __init__(self, client_repository: ClientInterface) -> None:
        self.__client_repository = client_repository

    def list(self) -> List[Dict]:
        clients = self.__client_repository.list_individual_clients()
        return [self.__format_response(client) for client in clients]

    def __format_response(self, client: IndividualClientRepository) -> Dict:
        return {
            "id": client.id,
            "full_name": client.full_name,
            "age": client.age,
            "monthly_income": client.monthly_income,
            "phone": client.phone,
            "category": client.category,
            "balance": client.balance,
        }
