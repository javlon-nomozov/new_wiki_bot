import logging
from googletrans import Translator

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
translator = Translator()


async def create_def_key(titles, lang: str):
    key = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    key.insert(KeyboardButton(text=f"❌ Cancel"))
    for title in titles:
        key.insert(KeyboardButton(text=title))
    return key



