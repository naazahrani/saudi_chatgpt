from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     username = Column(String(50), nullable=False, unique=True)
#     email = Column(String(120), nullable=False, unique=True)
#     password = Column(String(128), nullable=False)
#     posts = relationship('Post', backref='author', lazy=True)

class Doctors(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False, unique=False)
    last_name = Column(String(20), nullable=False, unique=False)
    specialization = Column(String(30), nullable=False, unique=False)
    qualification = Column(String(30), nullable=False, unique=False)
    clinic = Column(String(50), nullable=False, unique=False)
    country = Column(String(30), nullable=False, unique=False)
    city = Column(String(20), nullable=False, unique=False)
    availability = Column(String(30), nullable=False, unique=False)
    consultation_fee = Column(Integer, nullable=False, unique=False)
    service_type = Column(String(50), nullable=True, unique=False)