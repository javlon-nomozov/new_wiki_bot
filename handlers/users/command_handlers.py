from googletrans import Translator

from aiogram.types import Message
from aiogram.dispatcher.filters import Command

from data.config import GROUPS
from loader import dp, bot

translator = Translator()


# all commmands
# help - tushunmovchilik bo'lganida batafsil malumot
# /comunity - tushunmovchilik bo'lganida batafsil malumot
# /donate - qo'llab quvvatlovchilar uchun karta raqami
@dp.message_handler(commands="community", state="*")
async def comunity(msg: Message):
    text = translator.translate(text="Taklif va murojatlar uchun Community gruppa").text

    await msg.reply(f"{text}\n<a href='t.me/wiki_tobot_community'>Wikipedia Community</a>")


@dp.message_handler(commands="donate", state="*")
async def donate(msg: Message):
    text = translator.translate(text="Qo'llab quvvatlovchilar uchun:").text

    await msg.reply(f"{text}\nVisa card: 4023 0602 3763 4653\nUnionPay card: 6210 4501 9045 9206")






