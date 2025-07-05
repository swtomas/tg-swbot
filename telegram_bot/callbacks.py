from aiogram import Router,F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import dict
import buttons

class Form(StatesGroup):
 chatgpt=State()
 chatgptsearch=State()
 chatgpto3 = State()
 

router = Router()

@router.callback_query(F.data == "menu")
async def ru_start(callback: CallbackQuery):
 try:
  await callback.message.edit_text(text=f"Привет, {callback.from_user.first_name}!\n{dict.menu()}", parse_mode="HTML", reply_markup=buttons.ru_menu())
 except Exception as e:
  print(e) 

@router.callback_query(F.data == "chatgpt")
async def chatgpt(callback: CallbackQuery, state: FSMContext):
 try:
  await callback.message.edit_text(text=f"{callback.from_user.first_name}, выбран ChatGPT 4.1. Напишите ваш запрос:")
  await state.set_state(Form.chatgpt)
 except Exception as e:
  print(e)  

@router.callback_query(F.data == "chatgptsearch")
async def chatgpt(callback: CallbackQuery):
 try:
  await callback.message.edit_text(text=f"{callback.from_user.first_name}, выбран ChatGPT 4o mini Search. Напишите ваш запрос:")
 except Exception as e:
  print(e)  

@router.callback_query(F.data == "chatgpto3")
async def chatgpt(callback: CallbackQuery):
 try:
  await callback.message.edit_text(text=f"{callback.from_user.first_name}, выбран ChatGPT o3. Напишите ваш запрос:")
 except Exception as e:
  print(e)      