from typing import Optional
import pytest
from src.errors.errors_types.http_not_found import HttpNotFoundError
from src.models.sqlite.entities.individual_client import IndividualClientTable
from .individual_client_find_controller import IndividualClientFindController


class MockClientRepository:
    def __init__(self, client_data: dict):
        self.client_data = client_data

    def find_individual_client(self, client_id: int) -> Optional[IndividualClientTable]:
        return self.client_data.get(client_id)

    def withdraw_money(self, client_id: int, amount: float) -> None:
        pass

    def check_balance(self, client_id: int) -> float:
        pass


mock_clients = {
    1: IndividualClientTable(
        id=1,
        full_name="John Doe",
        age=30,
        monthly_income=3000.0,
        phone="+123456789",
        category="A",
        balance=1500.0,
    ),
    2: IndividualClientTable(
        id=2,
        full_name="Jane Smith",
        age=25,
        monthly_income=4000.0,
        phone="+987654321",
        category="B",
        balance=2500.0,
    ),
}


def test_find_client_existing():
    controller = IndividualClientFindController(MockClientRepository(mock_clients))

    response = controller.find_by_id(1)

    assert response["id"] == 1
    assert response["full_name"] == "John Doe"
    assert response["age"] == 30
    assert response["monthly_income"] == 3000.0
    assert response["phone"] == "+123456789"
    assert response["category"] == "A"
    assert response["balance"] == 1500.0


def test_find_client_non_existing():
    controller = IndividualClientFindController(MockClientRepository(mock_clients))

    with pytest.raises(HttpNotFoundError):
        controller.find_by_id(999)
