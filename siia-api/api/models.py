from sqlalchemy.schema import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import CHAR, Date, Float
from sqlalchemy.types import Boolean, Integer, String, DateTime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class School(db.Model):
    __tablename__ = 'schools'
    id = Column('id', Integer, primary_key=True)
    school_name = Column('school_name', String, nullable=False)