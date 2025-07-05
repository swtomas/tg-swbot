from aiogram.utils.keyboard import InlineKeyboardBuilder

def start_buttons():
    builder = InlineKeyboardBuilder()
    builder.button(text="🇷🇺 Русский", callback_data="lang_ru")
    builder.button(text="🇬🇧 English", callback_data="lang_en")
    builder.adjust(1,1)
    return builder.as_markup()

def ru_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="👁️ ChatGPT 4.1", callback_data="chatgpt")
    builder.button(text="🔍 ChatGPT Search", callback_data="chatgptsearch")
    builder.button(text="🧐 ChatGPT o3", callback_data="chatgpt03")
    builder.button(text="🤖 Deepseek R1", callback_data="deepseekr1")
    builder.button(text="🐟 Deepseek V3", callback_data="deepseekv3")
    builder.adjust(2,1,2)
    return builder.as_markup()

def back():
    builder = InlineKeyboardBuilder()
    builder.button(text="◀️ К другим моделям", callback_data="menu")
    builder.adjust(1,1)
    return builder.as_markup()

