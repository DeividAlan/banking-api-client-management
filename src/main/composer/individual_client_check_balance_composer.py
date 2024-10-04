from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.individual_client_repository import IndividualClientRepository
from src.controllers.individual_client_check_balance_controller import (
    IndividualClientCheckBalanceController,
)
from src.views.individual_client_check_balance_view import IndividualClientCheckBalanceView


def individual_client_check_balance_composer():
    model = IndividualClientRepository(db_connection_handler)
    controller = IndividualClientCheckBalanceController(model)
    view = IndividualClientCheckBalanceView(controller)

    return view
