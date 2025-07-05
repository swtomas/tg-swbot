from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
import buttons
import dict

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(text=f"Привет, {message.from_user.first_name}!\n{dict.menu()}", parse_mode="HTML", reply_markup=buttons.ru_menu()) # type: ignore
    return True

@router.message(Command("check"))
async def check(message: Message):
    await message.answer_sticker(sticker="CAACAgQAAxkBAAEPyz5oSbCtp9q8niGGvhmbVY0KnusvpwACVwwAAtoI6FBmuh4vtd-VqDYE")
