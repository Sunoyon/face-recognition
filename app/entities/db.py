from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def update_orm(orm_object, update_dict):
    for key, value in update_dict.items():
        setattr(orm_object, key, value)
