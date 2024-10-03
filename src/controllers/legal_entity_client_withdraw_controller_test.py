from src.controllers.legal_entity_client_withdraw_controller import (
    LegalEntityClientWithdrawController,
)
from src.errors.errors_types.http_invalid_balance import HttpInvalidBalanceError
from src.errors.errors_types.http_not_found import HttpNotFoundError
from src.models.sqlite.entities.legal_entity_client import LegalEntityClientTable


class MockClientRepository:
    def __init__(self, clients):
        self.clients = clients

    def withdraw_money(self, client_id: int, amount: float) -> None:
        client = self.find_client(client_id)
        if not client:
            raise HttpNotFoundError("Client not found.")
        if client.balance < amount:
            raise HttpInvalidBalanceError("Insufficient balance to complete the withdrawal.")
        client.balance -= amount

    def find_client(self, client_id: int) -> LegalEntityClientTable:
        for client in self.clients:
            if client.id == client_id:
                return client
        return None


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


def test_withdraw_success():
    controller = LegalEntityClientWithdrawController(MockClientRepository(mock_clients))

    controller.withdraw(client_id=1, amount=200.0)

    assert mock_clients[0].balance == 300.0


def test_withdraw_insufficient_balance():
    controller = LegalEntityClientWithdrawController(MockClientRepository(mock_clients))

    try:
        controller.withdraw(client_id=2, amount=2000.0)
    except HttpInvalidBalanceError as e:
        assert str(e) == "Insufficient balance to complete the withdrawal."


def test_withdraw_client_not_found():
    controller = LegalEntityClientWithdrawController(MockClientRepository(mock_clients))

    try:
        controller.withdraw(client_id=99, amount=100.0)
    except HttpNotFoundError as e:
        assert str(e) == "Client not found."
