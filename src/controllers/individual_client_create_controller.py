from typing import Dict
import re
from src.errors.errors_types.http_bad_request import HttpBadRequestError
from src.models.sqlite.interface.client import ClientInterface
from .interfaces.individual_client_create_controller import (
    IndividualClientCreateControllerInterface,
)


class IndividualClientCreateController(IndividualClientCreateControllerInterface):
    def __init__(self, client_repository: ClientInterface) -> None:
        self.__client_repository = client_repository

    def create(self, client_info: Dict) -> None:
        full_name = client_info["full_name"]
        monthly_income = client_info["monthly_income"]
        age = client_info["age"]
        phone = client_info["phone"]
        category = client_info["category"]
        balance = client_info["balance"]

        self.__validate_full_name(full_name)
        self.__validate_phone(phone)
        self.__client_repository.insert_individual_client(
            full_name=full_name,
            monthly_income=monthly_income,
            age=age,
            phone=phone,
            category=category,
            balance=balance,
        )

    def __validate_full_name(self, full_name: str) -> None:
        if not full_name.strip():
            raise HttpBadRequestError("Full name cannot be empty.")
        if re.search(r"[^a-zA-Z\s]", full_name):
            raise HttpBadRequestError("Full name contains invalid characters.")

    def __validate_phone(self, phone: str) -> None:
        phone = phone.strip()
        if not re.match(r"^55\d{2}\d{9}$", phone):
            raise HttpBadRequestError(
                "Phone number is invalid. Please use a valid format, such as '5511912345678'."
            )
