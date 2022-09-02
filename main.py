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
         BOT_USERNAME = await bot.get_me().username
         await message.reply_text(f"""**Hello sir. {message.from_user.mention}**\n
**The Paster Bot who can helps you to share code or share something whatever you can use this bot to past all Available Service.**

**~ /paste - command only works reply to (message/document) text format!**
""",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="SUBMIT ME", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),],[
InlineKeyboardButton(text="Service Paste", callback_data="service")]]))


bot.run()


         
