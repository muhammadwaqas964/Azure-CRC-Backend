from unittest import mock
import pytest
from function_app import http_triggerwaqas

def mock_request():
    class MockRequest:
        params = {}
        def get_json(self):
            return None  # Simulating an empty body

    return MockRequest()

@mock.patch('function_app.CosmosClient')
def test_http_trigger_no_name(mock_cosmos_client):
    mock_container = mock_cosmos_client.return_value.container
    mock_container.read_item.return_value = {"id": "visitor_count", "count": 5}
    
    req = mock_request()
    response = http_triggerwaqas(req)
    
    assert response.status_code == 200
    assert "visitor_count" in response.get_body().decode()

