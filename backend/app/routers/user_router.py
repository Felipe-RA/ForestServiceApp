from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..models import user as models
from ..schemas import user as schemas
from ..dependencies import get_db

router = APIRouter()

@router.post("/users/", response_model=schemas.User, summary="Create a new user")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user in the database.

    Parameters:
    - **user**: A `UserCreate` object containing the user details.
    - **db**: The database session dependency.

    Returns a `User` object after creating the user in the database.
    """
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users/{username}", response_model=schemas.User, summary="Retrieve a specific user")
def get_user(username: str, db: Session = Depends(get_db)):
    """
    Retrieve a specific user by their username.

    Parameters:
    - **username**: The username of the user.
    - **db**: The database session dependency.

    Returns the `User` object if found, else raises a 404 error.
    """
    db_user = db.query(models.User).filter(models.User.username == username).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user