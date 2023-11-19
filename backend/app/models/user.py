# app/models/user.py

from sqlalchemy import Column, String, DateTime
from .base import Base 

class User(Base):
    __tablename__ = 'users'

    username = Column(String, primary_key=True)
    registered_at = Column(DateTime)