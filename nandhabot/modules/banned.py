from pyrogram import filters
from nandhabot import bot 
from nandhabot.modules.start import BANNED

@bot.on_message(filters.command("addban"))
async def banned(_, message):
        try:
            if message.from_user.id in BANNED:
                 await message.reply_text("this son of bitch already banned!")
                 return 
            elif message.reply_to_message:
                 BANNED.append(message.reply_to_message.from_user.id)
                 await message.reply_text("checkout new banned user!")
             else:
                   user_id = message.text.split(" ")[1]
                   if user.id in BANNED:
                       await message.reply_text("this son of bitch already banned!")
                   elif user.id not in BANNED:
                          BANNED.append(user_id)
        except Exception as e:
                        await message.reply_text(f"Error: {e}")
                         
