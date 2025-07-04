from aiogram import Router,F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import dict
import buttons

router = Router()

@router.callback_query(F.data == "lang_ru")
async def ru_start(callback: CallbackQuery):
 try:
  await callback.message.edit_text(text=f"Привет, {callback.from_user.first_name}!\n{dict.ru_menu()}", parse_mode="HTML", reply_markup=buttons.ru_menu()) # type: ignore
 except Exception as e:
  print(e) 