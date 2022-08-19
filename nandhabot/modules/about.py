
from pyrogram import filters 
from nandhabot import bot 
from pyrogram.types import *

ABOUT_TEXT = """
-Welcome to Nandha's System-:

want to know what's this bot? 
(thinking)

Want to know Nandha's total bots list? 
(below click the *BOTLIST* button)

want to know Nandha's Owned UserNames?
(below click the *OWNED UN* button)

want to know moi others social media's links?
(below click the *Social* button)

"""

ABOUT_BUTTONS = [[ InlineKeyboardButton(text="What's this Bot", callback_data="what"),
                  ],[ InlineKeyboardButton(text="Social", callback_data="social"),
                      InlineKeyboardButton(text="BotList", callback_data="botlist"),
                  ],[ InlineKeyboardButton(text="Founding UN", callback_data="uns")]]
                  
@bot.on_callback_query(filters.regex("about"))
def about(_, query: CallbackQuery):
     query.message.edit(ABOUT_TEXT,reply_markup=InlineKeyboardMarkup(ABOUT_BUTTONS))

