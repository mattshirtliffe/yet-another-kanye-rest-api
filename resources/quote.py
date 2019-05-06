import sqlite3
from flask import Flask, request
from flask_restful import Resource
from models.quote import Quote
from flask_jwt import jwt_required, current_identity
import random


class QuoteResource(Resource):

    def get(self, id):
        if id == 'random':
            return random.choice([quote.json() for quote in Quote.query.all()])
        return Quote.find_by_id(id).json()

class QuoteListResource(Resource):
    
    @jwt_required()
    def post(self):
        data = request.get_json()
        quote_text = data['quote'] 

        quote = Quote(quote_text)
        try:
            quote.save_to_database()
        except Exception as e: 
            print(e)
            return {'message': 'An error occurred inserting the quote'}, 500
        
        return quote.json(), 201

    def get(self):
        return {"quotes": [quote.json() for quote in Quote.query.all()]}
