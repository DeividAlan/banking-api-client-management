from pydantic import BaseModel, constr, ValidationError, field_validator
from src.views.http_types.http_request import HttpRequest
from src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntityError


def legal_entity_client_validator(http_request: HttpRequest) -> None:

    class LegalEntityClientCreationData(BaseModel):
        business_name: constr(min_length=1)  # type: ignore
        revenue: float
        corporate_email: str
        phone: constr(min_length=1)  # type: ignore
        category: constr(min_length=1)  # type: ignore
        balance: float

        @field_validator("revenue", "balance")
        def check_positive(cls, value: float) -> float:  # type: ignore
            if value < 0:
                raise ValueError("Must be a positive number.")
            return value

        @field_validator("corporate_email")
        def validate_email(cls, value: str) -> str:  # type: ignore
            if "@" not in value or "." not in value:
                raise ValueError("Must be a valid email address.")
            return value

    try:
        LegalEntityClientCreationData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
