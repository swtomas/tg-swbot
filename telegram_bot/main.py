from aiogram import Bot, Dispatcher
import asyncio
import os
import commands
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("TOKEN")

bot = Bot(token=BOT_TOKEN) # type: ignore
dp = Dispatcher()

# Основная функция
async def main(): 
   try: 
    print("запуск")
    dp.include_router(commands.router)
    await dp.start_polling(bot)
   except Exception as e:
      print(e)
if __name__ == "__main__":
    asyncio.run(main())