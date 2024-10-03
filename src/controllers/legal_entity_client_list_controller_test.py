from typing import List
from src.models.sqlite.entities.legal_entity_client import LegalEntityClientTable
from src.controllers.legal_entity_client_list_controller import LegalEntityClientListController


class MockClientRepository:
    def __init__(self, clients: List[LegalEntityClientTable]):
        self.clients = clients

    def list_legal_entity_clients(self) -> List[LegalEntityClientTable]:
        return self.clients


mock_clients = [
    LegalEntityClientTable(
        id=1,
        business_name="Client A",
        revenue=1000.0,
        corporate_email="clienta@example.com",
        phone="123456789",
        category="Category 1",
        balance=500.0,
    ),
    LegalEntityClientTable(
        id=2,
        business_name="Client B",
        revenue=2000.0,
        corporate_email="clientb@example.com",
        phone="987654321",
        category="Category 2",
        balance=1500.0,
    ),
]


def test_list_clients():
    controller = LegalEntityClientListController(MockClientRepository(mock_clients))

    response = controller.list()

    assert len(response) == 2
    assert response[0]["id"] == 1
    assert response[0]["business_name"] == "Client A"
    assert response[0]["phone"] == "123456789"
    assert response[0]["category"] == "Category 1"
    assert response[0]["balance"] == 500.0

    assert response[1]["id"] == 2
    assert response[1]["business_name"] == "Client B"
    assert response[1]["phone"] == "987654321"
    assert response[1]["category"] == "Category 2"
    assert response[1]["balance"] == 1500.0


def test_list_clients_empty():
    controller = LegalEntityClientListController(MockClientRepository([]))

    response = controller.list()

    assert len(response) == 0
