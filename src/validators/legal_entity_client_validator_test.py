from src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .legal_entity_client_validator import legal_entity_client_validator


class MockRequest:
    def __init__(self, body) -> None:
        self.body = body


def test_legal_entity_client_validator():
    request = MockRequest(
        {
            "business_name": "Acme Corp",
            "revenue": 50000.0,
            "corporate_email": "contact@acme.com",
            "phone": "+123456789",
            "category": "Retail",
            "balance": 1000.0,
        }
    )

    legal_entity_client_validator(request)


def test_legal_entity_client_validator_invalid_email():
    request = MockRequest(
        {
            "business_name": "Acme Corp",
            "revenue": 50000.0,
            "corporate_email": "invalid-email",
            "phone": "+123456789",
            "category": "Retail",
            "balance": 1000.0,
        }
    )

    try:
        legal_entity_client_validator(request)
    except Exception as e:
        assert isinstance(e, HttpUnprocessableEntityError)


def test_legal_entity_client_validator_negative_revenue():
    request = MockRequest(
        {
            "business_name": "Acme Corp",
            "revenue": -50000.0,
            "corporate_email": "contact@acme.com",
            "phone": "+123456789",
            "category": "Retail",
            "balance": 1000.0,
        }
    )

    try:
        legal_entity_client_validator(request)
    except Exception as e:
        assert isinstance(e, HttpUnprocessableEntityError)
