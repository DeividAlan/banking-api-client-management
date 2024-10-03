from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.legal_entity_client import LegalEntityClientTable
from src.models.sqlite.repositories.legal_entity_client_repository import (
    LegalEntityClientRepository,
)
from src.errors.errors_types.http_invalid_balance import HttpInvalidBalanceError
from src.errors.errors_types.http_not_found import HttpNotFoundError


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(LegalEntityClientTable)],
                    [
                        LegalEntityClientTable(
                            id=1,
                            business_name="ABC Corp",
                            revenue=500000.00,
                            corporate_email="contact@abc.com",
                            phone="555-9876",
                            category="Enterprise",
                            balance=10000.00,
                        ),
                        LegalEntityClientTable(
                            id=2,
                            business_name="XYZ Ltd",
                            revenue=750000.00,
                            corporate_email="info@xyz.com",
                            phone="555-1234",
                            category="Small Business",
                            balance=20000.00,
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


def test_insert_legal_entity_client():
    mock_connection = MockConnection()
    repo = LegalEntityClientRepository(mock_connection)

    repo.insert_legal_entity_client(
        business_name="ABC Corp",
        revenue=500000.00,
        corporate_email="contact@abc.com",
        phone="555-9876",
        category="Enterprise",
        balance=10000.00,
    )

    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()


def test_list_legal_entity_clients():
    mock_connection = MockConnection()
    repo = LegalEntityClientRepository(mock_connection)

    response = repo.list_legal_entity_clients()

    mock_connection.session.query.assert_called_once_with(LegalEntityClientTable)
    mock_connection.session.all.assert_called_once()
    assert len(response) == 2
    assert response[0].business_name == "ABC Corp"


def test_find_legal_entity_client():
    mock_connection = MockConnection()
    repo = LegalEntityClientRepository(mock_connection)

    response = repo.find_legal_entity_client(1)

    mock_connection.session.query.assert_called_once_with(LegalEntityClientTable)
    assert response.business_name == "ABC Corp"


def test_check_balance():
    mock_connection = MockConnection()
    repo = LegalEntityClientRepository(mock_connection)

    balance = repo.check_balance(1)

    mock_connection.session.query.assert_called_once_with(LegalEntityClientTable)
    assert balance == 10000.00


def test_withdraw_money():
    mock_connection = MockConnection()
    repo = LegalEntityClientRepository(mock_connection)

    repo.withdraw_money(client_id=1, amount=5000.00)

    mock_connection.session.query.assert_called_once_with(LegalEntityClientTable)
    mock_connection.session.commit.assert_called_once()

    new_balance = mock_connection.session.query(LegalEntityClientTable).get(1).balance
    assert new_balance == 5000.00


def test_withdraw_money_insufficient_balance():
    mock_connection = MockConnection()
    repo = LegalEntityClientRepository(mock_connection)

    with pytest.raises(HttpInvalidBalanceError):
        repo.withdraw_money(client_id=1, amount=15000.00)

    mock_connection.session.rollback.assert_called_once()


def test_withdraw_money_user_not_found():
    mock_connection_no_result = MockConnectionNoResult()
    repo = LegalEntityClientRepository(mock_connection_no_result)

    with pytest.raises(HttpNotFoundError):
        repo.withdraw_money(client_id=1, amount=5000.00)

    mock_connection_no_result.session.rollback.assert_called_once()
