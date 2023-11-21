from fastapi import APIRouter, Depends
from google.cloud import bigquery
from app.dependencies import get_bigquery_client

router = APIRouter()


# Initialize the BigQuery client
bigquery_client = bigquery.Client()


@router.get("/run_query")
def run_query(bigquery_client: bigquery.Client = Depends(get_bigquery_client)):

    """
    Runs a query to GCloud bigquery. This function is just a test and shall be deprecated in favor
    of a better implementation

    Returns list of dicts to return as JSON
    """



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
