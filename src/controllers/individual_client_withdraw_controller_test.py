import pytest
from src.errors.errors_types.http_invalid_balance import HttpInvalidBalanceError
from src.errors.errors_types.http_not_found import HttpNotFoundError
from src.models.sqlite.entities.individual_client import IndividualClientTable
from .individual_client_withdraw_controller import IndividualClientWithdrawController


class MockClientRepository:
    def __init__(self, clients: dict):
        self.clients = clients

    def withdraw_money(self, client_id: int, amount: float) -> None:
        if client_id not in self.clients:
            raise HttpNotFoundError("Client not found.")

        client = self.clients[client_id]

        if client.balance < amount:
            raise HttpInvalidBalanceError("Insufficient balance to complete the withdrawal.")

        client.balance -= amount


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


def test_withdraw_success():
    controller = IndividualClientWithdrawController(MockClientRepository(mock_clients))

    controller.withdraw(client_id=1, amount=500.0)

    assert mock_clients[1].balance == 1000.0


def test_withdraw_insufficient_balance():
    controller = IndividualClientWithdrawController(MockClientRepository(mock_clients))

    with pytest.raises(HttpInvalidBalanceError):
        controller.withdraw(client_id=1, amount=2000.0)


def test_withdraw_client_not_found():
    controller = IndividualClientWithdrawController(MockClientRepository(mock_clients))

    with pytest.raises(HttpNotFoundError):
        controller.withdraw(client_id=999, amount=500.0)
