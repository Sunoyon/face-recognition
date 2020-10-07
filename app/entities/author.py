from datetime import datetime

from sqlalchemy import Column, DateTime, String, Integer

from app.entities.db import db


class Author(db.Model):

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255), nullable=False)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
