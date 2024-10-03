from typing import Dict, List
from src.models.sqlite.interface.client import ClientInterface
from src.models.sqlite.entities.legal_entity_client import LegalEntityClientTable
from .interfaces.legal_entity_client_list_controller import LegalEntityClientListControllerInterface


class LegalEntityClientListController(LegalEntityClientListControllerInterface):
    def __init__(self, client_repository: ClientInterface) -> None:
        self.__client_repository = client_repository

    def list(self) -> List[Dict]:
        clients = self.__client_repository.list_legal_entity_clients()
        return [self.__format_response(client) for client in clients]

    def __format_response(self, client: LegalEntityClientTable) -> Dict:
        return {
            "id": client.id,
            "business_name": client.business_name,
            "revenue": client.revenue,
            "corporate_email": client.corporate_email,
            "phone": client.phone,
            "category": client.category,
            "balance": client.balance,
        }
