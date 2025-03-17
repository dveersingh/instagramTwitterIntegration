import pytest
from unittest.mock import Mock, patch
from app.instagram import InstagramClient

@pytest.fixture
def mock_response():
    mock = Mock()
    mock.json.return_value = {
        "data": [{
            "caption": {"text": "Test caption"},
            "image_versions2": {"candidates": [{"url": "http://test.com/image.jpg"}]}
        }]
    }
    return mock

def test_get_latest_post_success(mock_response):
    with patch('requests.get', return_value=mock_response) as mock_get:
        client = InstagramClient()
        result = client.get_latest_post()
        
        assert result is not None
        assert result['caption'] == "Test caption"
        mock_get.assert_called_once()

def test_get_latest_post_empty_response():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {"data": []}
        client = InstagramClient()
        result = client.get_latest_post()
        assert result is None

def test_get_latest_post_api_failure():
    with patch('requests.get') as mock_get:
        mock_get.side_effect = Exception("API Error")
        client = InstagramClient()
        result = client.get_latest_post()
        assert result is None