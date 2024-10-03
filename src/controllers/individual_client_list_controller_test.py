from typing import List
from src.models.sqlite.entities.individual_client import IndividualClientTable
from .individual_client_list_controller import IndividualClientListController


class MockClientRepository:
    def __init__(self, clients: List[IndividualClientTable]):
        self.clients = clients

    def list_individual_clients(self) -> List[IndividualClientTable]:
        return self.clients


mock_clients = [
    IndividualClientTable(
        id=1,
        full_name="John Doe",
        age=30,
        monthly_income=3000.0,
        phone="+123456789",
        category="A",
        balance=1500.0,
    ),
    IndividualClientTable(
        id=2,
        full_name="Jane Smith",
        age=25,
        monthly_income=4000.0,
        phone="+987654321",
        category="B",
        balance=2500.0,
    ),
]


def test_list_clients():
    controller = IndividualClientListController(MockClientRepository(mock_clients))

    response = controller.list()

    assert len(response) == 2
    assert response[0]["id"] == 1
    assert response[0]["full_name"] == "John Doe"
    assert response[0]["age"] == 30
    assert response[0]["monthly_income"] == 3000.0
    assert response[0]["phone"] == "+123456789"
    assert response[0]["category"] == "A"
    assert response[0]["balance"] == 1500.0

    assert response[1]["id"] == 2
    assert response[1]["full_name"] == "Jane Smith"
    assert response[1]["age"] == 25
    assert response[1]["monthly_income"] == 4000.0
    assert response[1]["phone"] == "+987654321"
    assert response[1]["category"] == "B"
    assert response[1]["balance"] == 2500.0


def test_list_clients_empty():
    controller = IndividualClientListController(MockClientRepository([]))

    response = controller.list()

    assert len(response) == 0
