from datetime import timedelta

class BaseConfig():
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://siia:siiauas@localhost:5432/siiadb'
    SQLALCHEMY_DATABASE_URI = 'postgresql://doadmin:iyTqd0IsG1ZNGiK0@db-postgresql-sfo2-06782-do-user-10528240-0.b.db.ondigitalocean.com:25060/defaultdb?sslmode=require'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "10d58d427fc9fe1426de41f0"
    JWT_SECRET_KEY = "10d58d427fc9fe1426de41f0"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
