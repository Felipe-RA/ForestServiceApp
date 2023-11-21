# app/models/saved_query.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Index
from .base import Base



class SavedQuery(Base):

    """
    Defines the SQLAlchemy ORM model for the 'saved_queries' table.
    """

    
    __tablename__ = 'saved_queries'  # Name of the table in the database.

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    query_text = Column(Text, nullable=False)
    username = Column(String, ForeignKey('users.username'), nullable=False)
    comment = Column(Text)
    created_at = Column(DateTime)

    # Define an index on the username column to improve query performance.
    __table_args__ = (
        Index('idx_saved_queries_username', 'username'),
    )