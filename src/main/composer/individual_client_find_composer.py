from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.individual_client_repository import IndividualClientRepository
from src.controllers.individual_client_find_controller import IndividualClientFindController
from src.views.individual_client_find_view import IndividualClientFindView


def individual_client_find_composer():
    model = IndividualClientRepository(db_connection_handler)
    controller = IndividualClientFindController(model)
    view = IndividualClientFindView(controller)

    return view
