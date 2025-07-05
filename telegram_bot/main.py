from aiogram import Bot, Dispatcher
import asyncio
import os
import forms, callbacks, commands, database
import logging
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")
logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN) 
dp = Dispatcher()

async def main(): 
   try: 
    dp.include_routers(commands.router, forms.router, callbacks.router)
    await database.init()
    await dp.start_polling(bot)
   except Exception as e:
      print(e)

if __name__ == "__main__":
    asyncio.run(main())