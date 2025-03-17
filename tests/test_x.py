import pytest
from unittest.mock import Mock, patch
from app.x_client import XClient

@pytest.fixture
def mock_tweepy():
    mock = Mock()
    mock.create_tweet.return_value = Mock(data={"id": "123"})
    return mock

def test_post_tweet_success(mock_tweepy):
    with patch('tweepy.Client', return_value=mock_tweepy):
        client = XClient()
        result = client.post_tweet("Test tweet")
        assert result is True
        mock_tweepy.create_tweet.assert_called_once_with(text="Test tweet")

def test_post_tweet_failure():
    with patch('tweepy.Client') as mock_client:
        mock_instance = mock_client.return_value
        mock_instance.create_tweet.side_effect = Exception("API Error")
        client = XClient()
        result = client.post_tweet("Test tweet")
        assert result is False

def test_empty_tweet():
    client = XClient()
    result = client.post_tweet("")
    assert result is False