from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..models import saved_query as models
from ..schemas import saved_query as schemas
from ..dependencies import get_db

router = APIRouter()

@router.post("/queries/", response_model=schemas.SavedQuery, summary="Create a new saved query")
def create_query(query: schemas.SavedQueryCreate, db: Session = Depends(get_db)):
    """
    Create a new saved query in the database.

    Parameters:
    - **query**: A `SavedQueryCreate` object containing the query details.
    - **db**: The database session dependency.

    Returns a `SavedQuery` object after creating it in the database.
    """
    db_query = models.SavedQuery(**query.dict())
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query

@router.get("/queries/{id}", response_model=schemas.SavedQuery, summary="Retrieve a specific saved query")
def get_query(id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific saved query by its ID.

    Parameters:
    - **id**: The unique identifier of the saved query.
    - **db**: The database session dependency.

    Returns the `SavedQuery` object if found, else raises a 404 error.
    """
    db_query = db.query(models.SavedQuery).filter(models.SavedQuery.id == id).first()
    if db_query is None:
        raise HTTPException(status_code=404, detail="Query not found")
    return db_query

@router.get("/users/{username}/queries", response_model=list[schemas.SavedQuery], summary="Retrieve all queries saved by a user")
def get_queries_by_user(username: str, db: Session = Depends(get_db)):
    """
    Retrieve all queries saved by a specific user.

    Parameters:
    - **username**: The username of the user whose saved queries are to be retrieved.
    - **db**: The database session dependency.

    Returns a list of `SavedQuery` objects.
    """
    queries = db.query(models.SavedQuery).filter(models.SavedQuery.username == username).all()
    return queries