import os
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class BaseConfig():
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(12) # genera una cadena de 12 caracteres randomizados como llave secreta
    JWT_SECRET_KEY = os.urandom(12)
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)