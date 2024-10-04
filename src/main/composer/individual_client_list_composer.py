from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.individual_client_repository import IndividualClientRepository
from src.controllers.individual_client_list_controller import IndividualClientListController
from src.views.individual_client_list_view import IndividualClientListView


def individual_client_list_composer():
    model = IndividualClientRepository(db_connection_handler)
    controller = IndividualClientListController(model)
    view = IndividualClientListView(controller)

    return view
