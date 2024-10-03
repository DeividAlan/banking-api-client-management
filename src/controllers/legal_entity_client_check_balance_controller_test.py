import pytest
from src.errors.errors_types.http_not_found import HttpNotFoundError
from .legal_entity_client_check_balance_controller import LegalEntityClientCheckBalanceController


class MockClientRepository:
    def __init__(self, clients):
        self.clients = clients

    def check_balance(self, client_id: int) -> float:
        client = self.clients.get(client_id)
        if client is None:
            raise HttpNotFoundError("Client not found.")
        return client["balance"]


mock_clients = {
    1: {"balance": 1000.0},
    2: {"balance": 500.0},
}


def test_check_balance_existing_client():
    controller = LegalEntityClientCheckBalanceController(MockClientRepository(mock_clients))
    balance = controller.check_balance(1)
    assert balance == 1000.0


def test_check_balance_non_existing_client():
    controller = LegalEntityClientCheckBalanceController(MockClientRepository(mock_clients))

    with pytest.raises(HttpNotFoundError, match="Client not found."):
        controller.check_balance(999)
