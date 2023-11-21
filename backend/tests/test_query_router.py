from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app

client = TestClient(app)

@patch('app.dependencies.get_bigquery_client')
def test_run_query(mock_get_bigquery_client):
    # Setup mock BigQuery client
    mock_bigquery_client = MagicMock()
    mock_get_bigquery_client.return_value = mock_bigquery_client

    # Create mock data similar to what BigQuery would return
    mock_data = [
        {
            "tree_inventory_year": 2011,
            "tree_state_code": "51",
            "tree_status_code": "1",
            "species_common_name": "chestnut oak",
            "species_scientific_name": "Quercus prinus",
            "net_cubicfoot_volume": 16.705032348632812
        },
        {
            "tree_inventory_year": 2011,
            "tree_state_code": "51",
            "tree_status_code": "1",
            "species_common_name": "Virginia pine",
            "species_scientific_name": "Pinus virginiana",
            "net_cubicfoot_volume": 5.3596048355102539
        },
        {
            "tree_inventory_year": 2011,
            "tree_state_code": "51",
            "tree_status_code": "1",
            "species_common_name": "black oak",
            "species_scientific_name": "Quercus velutina",
            "net_cubicfoot_volume": 2.1493721008300781
        },
        {
            "tree_inventory_year": 2011,
            "tree_state_code": "51",
            "tree_status_code": "1",
            "species_common_name": "northern red oak",
            "species_scientific_name": "Quercus rubra",
            "net_cubicfoot_volume": 70.3230972290039
        },
        {
            "tree_inventory_year": 2011,
            "tree_state_code": "51",
            "tree_status_code": "1",
            "species_common_name": "mockernut hickory",
            "species_scientific_name": "Carya alba",
            "net_cubicfoot_volume": 24.748567581176758
        }
    ]

    # Mock the return value of the query
    mock_query_result = MagicMock()
    mock_query_result.result.return_value = mock_data
    mock_bigquery_client.query.return_value = mock_query_result

    # Call the API endpoint
    response = client.get("/run_query")

    # Assert the response
    assert response.status_code == 200
    assert response.json() == mock_data
