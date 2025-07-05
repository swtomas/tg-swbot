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
 deepseekr1 = State()
 deepseekv3 = State()
 chatgptimage = State()

router = Router()

@router.callback_query(F.data == "menu")
async def ru_start(callback: CallbackQuery):
 try:
  await callback.message.edit_text(text=f"Привет, {callback.from_user.first_name}!\n{dict.menu()}", parse_mode="HTML", reply_markup=buttons.menu())
 except Exception as e:
  print(e) 

@router.callback_query(F.data == "chatgpt")
async def chatgpt(callback: CallbackQuery, state: FSMContext):
 try:
  await callback.message.edit_text(text=f"{callback.from_user.first_name}, выбран ChatGPT 4.1. Напишите ваш запрос:", reply_markup=buttons.back())
  await state.set_state(Form.chatgpt)
 except Exception as e:
  print(e)  

@router.callback_query(F.data == "chatgptsearch")
async def chatgptsearch(callback: CallbackQuery, state: FSMContext):
 try:
  await callback.message.edit_text(text=f"{callback.from_user.first_name}, выбран ChatGPT 4o mini Search. Напишите ваш запрос:", reply_markup=buttons.back())
  await state.set_state(Form.chatgptsearch) 
 except Exception as e:
  print(e)  

@router.callback_query(F.data == "chatgpto3")
async def chatgpto3(callback: CallbackQuery, state: FSMContext):
 try:
  await callback.message.edit_text(text=f"{callback.from_user.first_name}, выбран ChatGPT o3. Напишите ваш запрос:", reply_markup=buttons.back())
  await state.set_state(Form.chatgpto3)
 except Exception as e:
  print(e)      

@router.callback_query(F.data == "deepseekr1")
async def deepseekr1(callback: CallbackQuery, state: FSMContext):
 try:
  await callback.message.edit_text(text=f"{callback.from_user.first_name}, выбран Deepseek R1. Напишите ваш запрос:", reply_markup=buttons.back())
  await state.set_state(Form.deepseekr1)
 except Exception as e:
  print(e)  

@router.callback_query(F.data == "deepseekv3")
async def deepseekv3(callback: CallbackQuery, state: FSMContext):
 try:
  await callback.message.edit_text(text=f"{callback.from_user.first_name}, выбран Deepseek V3. Напишите ваш запрос:", reply_markup=buttons.back())
  await state.set_state(Form.deepseekv3)
 except Exception as e:
  print(e)  

@router.callback_query(F.data == "chatgptimage")
async def chatgptimage(callback: CallbackQuery, state: FSMContext):
 try:
  await callback.message.edit_text(text=f"{callback.from_user.first_name}, выбран ChatGPT Image. Напишите ваш запрос:", reply_markup=buttons.back())
  await state.set_state(Form.chatgptimage)
 except Exception as e:
  print(e)    