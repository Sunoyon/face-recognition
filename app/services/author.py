from app.entities.author import Author
from app.entities.db import db
from app.entities.db import update_orm


def save(author):
    db.session.add(author)
    db.session.commit()
    return author


def get_by_id(author_id):
    return Author.query.get(author_id)


def get_by_name(author_name):
    return Author.query.filter_by(name=author_name).all()


def update(author_id, author):
    db_entry = Author.query.get(author_id)
    if db_entry is not None:
        update_orm(db_entry, author)
        db.session.commit()
    return db_entry
