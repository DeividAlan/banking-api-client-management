from .individual_client_check_balance_controller import IndividualClientCheckBalanceController


class MockClientRepository:
    def __init__(self, balance_data: dict):
        self.balance_data = balance_data

    def check_balance(self, client_id: int) -> float:
        return self.balance_data.get(client_id, 0.0)


def test_check_balance_existing_client():
    mock_balances = {
        1: 1500.0,
        2: 2500.0,
        3: 3500.0,
    }

    controller = IndividualClientCheckBalanceController(MockClientRepository(mock_balances))

    balance = controller.check_balance(1)
    assert balance == 1500.0

    balance = controller.check_balance(2)
    assert balance == 2500.0

    balance = controller.check_balance(3)
    assert balance == 3500.0


def test_check_balance_non_existing_client():
    mock_balances = {
        1: 1500.0,
    }

    controller = IndividualClientCheckBalanceController(MockClientRepository(mock_balances))

    balance = controller.check_balance(999)
    assert balance == 0.0
