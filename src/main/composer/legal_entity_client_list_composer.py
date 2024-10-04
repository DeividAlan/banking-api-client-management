from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.legal_entity_client_repository import (
    LegalEntityClientRepository,
)
from src.controllers.legal_entity_client_list_controller import LegalEntityClientListController
from src.views.legal_entity_client_list_view import LegalEntityClientListView


def legal_entity_client_list_composer():
    model = LegalEntityClientRepository(db_connection_handler)
    controller = LegalEntityClientListController(model)
    view = LegalEntityClientListView(controller)

    return view
