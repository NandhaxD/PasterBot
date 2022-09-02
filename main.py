import requests 
import config
import logging 

from pyrogram import idle, Client 
from pyrogram import filters
from pyrogram.types import ( 
InlineKeyboardButton, 
InlineKeyboardMarkup, )
 
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()],
    level=logging.INFO)

     

bot = Client("pasterbot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)



@bot.on_message(filters.command("start"))
async def start(_, message):
         await message.reply_text(text=f"""**Hello sir, {message.from_user.mention}**
**commands: /paste - reply to message text or  file text to Paste All  Available Servers.
Made by @NandhaBots**
""")


bot.start()


         
