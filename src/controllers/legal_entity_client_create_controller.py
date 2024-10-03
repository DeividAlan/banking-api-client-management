from typing import Dict
import re
from src.errors.errors_types.http_bad_request import HttpBadRequestError
from src.models.sqlite.interface.client import ClientInterface
from .interfaces.legal_entity_client_create_controller import (
    LegalEntityClientCreateControllerInterface,
)


class LegalEntityClientCreateController(LegalEntityClientCreateControllerInterface):
    def __init__(self, client_repository: ClientInterface) -> None:
        self.__client_repository = client_repository

    def create(self, client_info: Dict) -> None:
        business_name = client_info["business_name"]
        revenue = client_info["revenue"]
        corporate_email = client_info["corporate_email"]
        phone = client_info["phone"]
        category = client_info["category"]
        balance = client_info["balance"]

        self.__validate_business_name(business_name)
        self.__validate_revenue(revenue)
        self.__validate_corporate_email(corporate_email)
        self.__validate_phone(phone)

        self.__client_repository.insert_legal_entity_client(
            business_name=business_name,
            revenue=revenue,
            corporate_email=corporate_email,
            phone=phone,
            category=category,
            balance=balance,
        )

    def __validate_business_name(self, business_name: str) -> None:
        if not business_name.strip():
            raise HttpBadRequestError("Business name cannot be empty.")
        if re.search(r"[^a-zA-Z0-9\s]", business_name):
            raise HttpBadRequestError("Business name contains invalid characters.")

    def __validate_revenue(self, revenue: float) -> None:
        if revenue < 0:
            raise HttpBadRequestError("Revenue cannot be negative.")

    def __validate_corporate_email(self, corporate_email: str) -> None:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", corporate_email):
            raise HttpBadRequestError("Corporate email is invalid.")

    def __validate_phone(self, phone: str) -> None:
        if not re.match(r"^\+?\d{10,15}$", phone):
            raise HttpBadRequestError("Phone number is invalid.")
