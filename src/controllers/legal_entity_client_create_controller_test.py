import pytest
from src.errors.errors_types.http_bad_request import HttpBadRequestError
from src.models.sqlite.entities.legal_entity_client import LegalEntityClientTable
from .legal_entity_client_create_controller import LegalEntityClientCreateController


class MockClientRepository:
    def __init__(self):
        self.data = []

    def insert_legal_entity_client(
        self, business_name, revenue, corporate_email, phone, category, balance
    ):
        new_client = LegalEntityClientTable(
            business_name=business_name,
            revenue=revenue,
            corporate_email=corporate_email,
            phone=phone,
            category=category,
            balance=balance,
        )
        self.data.append(new_client)


def test_create_valid_client():
    mock_repo = MockClientRepository()
    controller = LegalEntityClientCreateController(mock_repo)

    client_info = {
        "business_name": "Valid Business",
        "revenue": 500000.0,
        "corporate_email": "business@company.com",
        "phone": "+1234567890",
        "category": "A",
        "balance": 1000.0,
    }

    controller.create(client_info)

    assert len(mock_repo.data) == 1
    client = mock_repo.data[0]
    assert client.business_name == "Valid Business"
    assert client.revenue == 500000.0
    assert client.corporate_email == "business@company.com"
    assert client.phone == "+1234567890"
    assert client.category == "A"
    assert client.balance == 1000.0


def test_create_invalid_business_name():
    mock_repo = MockClientRepository()
    controller = LegalEntityClientCreateController(mock_repo)

    client_info = {
        "business_name": "",
        "revenue": 500000.0,
        "corporate_email": "business@company.com",
        "phone": "+1234567890",
        "category": "A",
        "balance": 1000.0,
    }

    with pytest.raises(HttpBadRequestError, match="Business name cannot be empty."):
        controller.create(client_info)


def test_create_invalid_revenue():
    mock_repo = MockClientRepository()
    controller = LegalEntityClientCreateController(mock_repo)

    client_info = {
        "business_name": "Valid Business",
        "revenue": -500.0,
        "corporate_email": "business@company.com",
        "phone": "+1234567890",
        "category": "A",
        "balance": 1000.0,
    }

    with pytest.raises(HttpBadRequestError, match="Revenue cannot be negative."):
        controller.create(client_info)


def test_create_invalid_corporate_email():
    mock_repo = MockClientRepository()
    controller = LegalEntityClientCreateController(mock_repo)

    client_info = {
        "business_name": "Valid Business",
        "revenue": 500000.0,
        "corporate_email": "invalid-email",
        "phone": "+1234567890",
        "category": "A",
        "balance": 1000.0,
    }

    with pytest.raises(HttpBadRequestError, match="Corporate email is invalid."):
        controller.create(client_info)


def test_create_invalid_phone():
    mock_repo = MockClientRepository()
    controller = LegalEntityClientCreateController(mock_repo)

    client_info = {
        "business_name": "Valid Business",
        "revenue": 500000.0,
        "corporate_email": "business@company.com",
        "phone": "123",
        "category": "A",
        "balance": 1000.0,
    }

    with pytest.raises(HttpBadRequestError, match="Phone number is invalid."):
        controller.create(client_info)
