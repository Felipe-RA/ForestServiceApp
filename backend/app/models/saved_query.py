# app/models/saved_query.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Index, Sequence
from .base import Base

class SavedQuery(Base):
    __tablename__ = 'saved_queries'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    query_text = Column(Text, nullable=False)
    username = Column(String, ForeignKey('users.username'), nullable=False)
    comment = Column(Text)
    created_at = Column(DateTime)

    __table_args__ = (
        Index('idx_saved_queries_username', 'username'),
    )
