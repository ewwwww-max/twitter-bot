# main.py
# One job: tie everything together and run the bot in a continuous loop.cd D:\twitter_bot
import time
import tweepy
import os
from dotenv import load_dotenv
from monitor import get_speed
from complaint import log_speed, should_complain, format_complaint, log_complaint
from config import CHECK_INTERVAL_SECONDS

load_dotenv()

def get_twitter_client():
    client = tweepy.Client(
        consumer_key=os.getenv("API_KEY"),
        consumer_secret=os.getenv("API_SECRET"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
    )
    return client

def run_bot():
    print("Bot started. Monitoring network performance...")
    client = get_twitter_client()
    
    while True:
        speeds = get_speed()
        
        if speeds is None:
            print("Speed test failed. Retrying next cycle.")
            time.sleep(CHECK_INTERVAL_SECONDS)
            continue
        
        log_speed(speeds)
        
        if should_complain(speeds):
            message = format_complaint(speeds)
            
            try:
                # client.create_tweet(text=message)  # Uncomment when API credits available
                print(f"[SIMULATED TWEET]: {message}")  # Remove when live
                log_complaint(message)
                print("Complaint logged successfully.")

            except Exception as e:
                print(f"Tweet failed: {e}")
                log_complaint(f"FAILED TO TWEET: {message} | Error: {e}")
        
        else:
            print("Speeds are acceptable. No complaint needed.")
        
        time.sleep(CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    run_bot()