from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    """
    Create a new user in the database.

    Parameters:
    - db: The database session.
    - user: A UserCreate schema object containing user data.

    Returns:
    The newly created User object.
    """
    db_user = models.User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, username: str):
    """
    Retrieve a user by their username.

    Parameters:
    - db: The database session.
    - username: The username of the user to retrieve.

    Returns:
    The User object if found, otherwise None.
    """
    return db.query(models.User).filter(models.User.username == username).first()

def create_saved_query(db: Session, query: schemas.SavedQueryCreate):
    """
    Create a new saved query in the database.

    Parameters:
    - db: The database session.
    - query: A SavedQueryCreate schema object containing the query data.

    Returns:
    The newly created SavedQuery object.
    """
    db_query = models.SavedQuery(**query.dict())
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query

def get_saved_query(db: Session, query_id: int):
    """
    Retrieve a specific saved query by its ID.

    Parameters:
    - db: The database session.
    - query_id: The ID of the saved query to retrieve.

    Returns:
    The SavedQuery object if found, otherwise None.
    """
    return db.query(models.SavedQuery).filter(models.SavedQuery.id == query_id).first()

def get_user_saved_queries(db: Session, username: str):
    """
    Retrieve all saved queries for a specific user.

    Parameters:
    - db: The database session.
    - username: The username of the user whose saved queries are to be retrieved.

    Returns:
    A list of SavedQuery objects.
    """
    return db.query(models.SavedQuery).filter(models.SavedQuery.username == username).all()
