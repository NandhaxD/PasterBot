import config
from nandhabot import bot


if __name__ == "__main__":
   bot.start()
   with bot:
         bot.send_message(config.OWNER_ID, "Hey Don't worry iam online!")


      
