from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.individual_client import IndividualClientTable
from src.models.sqlite.repositories.individual_client_repository import IndividualClientRepository
from src.errors.errors_types.http_invalid_balance import HttpInvalidBalanceError
from src.errors.errors_types.http_not_found import HttpNotFoundError


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(IndividualClientTable)],
                    [
                        IndividualClientTable(
                            id=1,
                            full_name="John Doe",
                            monthly_income=3000.00,
                            age=30,
                            phone="555-1234",
                            category="A",
                            balance=1000.00,
                        ),
                        IndividualClientTable(
                            id=2,
                            full_name="Jane Doe",
                            monthly_income=4000.00,
                            age=25,
                            phone="555-5678",
                            category="B",
                            balance=2000.00,
                        ),
                    ],
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class MockConnectionNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def test_insert_individual_client():
    mock_connection = MockConnection()
    repo = IndividualClientRepository(mock_connection)

    repo.insert_individual_client(
        full_name="John Doe",
        monthly_income=3000.00,
        age=30,
        phone="555-1234",
        category="A",
        balance=1000.00,
    )

    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()


def test_list_individual_clients():
    mock_connection = MockConnection()
    repo = IndividualClientRepository(mock_connection)

    response = repo.list_individual_clients()

    mock_connection.session.query.assert_called_once_with(IndividualClientTable)
    mock_connection.session.all.assert_called_once()
    assert len(response) == 2
    assert response[0].full_name == "John Doe"


def test_find_individual_client():
    mock_connection = MockConnection()
    repo = IndividualClientRepository(mock_connection)

    response = repo.find_individual_client(1)

    mock_connection.session.query.assert_called_once_with(IndividualClientTable)
    assert response.full_name == "John Doe"


def test_check_balance():
    mock_connection = MockConnection()
    repo = IndividualClientRepository(mock_connection)

    balance = repo.check_balance(1)

    mock_connection.session.query.assert_called_once_with(IndividualClientTable)
    assert balance == 1000.00


def test_withdraw_money():
    mock_connection = MockConnection()
    repo = IndividualClientRepository(mock_connection)

    repo.withdraw_money(client_id=1, amount=500.00)

    mock_connection.session.query.assert_called_once_with(IndividualClientTable)
    mock_connection.session.commit.assert_called_once()

    new_balance = mock_connection.session.query(IndividualClientTable).get(1).balance
    assert new_balance == 500.00


def test_withdraw_money_insufficient_balance():
    mock_connection = MockConnection()
    repo = IndividualClientRepository(mock_connection)

    with pytest.raises(HttpInvalidBalanceError):
        repo.withdraw_money(client_id=1, amount=2000.00)

    mock_connection.session.rollback.assert_called_once()


def test_withdraw_money_user_not_found():
    mock_connection_no_result = MockConnectionNoResult()
    repo = IndividualClientRepository(mock_connection_no_result)

    with pytest.raises(HttpNotFoundError):
        repo.withdraw_money(client_id=1, amount=2000.00)

    mock_connection_no_result.session.rollback.assert_called_once()
