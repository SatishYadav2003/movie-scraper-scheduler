from dotenv import load_dotenv
from urllib.parse import urljoin
import time
import os
import requests

load_dotenv()


def telegram_message_forward(all_latest_movie_name_array, movie_links):
    
     
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    
    
    
    for movie_name, movie_link in zip(all_latest_movie_name_array, movie_links):
        
        
        movie_full_url = urljoin(os.getenv("MP4_MOVIEZ_LINK"), movie_link)
        
        message_body = """ ********** Hello <b>Satish Yadav</b> *********** \n\nMovie-Alert: <b>We found new movie for you</b>"""
        message_body += f"\n\nMovie-Name: <b>{movie_name}</b>\n\nMovie-Link: {movie_full_url}\n\n"

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message_body,
            "parse_mode": "HTML"
        }

        requests.post(url, json=payload)

        time.sleep(1)
     
          
