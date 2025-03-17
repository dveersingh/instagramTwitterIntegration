import requests , re
from .config import logger, INSTAGRAM_USERNAME, RAPIDAPI_KEY

class InstagramClient:
    def __init__(self):
        self.base_url = "https://instagram230.p.rapidapi.com/user/posts"
        self.querystring = {"username":"bbcnews"}
        
        self.headers = {
            "x-rapidapi-key": RAPIDAPI_KEY,
            "x-rapidapi-host": "instagram230.p.rapidapi.com"
        }
        
    
    def get_latest_post(self):
        """Fetch latest Instagram post"""
        try:
            response = requests.get( 
                self.base_url,
                headers=self.headers,
                params=self.querystring
            )
            
            response.raise_for_status()
            
            data = response.json()
            
            if "items" in data and len(data["items"]) > 0:
                latest_post = data["items"][0]  # First post is the latest one
                caption_data = latest_post.get("caption", {})
                

                parsed_data = {
                    "caption":  caption_data.get("text", "No caption available"),
                    "image_url": latest_post.get("display_uri", "No image available"),
                    "id": latest_post.get("id", "No ID available"),
                    "timestamp": latest_post.get("taken_at", "No timestamp available"),
                    
                }
                return parsed_data
              
        except Exception as e:
            logger.error(f"Instagram fetch failed: {str(e)}")
            
            return None
        
         
   
   