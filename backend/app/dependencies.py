from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from google.cloud import bigquery
import os

# dependencies.py contains the SQLAlchemy setup for database interactions.

# Environment variables are used to configure the database connection.
# This allows for flexibility and keeps sensitive information out of the codebase.
username = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
database = os.getenv("POSTGRES_DB")
host = "db"  # This is the Docker Compose service name for the Database.

# Construct the SQLALCHEMY_DATABASE_URL using environment variables.
SQLALCHEMY_DATABASE_URL = f"postgresql://{username}:{password}@{host}/{database}"

# Create a SQLAlchemy engine that connects to the PostgreSQL database.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal is a factory for producing instances of Session class.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    """
    Dependency that creates and yields a new SQLAlchemy SessionLocal object,
    providing a scoped session for each request and ensuring cleanup afterward.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_bigquery_client() -> bigquery.Client:
    """
    Dependency that creates a Bigquery session
    """
    return bigquery.Client()