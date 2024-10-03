import pytest
from src.errors.errors_types.http_bad_request import HttpBadRequestError
from .individual_client_create_controller import IndividualClientCreateController


class MockClientRepository:
    def insert_individual_client(
        self,
        full_name: str,
        monthly_income: float,
        age: int,
        phone: str,
        category: str,
        balance: float,
    ) -> None:
        pass


def test_create_individual_client():
    client_info = {
        "full_name": "Jane Doe",
        "monthly_income": 5000.0,
        "age": 28,
        "phone": "+1234567890",
        "category": "Regular",
        "balance": 1000.0,
    }

    controller = IndividualClientCreateController(MockClientRepository())
    response = controller.create(client_info)

    # No response expected since the method returns None on successful creation
    assert response is None


def test_create_individual_client_error_empty_full_name():
    client_info = {
        "full_name": "",
        "monthly_income": 5000.0,
        "age": 28,
        "phone": "+1234567890",
        "category": "Regular",
        "balance": 1000.0,
    }

    controller = IndividualClientCreateController(MockClientRepository())

    with pytest.raises(HttpBadRequestError, match="Full name cannot be empty."):
        controller.create(client_info)


def test_create_individual_client_error_invalid_phone():
    client_info = {
        "full_name": "Jane Doe",
        "monthly_income": 5000.0,
        "age": 28,
        "phone": "123456",
        "category": "Regular",
        "balance": 1000.0,
    }

    controller = IndividualClientCreateController(MockClientRepository())

    with pytest.raises(HttpBadRequestError, match="Phone number is invalid."):
        controller.create(client_info)


def test_create_individual_client_error_invalid_full_name():
    client_info = {
        "full_name": "Jane123",
        "monthly_income": 5000.0,
        "age": 28,
        "phone": "+1234567890",
        "category": "Regular",
        "balance": 1000.0,
    }

    controller = IndividualClientCreateController(MockClientRepository())

    with pytest.raises(HttpBadRequestError, match="Full name contains invalid characters."):
        controller.create(client_info)
