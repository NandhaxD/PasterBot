import config
import time
from nandhabot import bot 
from pyrogram import filters 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BANNED = []

START_TEXT = """ Welcome to **Nandhas System!**

You can collect details about 
our channels/bots here thanks for visiting our bots!\n
**YOUR INFORMATION:**
Your name: {}
Your ID: {}

Keep follow our network and check rules/about/alive details!
"""


@bot.on_message(filters.command("start"))
async def start(_, message):
    USER = message.from_user
    if message.from_user.id in BANNED:
       await message.reply_text("sorry son of bitch you can't use this bot")
       return 
    msg = await message.reply_text("Welcome to Nandhas System! Please wait while we finish your info scan...")
    time.sleep(2)
    await msg.edit_text(START_TEXT.format(USER.mention, USER.id),reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("About our Details", callback_data="about"),
                    ],[ InlineKeyboardButton("Our Group", url=f"t.me/{config.support}"),
                       InlineKeyboardButton("Our Updates", url=f"t.me/{config.updates}")]]))
                       
