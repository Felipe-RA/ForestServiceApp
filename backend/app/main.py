from google.cloud import bigquery
from fastapi import FastAPI

app = FastAPI()

# Initialize the BigQuery client
bigquery_client = bigquery.Client()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/run_query")
def run_query():

    # Example query to access the USForestServiceInventory bigquery DB
    query = """
    SELECT
        tree_inventory_year,
        tree_state_code,
        tree_status_code,
        species_common_name,
        species_scientific_name,
        net_cubicfoot_volume
    FROM
        `bigquery-public-data.usfs_fia.tree` 
    LIMIT
        100
    """


    query_job = bigquery_client.query(query)
    results = query_job.result()  # Waits for the query to finish


    # Convert the results to a list of dictionaries to return as JSON
    return [dict(row) for row in results]
