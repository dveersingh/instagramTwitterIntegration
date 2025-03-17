import pytest
from unittest.mock import Mock, patch
from app.gemini import GeminiSummarizer

@pytest.fixture
def mock_gemini():
    mock = Mock()
    mock.generate_content.return_value = Mock(text="Short summary")
    return mock

def test_summarize_success(mock_gemini):
    with patch('google.generativeai.GenerativeModel', return_value=mock_gemini):
        summarizer = GeminiSummarizer()
        result = summarizer.summarize("Long text here")
        assert result == "Short summary"

def test_summarize_fallback():
    with patch('google.generativeai.GenerativeModel') as mock_model:
        mock_model.side_effect = Exception("API Error")
        summarizer = GeminiSummarizer()
        long_text = "a" * 300
        result = summarizer.summarize(long_text)
        assert len(result) == 280
        assert result.endswith("...")

def test_empty_input():
    summarizer = GeminiSummarizer()
    result = summarizer.summarize("")
    assert result == ""