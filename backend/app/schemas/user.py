from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    """
    Base model for user, defining the core attribute.
    Used as a base class for more specific user models.
    Attributes:
        username (str): The unique username of the user.
    """
    username: str

class UserCreate(UserBase):
    """
    Schema for creating a new user. Currently, this is identical to UserBase,
    but it can be expanded with additional attributes in the future.
    """
    pass

class User(UserBase):
    """
    Schema for representing a user, extending the base with additional attributes.
    Attributes:
        registered_at (Optional[datetime]): The timestamp when the user was registered.
    """
    registered_at: Optional[datetime] = None

    class Config:
        """
        Pydantic configuration class to enable ORM mode.
        Allows the model to be compatible with SQLAlchemy models,
        enabling the direct usage of database models in FastAPI responses.
        """
        orm_mode = True