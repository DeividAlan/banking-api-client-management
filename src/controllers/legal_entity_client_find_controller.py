from typing import Dict, Optional
from src.errors.errors_types.http_not_found import HttpNotFoundError
from src.models.sqlite.interface.client import ClientInterface
from src.models.sqlite.repositories.legal_entity_client_repository import (
    LegalEntityClientRepository,
)
from .interfaces.legal_entity_client_find_controller import (
    LegalEntityClientFindControllerInterface,
)


class LegalEntityClientFindController(LegalEntityClientFindControllerInterface):
    def __init__(self, client_repository: ClientInterface) -> None:
        self.__client_repository = client_repository

    def find_by_id(self, client_id: int) -> Optional[Dict]:
        client = self.__client_repository.find_legal_entity_client(client_id)
        if not client:
            raise HttpNotFoundError("Client not found.")
        return self.__format_response(client)

    def __format_response(self, client: LegalEntityClientRepository) -> Dict:
        return {
            "id": client.id,
            "business_name": client.business_name,
            "revenue": client.revenue,
            "corporate_email": client.corporate_email,
            "phone": client.phone,
            "category": client.category,
            "balance": client.balance,
        }
