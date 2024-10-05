from pydantic import BaseModel, constr, ValidationError, PositiveFloat, PositiveInt
from src.views.http_types.http_request import HttpRequest
from src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntityError


def individual_client_validator(http_request: HttpRequest) -> None:

    class IndividualClientCreationData(BaseModel):
        full_name: constr(min_length=1)  # type: ignore
        monthly_income: PositiveFloat
        age: PositiveInt
        phone: constr(min_length=1)  # type: ignore
        category: constr(min_length=1)  # type: ignore
        balance: PositiveFloat

    try:
        IndividualClientCreationData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
