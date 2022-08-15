from config import API_ID, API_HASH, BOT_TOKEN
import logging
import os
from pyrogram import Client 


# enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()],
    level=logging.INFO)



bot = Client(
  "nandhabot", 
  api_id=API_ID, 
  api_hash=API_HASH, 
  bot_token=BOT_TOKEN, 
  plugins=dict(root="{}/modules".format(__name__)))
