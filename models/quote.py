import uuid
from db import db

from sqlalchemy import func
from .database_helpers import generate_uuid

class Quote(db.Model):
    __tablename__ = 'quotes'

    id = db.Column(db.String, name="id", primary_key=True, default=generate_uuid)
    quote = db.Column(db.String(255), nullable=False)

    user_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=True)
    user = db.relationship('User')

    created_at = db.Column(db.DateTime, server_default=func.now())
    deleted_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def __init__(self, quote):
        self.quote = quote
    
    def json(self):
        return {'id':self.id,'quote': self.quote}

    def save_to_database(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_database(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, quote_id):
        return cls.query.filter_by(id=quote_id).first()


