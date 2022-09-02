import requests 
import config
import logging 

from pyrogram import idle, Client 
from pyrogram import filters
from pyrogram.types import ( 
InlineKeyboardButton, 
InlineKeyboardMarkup, 
InputMediaPhoto)
 
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()],
    level=logging.INFO)

     

bot = Client("pasterbot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)



@bot.on_message(filters.command("start"))
async def start(_, message):
         global user
         start = await message.reply("**process starting.**")
         user = await bot.get_users(message.from_user.id)
         client = await bot.get_me()
         voice = "./Paster Bot Start.mp3"
         await message.reply_audio(audio=voice,caption=f"""**Hello sir. {message.from_user.mention}**\n
**The Paster Bot who can helps you to share code or share something whatever you can use this bot to past all Available Service.**

**~ /paste - command only works reply to (message/document) text format!**
""",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="SUBMIT ME", url=f"http://t.me/{client.username}?startgroup=true"),],[
InlineKeyboardButton(text="Service Paste", callback_data="service")]]))
          
         await start.edit("**complete process.**")
         await start.delete()

@bot.on_callback_query(filters.regex("service"))
async def service(_, query):
        if query.from_user.id == user.id:
            await query.message.edit_media(
                       media=InputMediaPhoto(
      "http://telegra.ph/file/b4c7453a0b5c62df60063.jpg",
      caption=f"""
**Available Service Paste!**

~ batbin.me
~ paste.safone.tech
~ spaceb.in
~ ezup.dev

**Share and Support >_<**
"""
    ))
        else:
              await query.answer("This is message NOT for you", show_alert=True)

BATBIN_URL = "batbin.me/"

@bot.on_message(filters.command(["paste","batbin"]))
async def paste(_, message):
          if message.command[0] == "b":
              resp = await send(f"{BATBIN_URL}api/v2/paste", data=file_text)
              code = resp["message"]
              bat_link = f"{BATBIN_URL}{code}"
              await message.reply_photo(bat_link,caption=f"**Successfully Pasted Batbin.me Service**: **Paster Link**:{batlink}")
         

bot.run()


         
