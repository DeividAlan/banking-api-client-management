from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.legal_entity_client_repository import (
    LegalEntityClientRepository,
)
from src.controllers.legal_entity_client_withdraw_controller import (
    LegalEntityClientWithdrawController,
)
from src.views.legal_entity_client_withdraw_view import LegalEntityClientWithdrawView


def legal_entity_client_withdraw_composer():
    model = LegalEntityClientRepository(db_connection_handler)
    controller = LegalEntityClientWithdrawController(model)
    view = LegalEntityClientWithdrawView(controller)

    return view
