from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.legal_entity_client_repository import (
    LegalEntityClientRepository,
)
from src.controllers.legal_entity_client_find_controller import LegalEntityClientFindController
from src.views.legal_entity_client_find_view import LegalEntityClientFindView


def legal_entity_client_find_composer():
    model = LegalEntityClientRepository(db_connection_handler)
    controller = LegalEntityClientFindController(model)
    view = LegalEntityClientFindView(controller)

    return view
