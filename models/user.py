import sqlite3
import uuid
from db import db
from sqlalchemy import func
import uuid

from .database_helpers import generate_uuid

class User(db.Model):
    __tablename__ = 'users'

    def __init__(self, email, password, first_name, last_name):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    id = db.Column(db.String, name="id", primary_key=True, default=generate_uuid)
    first_name = db.Column(db.String(255), unique=False, nullable=False)
    last_name = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)

    is_active = db.Column(db.Boolean, default=False, nullable=False)

    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return '<User %r>' % self.first_name

    def save_to_database(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_user_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()

    @classmethod
    def find_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()