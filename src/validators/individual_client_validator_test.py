from src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .individual_client_validator import (
    individual_client_validator,
)


class MockRequest:
    def __init__(self, body) -> None:
        self.body = body


def test_individual_client_validator():
    request = MockRequest(
        {
            "full_name": "John Doe",
            "monthly_income": 3000.0,
            "age": 30,
            "phone": "1234567890",
            "category": "Standard",
            "balance": 150.0,
        }
    )

    individual_client_validator(request)


def test_individual_client_validator_invalid_full_name():
    request = MockRequest(
        {
            "full_name": "",  # Nome vazio
            "monthly_income": 3000.0,
            "age": 30,
            "phone": "1234567890",
            "category": "Standard",
            "balance": 150.0,
        }
    )

    try:
        individual_client_validator(request)
    except Exception as e:
        assert isinstance(e, HttpUnprocessableEntityError)


def test_individual_client_validator_negative_monthly_income():
    request = MockRequest(
        {
            "full_name": "John Doe",
            "monthly_income": -300.0,  # Renda negativa
            "age": 30,
            "phone": "1234567890",
            "category": "Standard",
            "balance": 150.0,
        }
    )

    try:
        individual_client_validator(request)
    except Exception as e:
        assert isinstance(e, HttpUnprocessableEntityError)


def test_individual_client_validator_negative_age():
    request = MockRequest(
        {
            "full_name": "John Doe",
            "monthly_income": 3000.0,
            "age": -1,
            "phone": "1234567890",
            "category": "Standard",
            "balance": 150.0,
        }
    )

    try:
        individual_client_validator(request)
    except Exception as e:
        assert isinstance(e, HttpUnprocessableEntityError)


def test_individual_client_validator_empty_phone():
    request = MockRequest(
        {
            "full_name": "John Doe",
            "monthly_income": 3000.0,
            "age": 30,
            "phone": "",
            "category": "Standard",
            "balance": 150.0,
        }
    )

    try:
        individual_client_validator(request)
    except Exception as e:
        assert isinstance(e, HttpUnprocessableEntityError)


def test_individual_client_validator_negative_balance():
    request = MockRequest(
        {
            "full_name": "John Doe",
            "monthly_income": 3000.0,
            "age": 30,
            "phone": "1234567890",
            "category": "Standard",
            "balance": -100.0,
        }
    )

    try:
        individual_client_validator(request)
    except Exception as e:
        assert isinstance(e, HttpUnprocessableEntityError)
