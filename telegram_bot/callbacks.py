from aiogram import Router,F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import dict
import buttons

class From(StatesGroup):
 chatgpt=State()
 chatgptsearch=State()
 chatgpt3o = State()
 

router = Router()

@router.callback_query(F.data == "menu")
async def ru_start(callback: CallbackQuery):
 try:
  await callback.message.edit_text(text=f"Привет, {callback.from_user.first_name}!\n{dict.menu()}", parse_mode="HTML", reply_markup=buttons.ru_menu())
 except Exception as e:
  print(e) 

@router.callback_query(F.data == "chatgpt")
async def chatgpt(callback: CallbackQuery):
 try:
  await callback.message.edit_text(text=f"{callback.from_user.first_name}, выбран ChatGPT 4.1. Напишите ваш запрос:")
 except Exception as e:
  print(e)  