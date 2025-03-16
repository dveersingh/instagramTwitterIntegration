import google.generativeai as genai
from .config import logger, GEMINI_KEY

genai.configure(api_key=GEMINI_KEY)

class GeminiSummarizer:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-2.0-flash')
    
    def summarize(self, text, max_length=280):
        """Summarize text for Twitter"""
        try:
            response = self.model.generate_content(
                f"Summarize this in under {max_length} characters for Twitter: {text}"
            )
            return response.text[:max_length].strip()
        except Exception as e:
            logger.error(f"Gemini summarization failed: {str(e)}")
            return text[:max_length-3] + "..." if len(text) > max_length else text