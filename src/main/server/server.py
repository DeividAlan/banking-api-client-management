from flask import Flask
from flasgger import Swagger
from flask_cors import CORS
from src.models.sqlite.settings.connection import db_connection_handler

from src.main.routes.individual_client_routes import individual_client_routes_bp
from src.main.routes.legal_entity_client_routes import legal_entity_client_routes_bp

db_connection_handler.connect_to_db()

app = Flask(__name__)
swagger = Swagger(app)
CORS(app)

app.register_blueprint(individual_client_routes_bp)
app.register_blueprint(legal_entity_client_routes_bp)
