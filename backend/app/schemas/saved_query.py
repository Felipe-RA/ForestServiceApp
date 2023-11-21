from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SavedQueryBase(BaseModel):
    name: str
    query_text: str
    username: str

class SavedQueryCreate(SavedQueryBase):
    comment: Optional[str] = None

class SavedQuery(SavedQueryBase):
    id: int
    created_at: Optional[datetime] = None
    comment: Optional[str] = None

    class Config:
        orm_mode = True
