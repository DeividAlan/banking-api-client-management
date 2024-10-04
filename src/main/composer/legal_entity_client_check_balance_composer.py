from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.legal_entity_client_repository import (
    LegalEntityClientRepository,
)
from src.controllers.legal_entity_client_check_balance_controller import (
    LegalEntityClientCheckBalanceController,
)
from src.views.legal_entity_client_check_balance_view import LegalEntityClientCheckBalanceView


def legal_entity_client_check_balance_composer():
    model = LegalEntityClientRepository(db_connection_handler)
    controller = LegalEntityClientCheckBalanceController(model)
    view = LegalEntityClientCheckBalanceView(controller)

    return view
