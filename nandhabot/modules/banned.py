import config
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from nandhabot import bot 
from nandhabot.modules.start import BANNED 

banned_text = """**Nandha System!**

**Banned user:** {}
**Banned ID:**  {}
**Reason:** {}
"""

@bot.on_message(filters.command("addban"))
async def banned(_, message):
        try:
             if message.reply_to_message:
                  await message.reply_text("@NandhaNetworkBot: Read The guild First")
                  return 
             elif not message.reply_to_message:
                        if len(message.command) <2:
                            await message.reply_text("give a userID")       
                            USER = message.text.split(" ")[1]
                            return 
                        elif len(message.command) <3:
                             await message.relpy_text("give a Reason for Banning")
                        reason = message.text.split(" ")[2]
                        return 
             user = await bot.get_chat(USER)        
             elif user.id in BANNED:
                       await message.reply_text("this son of bitch already banned!")
             elif user.id not in BANNED:
                          BANNED.append(user.id)
                          buttons = [[InlineKeyboardButton("Banned System!" , url="t.me/NandhaSystem")]]
                          await message.reply_text("checkout new banned user!",
                          reply_markup=InlineKeyboardMarkup(buttons))
                          return
             mention = f"tg://user?id={user.id}"
             buttons = [[InlineKeyboardButton("ᴜɴʙᴀɴ" , callback_data="unban"),
                                      InlineKeyboardButton("ᴅᴇʟᴇᴛᴇ" , callback_data="delete")]]
             await bot.send_message("NandhaSystem", 
             banned_text.format(mention,user.id,reason),reply_markup=InlineKeyboardMarkup(buttons))
        except Exception as e:
                        await message.reply_text(f"Error: {e}")

                  
                   
                        
               
                   

