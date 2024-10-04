from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.individual_client_repository import IndividualClientRepository
from src.controllers.individual_client_create_controller import IndividualClientCreateController
from src.views.individual_client_create_view import IndividualClientCreatorView


def individual_client_create_composer():
    model = IndividualClientRepository(db_connection_handler)
    controller = IndividualClientCreateController(model)
    view = IndividualClientCreatorView(controller)

    return view
