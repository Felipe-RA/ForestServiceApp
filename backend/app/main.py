from fastapi import FastAPI
from .routers import query_router, user_router, stored_queries_router

# main.py is the entry point of the FastAPI application.

app = FastAPI()

# A root endpoint to confirm that the backend is operational.
@app.get("/")
def read_root():
    return {"Backend is WORKING": "FINE"}

# Include the routers from the routers module.
# These routers handle different API endpoints related to queries, users, and saved queries.
app.include_router(query_router.router)
app.include_router(user_router.router, prefix="/users", tags=["users"])
app.include_router(stored_queries_router.router, prefix="/queries", tags=["queries"])