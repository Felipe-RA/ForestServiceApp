from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud
from schemas import saved_query as schemas
from dependencies import get_db

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

    return crud.create_saved_query(db=db, query=query)


@router.get("/queries/{id}", response_model=schemas.SavedQuery, summary="Retrieve a specific saved query")
def get_query(id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific saved query by its ID.

    Parameters:
    - **id**: The unique identifier of the saved query.
    - **db**: The database session dependency.

    Returns the `SavedQuery` object if found, else raises a 404 error.
    """

    db_query = crud.get_saved_query(db=db, query_id=id)

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

    return crud.get_user_saved_queries(db=db, username=username)