from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SavedQueryBase(BaseModel):
    """
    Base model for saved queries, defining common attributes.
    Used as a base class for more specific saved query models.
    Attributes:
        name (str): The name assigned to the saved query.
        query_text (str): The SQL text of the saved query.
        username (str): The username of the user who created the query.
    """
    name: str
    query_text: str
    username: str

class SavedQueryCreate(SavedQueryBase):
    """
    Schema for creating a new saved query. Inherits from SavedQueryBase.
    Adds an optional comment field.
    Attributes:
        comment (Optional[str]): An optional comment about the saved query.
    """
    comment: Optional[str] = None

class SavedQuery(SavedQueryBase):
    """
    Schema for representing saved queries, extending the base with additional attributes.
    Attributes:
        id (int): The unique identifier of the saved query.
        created_at (Optional[datetime]): The timestamp when the query was saved.
        comment (Optional[str]): An optional comment about the saved query.
    """
    id: int
    created_at: Optional[datetime] = None
    comment: Optional[str] = None

    class Config:
        """
        Pydantic configuration class to enable ORM mode.
        This allows the model to be compatible with SQLAlchemy models,
        enabling direct usage of database models in FastAPI responses.
        """
        orm_mode = True