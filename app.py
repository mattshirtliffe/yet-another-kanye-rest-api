from flask import Flask, jsonify, request
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identify
from resources.user import UserResource
from resources.quote import QuoteResource, QuoteListResource

from datetime import timedelta

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret_key'
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=1)

api = Api(app)

JWT(app, authenticate, identify)

api.add_resource(UserResource, '/users')
api.add_resource(QuoteResource, '/quotes/<string:id>')
api.add_resource(QuoteListResource, '/quotes')

if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run()