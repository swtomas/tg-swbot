from aiogram import Bot, Dispatcher
import logging
import os
import asyncio
import commands
from dotenv import load_dotenv

load_dotenv() # CREATE .env FILE in main directory, then write TOKEN=BOT_TOKEN
dp = Dispatcher()
TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)

async def main():
    await dp.start_polling(bot)
    await dp.include_routers(commands.router)
if __name__ == "__main__":
    asyncio.run(main())
    print("start")