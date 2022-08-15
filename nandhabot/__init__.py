import config
from pyrogram import Client 


# enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()],
    level=logging.INFO)

bot = Client(
  "nandhabot", 
  api_id=config.API_ID, 
  api_hash=config.API_HASH, 
  bot_token=config.BOT_TOKEN, 
  plugins=dict(root="{}/modules".format(__name__)))
