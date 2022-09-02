import requests 
import config
import logging 
from requests import post, get
import os
import aiofiles
import socket

from asyncio import get_running_loop
from functools import partial
from aiohttp import ClientSession
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

from SafoneAPI import SafoneAPI

Safone = SafoneAPI()

bot = Client("pasterbot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)
aiohttpsession = ClientSession()

session  = aiohttpsession

async def send(url: str, *args, **kwargs):
    async with session.post(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data

BASE = "https://batbin.me/"
    
      
def spacebin(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = post(url, data={"content": text, "extension": "txt"})
    return f"https://spaceb.in/{res.json()['payload']['id']}"


def _netcat(host, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(content.encode())
    s.shutdown(socket.SHUT_WR)
    while True:
        data = s.recv(4096).decode("utf-8").strip("\n\x00")
        if not data:
            break
        return data
    s.close()
    
async def ezup(content):
    loop = get_running_loop()
    link = await loop.run_in_executor(
        None, partial(_netcat, "ezup.dev", 9999, content)
    )
    return link

@bot.on_message(filters.command("start"))
async def start(_, message):
         global user
         start = await message.reply("**process starting.**")
         user = await bot.get_users(message.from_user.id)
         client = await bot.get_me()
         voice = "./Paster Bot Start.mp3"
         thumb_id = "./IMG_20220903_013242_387.jpg"
         await message.reply_audio(audio=voice,title="PasterBot",thumb=thumb_id,caption=f"""**Hello sir. {message.from_user.mention}**\n
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

@bot.on_message(filters.command('paste'))
async def paste(_, m):
 try:
    reply = m.reply_to_message
    if not reply:
           await m.reply_text("Reply to Message or Text-File")
    if reply.document:
        doc = await m.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
          file_text = await f.read()
        os.remove(doc)
        msg = await m.reply("**Starting to Past  Process.**")
        spacebin_url = spacebin(file_text)
        safone_url = await Safone.paste(file_text)
        ezup_link = await ezup(file_text)
        resp = await send(f"{BASE}api/v2/paste", data=file_text)
        code = resp["message"]
        bat_link = f"{BASE}{code}"
        await msg.edit("**Process Complete**")                  
        caption = f"[SPACEBIN]({spacebin_url}) | [EZUP.DEV]({ezup_link})\n [SAFONE]({safone_url.link}) | [BATBIN]({bat_link})"
        await m.reply_photo(photo=bat_link,caption=caption,
                      reply_markup=InlineKeyboardMarkup(
                          [[InlineKeyboardButton(text="BATBIN", url=bat_link),],[InlineKeyboardButton("SPACEBIN", url=spacebin_url),
                         ],[ InlineKeyboardButton("EZUP.DEV", url=ezup_link),],[ InlineKeyboardButton(text="SAFONE", url=safone_url.link),]]))
    elif reply.text or reply.caption:
          text = reply.text or reply.caption
          msg = await m.reply("**Starting to Past Process.**")                
          spacebin_url = spacebin(text)
          link = await ezup(text)
          safone_url = await Safone.paste(text)
          resp = await send(f"{BASE}api/v2/paste", data=text)
          code = resp["message"]
          bat_link = f"{BASE}{code}"
          await msg.edit("**Process Complete.**")                 
          caption = f"[SPACEBIN]({spacebin_url}) | [EZUP.DEV]({link})\n [SAFONE]({safone_url.link}) | [BATBIN]({bat_link}) "
          await m.reply_photo(photo=bat_link,caption=caption,
                      reply_markup=InlineKeyboardMarkup(
                          [[InlineKeyboardButton(text="BATBIN", url=bat_link),],[InlineKeyboardButton(text="SAFONE", url=safone_url.link), ],[ InlineKeyboardButton("SPACEBIN", url=spacebin_url),
                           ],[ InlineKeyboardButton("EZUP.DEV", url=link)]]))   

 except Exception as e:
       await msg.edit(f"**ERROR**: {e}")

bot.run()


         
