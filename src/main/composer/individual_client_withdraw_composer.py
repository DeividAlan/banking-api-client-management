from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.individual_client_repository import IndividualClientRepository
from src.controllers.individual_client_withdraw_controller import IndividualClientWithdrawController
from src.views.individual_client_withdraw_view import IndividualClientWithdrawView


def individual_client_withdraw_composer():
    model = IndividualClientRepository(db_connection_handler)
    controller = IndividualClientWithdrawController(model)
    view = IndividualClientWithdrawView(controller)

    return view
