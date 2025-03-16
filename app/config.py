import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Environment variables
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME', 'bbcnews')
RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')
GEMINI_KEY = os.getenv('GEMINI_KEY')
X_CREDENTIALS = {
    'api_key': os.getenv('X_API_KEY'),
    'api_secret': os.getenv('X_API_SECRET'),
    'access_token': os.getenv('X_ACCESS_TOKEN'),
    'access_secret': os.getenv('X_ACCESS_SECRET')
}