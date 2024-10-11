import pytest
from unittest import mock
from function_app import http_triggerwaqas  # Correct import statement

# Mocking the CosmosClient
@pytest.fixture(autouse=True)
def mock_cosmos_client():
    with mock.patch('function_app.CosmosClient') as MockClient:
        yield MockClient

def mock_request():
    class MockRequest:
        params = {}
        def get_json(self):
            return None  # Simulating an empty body

    return MockRequest()

def test_http_trigger_no_name(mocker):
    mock_container = mocker.patch('function_app.container')  # Adjust according to your actual container path
    mock_container.read_item.return_value = {"id": "visitor_count", "count": 5}
    
    req = mock_request()
    response = http_triggerwaqas(req)
    
    assert response.status_code == 200
    assert "visitor_count" in response.get_body().decode()
