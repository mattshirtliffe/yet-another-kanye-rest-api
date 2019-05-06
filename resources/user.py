import sqlite3
from flask import Flask, request
from flask_restful import Resource
from passlib.hash import bcrypt
from models.user import User

class UserResource(Resource):
    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']
        first_name = data['first_name']
        last_name = data['last_name']

        if User.find_user_by_email(email):
            return {'message': 'user already exists'}, 400

        password = bcrypt.hash(password)
        new_user = User(email, password, first_name, last_name)
        new_user.save_to_database()
        return {'message': 'user created'}, 201
