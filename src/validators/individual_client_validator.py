from pydantic import BaseModel, constr, ValidationError, field_validator
from src.views.http_types.http_request import HttpRequest
from src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntityError


def individual_client_validator(http_request: HttpRequest) -> None:

    class IndividualClientCreationData(BaseModel):
        full_name: constr(min_length=1)  # type: ignore
        monthly_income: float
        age: int
        phone: constr(min_length=1)  # type: ignore
        category: constr(min_length=1)  # type: ignore
        balance: float

        @field_validator("monthly_income", "balance")
        def check_positive(cls, value: float) -> float:
            if value < 0:
                raise ValueError("Must be a positive number.")
            return value

        @field_validator("age")
        def check_age(cls, value: int) -> int:
            if value < 0:
                raise ValueError("Age must be a non-negative integer.")
            return value

    try:
        IndividualClientCreationData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
