from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.legal_entity_client_repository import (
    LegalEntityClientRepository,
)
from src.controllers.legal_entity_client_create_controller import LegalEntityClientCreateController
from src.views.legal_entity_client_create_view import LegalEntityClientCreateView


def legal_entity_client_create_composer():
    model = LegalEntityClientRepository(db_connection_handler)
    controller = LegalEntityClientCreateController(model)
    view = LegalEntityClientCreateView(controller)

    return view
