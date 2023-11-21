# app/models/user.py

from sqlalchemy import Column, String, DateTime
from .base import Base 


class User(Base):

    """
    Defines the SQLAlchemy ORM model for the 'users' table.
    """

    __tablename__ = 'users'  # Name of the table in the database.

    username = Column(String, primary_key=True)  # Unique identifier for each user.
    registered_at = Column(DateTime)  # Timestamp of when the user first registered.
