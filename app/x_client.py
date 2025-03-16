import tweepy
from .config import logger, X_CREDENTIALS

class XClient:
    def __init__(self):
        
        self.client = tweepy.Client(
            #consumer_key=str(X_CREDENTIALS['api_key']),
            #consumer_secret=str(X_CREDENTIALS['api_secret']),
            #access_token=str(X_CREDENTIALS['access_token']),
            #access_token_secret=str(X_CREDENTIALS['access_secret'])
            
            consumer_key=X_API_KEY,
            consumer_secret=X_API_SECRET,
            access_token=X_ACCESS_TOKEN,
            access_token_secret=X_ACCESS_SECRET
        )
    
    def post_tweet(self, text):
        """Post tweet to X"""
        try:
            response = self.client.create_tweet(text=text)
            logger.info(f"Tweet posted: {response.data['id']}")
            return True
        except Exception as e:
            logger.error(f"X post failed: {str(e)}")
            return False