from typing import Dict, Optional
from src.errors.errors_types.http_not_found import HttpNotFoundError
from src.models.sqlite.interface.client import ClientInterface
from src.models.sqlite.repositories.individual_client_repository import IndividualClientRepository
from .interfaces.individual_client_find_controller import (
    IndividualClientFindControllerInterface,
)


class IndividualClientFindController(IndividualClientFindControllerInterface):
    def __init__(self, client_repository: ClientInterface) -> None:
        self.__client_repository = client_repository

    def find_by_id(self, client_id: int) -> Optional[Dict]:
        client = self.__client_repository.find_individual_client(client_id)
        if not client:
            raise HttpNotFoundError("Client not found.")
        return self.__format_response(client)

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
