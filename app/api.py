import re 
from fastapi import FastAPI, HTTPException, Header
from .instagram import InstagramClient
from .gemini import GeminiSummarizer
from .x_client import XClient
from .config import logger
from pydantic import BaseModel

app = FastAPI()


class TweetRequest(BaseModel):
    text: str

@app.get("/latest-post")
async def get_latest_post():
    """Get latest Instagram post"""
    client = InstagramClient()
    post = client.get_latest_post()
    if not post:
        raise HTTPException(404, "No posts found")
    return post


@app.post("/summarize")
async def summarize_text(request: TweetRequest):
    """Summarize text using Gemini AI"""
    try:
        # Validate input
        if not request.text.strip():
            raise HTTPException(400, "Input text cannot be empty")
    
    
    
        
        # Generate summary
        gemini = GeminiSummarizer()
        summary = gemini.summarize(request.text)
        
        return {
            "status": "success",
            "original_length": len(request.text),
            "summary_length": len(summary),
            "summary": summary
        }
        
    except Exception as e:
        logger.error(f"Summarization failed: {str(e)}")
        raise HTTPException(500, f"Summarization failed: {str(e)}")


@app.post("/post-tweet")
async def post_tweet(request: TweetRequest):
    """Post summarized tweet"""
   
    x = XClient()
    #text = "“That’s a tornado.”\n \nA resident in Tylertown, Mississippi, filmed the moment a tornado tore past his home.\n \nSix deaths were reported in the state, with a total of at least 34 people killed in the south-east of the US.\n \nThe deadly tornadoes flipped vehicles and destroyed homes, leaving more than 250,000 properties without power.\n \nFurther severe weather is expected for the region.\n \nTap the link in @BBCNews’s bio for the latest on the tornadoes’ destruction.\n \n#Tornado #BBCNews"
    
    if not request.text.strip():
            raise HTTPException(status_code=400, detail="Tweet text cannot be empty")
            
    if len(request.text) > 280:
        raise HTTPException(status_code=400, detail="Tweet exceeds 280 characters")

    #new_summary = "Cargo ship & oil tanker collide off East Yorkshire coast. 36 rescued, 1 hospitalized. Search called off for 1 missing crew member. More info: @BBCNews link in bio. #NorthSea #ShippingAccident"
    if not x.post_tweet(request.text):
        raise HTTPException(500, "Failed to post tweet")
    
    return {"status": "success", "tweet": request.text}