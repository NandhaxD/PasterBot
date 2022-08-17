import config
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from nandhabot import bot 
from nandhabot.modules.start import BANNED 

banned_text = """**Nandha System!**

**target msg:** [link]({})
**Banned user:** {}
**Banned ID:**  {}
**Reason:** {}
"""

@bot.on_message(filters.command("addban"))
async def banned(_, message):
        try:
            if message.from_user.id in BANNED:
                 await message.reply_text("this son of bitch already banned!")
                 return 
            elif message.reply_to_message:
                  USER = message.reply_to_message.from_user
                  text = message.text
                  reason = text 
                  BANNED.append(message.reply_to_message.from_user.id)
                  buttons = [[InlineKeyboardButton("Banned System!" , url="t.me/NandhaSystem")]]
                  await message.reply_text("checkout new banned user!",
                  reply_markup=InlineKeyboardMarkup(buttons))
                  buttons = [[InlineKeyboardButton("ᴜɴʙᴀɴ" , callback_data="unban"),
                                      InlineKeyboardButton("ᴅᴇʟᴇᴛᴇ" , callback_data="delete")]]
                  await bot.send_message("@NandhaSystem", banned_text.format(message.reply_to_message.link,USER.mention,USER.id,reason),
                  reply_markup=InlineKeyboardMarkup(buttons))
            else:
                   if not message.reply_to_message:
                        user_id = message.text.split(" ")[1]
                        return 
                   if user_id in BANNED:
                       await message.reply_text("this son of bitch already banned!")
                   elif user_id not in BANNED:
                          BANNED.append(user_id)
                          await message.reply_text("checkout new banned user!")
        except Exception as e:
                        await message.reply_text(f"Error: {e}")
                         
@bot.on_message(filters.command(["rban","removeban"]))
async def removeban(_, message):
          try:
              if message.reply_to_message.from_user.id not in BANNED:
                    await message.reply_text("user is not banned!")
                    return 
              if message.reply_to_message.from_user.id in BANNED:
                       BANNED.remove(message.reply_to_message.from_user.id)
                       await message.reply_text("Successfully remove ban")
                       return 
          except Exception as e:
                        await message.reply_text(f"Error: {e}")
     
               
                   

