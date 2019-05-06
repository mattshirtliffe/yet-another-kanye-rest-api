from models.user import User
from passlib.hash import bcrypt

def authenticate(email, password):
    user = User.find_user_by_email(email)
    if user and bcrypt.verify(password, user.password):
        return user

def identify(payload):
    user_id = payload['identity']
    return User.find_user_by_id(user_id)
