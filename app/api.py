from fastapi import FastAPI, HTTPException, Header
from .instagram import InstagramClient
from .gemini import GeminiSummarizer
from .x_client import XClient
from .config import logger

app = FastAPI()

@app.get("/latest-post")
async def get_latest_post():
    """Get latest Instagram post"""
    client = InstagramClient()
    post = client.get_latest_post()
    if not post:
        raise HTTPException(404, "No posts found")
    return post

@app.post("/post-tweet")
async def post_tweet():
    """Post summarized tweet"""
    #ig = InstagramClient()
    gemini = GeminiSummarizer()
    x = XClient()
    
    #post = ig.get_latest_post()
    #if not post or not post.get('caption'):
    #   raise HTTPException(404, "No valid post found")
    post =  "This footage shows the aftermath of a collision involving a cargo ship and oil tanker in the North Sea."\
            "The collision took place off the coast of East Yorkshire, near Hull in the UK."\
            "Thirty-six people were brought ashore, one of whom was hospitalised."\
            "The search has been called off for one unaccounted for cargo crew member after “an extensive search”, HM Coastguard said." \
            "Tap the link in @BBCNews’s bio read more about the incident."
    #summary = gemini.summarize(post['caption'])
    #decoded_text = post.encode('utf-8').decode('unicode_escape')
    #cleaned_text = decoded_text.replace('\\"', '"').replace('\\n', '\n')
    #api_input = cleaned_text.encode('utf-8')
    #summary = gemini.summarize(post)
    #print(summary)
    new_summary = "Cargo ship & oil tanker collide off East Yorkshire coast. 36 rescued, 1 hospitalized. Search called off for 1 missing crew member. More info: @BBCNews link in bio. #NorthSea #ShippingAccident"
    if not x.post_tweet(new_summary):
        raise HTTPException(500, "Failed to post tweet")
    
    return {"status": "success", "tweet": new_summary}