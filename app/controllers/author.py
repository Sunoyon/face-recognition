import logging
from datetime import datetime

import flask_rebar
from flask_rebar import errors

from app.app import v1_registry
from app.entities.author import Author
from app.schemas.request.author import AuthorRequestSchema
from app.schemas.response.author import AuthorResponseSchema
from app.services import author as author_service


@v1_registry.handles(
    rule="/author",
    method="POST",
    response_body_schema={201: AuthorResponseSchema()},
    request_body_schema=AuthorRequestSchema()
)
def create_author():
    body = flask_rebar.get_validated_body()
    author = Author(**body)
    author = author_service.save(author)
    return author, 201


@v1_registry.handles(
    rule="/author/<int:author_id>",
    method="GET",
    response_body_schema=AuthorResponseSchema()
)
def get_author_by_id(author_id: int):
    author = author_service.get_by_id(author_id)
    if author is None:
        logging.error("Author is not found for [author_id=%s]", author_id)
        raise errors.NotFound(msg="Author is not found for [author_id={}]".format(author_id),
                              additional_data={'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

    return author


@v1_registry.handles(
    rule="/author/<string:author_name>",
    method="GET",
    response_body_schema=AuthorResponseSchema(many=True)
)
def get_author_by_name(author_name: str):
    authors = author_service.get_by_name(author_name)
    if not authors:
        logging.error("Author is not found for [author_name=%s]", author_name)
        raise errors.NotFound(msg="Author is not found for [name={}]".format(author_name)
                              , additional_data={'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    return authors


@v1_registry.handles(
    rule="/author/<int:author_id>",
    method="PUT",
    response_body_schema={200: AuthorResponseSchema()},
    request_body_schema=AuthorRequestSchema()
)
def update_author(author_id: int):
    body = flask_rebar.get_validated_body()
    author = author_service.update(author_id, body)
    if author is None:
        logging.error("Author is not found for [author_id=%s]", author_id)
        raise errors.NotFound(msg="Author is not found for [author_id={}]".format(author_id)
                              , additional_data={'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    return author, 200


