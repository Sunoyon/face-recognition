import flask_rebar

from app.app import v1_registry
from app.entities.book import Book
from app.services import book as book_service
from app.schemas.request.book import BookRequestSchema
from app.schemas.response.book import BookResponseSchema


@v1_registry.handles(
    rule="/book",
    method="POST",
    response_body_schema={201: BookResponseSchema()},
    request_body_schema=BookRequestSchema()
)
def create_book():
    body = flask_rebar.get_validated_body()
    book = Book(**body)
    book = book_service.save(book)
    return book, 201
