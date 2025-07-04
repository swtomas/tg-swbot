from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
import buttons

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.reply("Выберите язык | Choose your language:", reply_markup=buttons.start_buttons())
    return True
