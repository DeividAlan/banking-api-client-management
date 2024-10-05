from pydantic import BaseModel, constr, ValidationError, PositiveFloat, EmailStr
from src.views.http_types.http_request import HttpRequest
from src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntityError


def legal_entity_client_validator(http_request: HttpRequest) -> None:

    class LegalEntityClientCreationData(BaseModel):
        business_name: constr(min_length=1)  # type: ignore
        revenue: PositiveFloat
        corporate_email: EmailStr
        phone: constr(min_length=1)  # type: ignore
        category: constr(min_length=1)  # type: ignore
        balance: PositiveFloat

    try:
        LegalEntityClientCreationData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(
            {"errors": e.errors(), "message": "Validation failed for the provided data."}
        ) from e
