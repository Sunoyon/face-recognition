# Import controllers for flask_rebar
from app.controllers import author, health, book

# Import models for flask_migrate
from app.entities import author, book
from app.app import create_app
