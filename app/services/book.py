from app.entities.db import db
from app.entities.db import update_orm


def save(book):
    db.session.add(book)
    db.session.commit()
    return book
