from googletrans import Translator

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

# from data.config import CHANNELS, GROUPS
# from keyboards.inline import check_button
# from utils.misc import subscription
from keyboards.inline import settings_keyboard
from loader import dp, db

translator = Translator()


@dp.message_handler(CommandStart(), state="*")
async def start(msg: types.Message):
    user = db.select_user(id=msg.from_user.id)

    if user:
        user_lang = user[3]
        text = translator.translate(text=f'Qadirli {user[1]} siz allaqachon botdan foydalanib boshlagansiz', src='uz',
                                    dest=user_lang).text
        await msg.answer(text=text)
    else:
        lang = msg.from_user.language_code
        if not lang in ['en', 'uz', 'ru']:
            lang = 'en'
        db.add_user(name=msg.from_user.full_name,
                    id=msg.from_user.id,
                    language=lang)
        text = translator.translate(text=f'Salom hurmatli {msg.from_user.mention}', dest=lang, src='uz').text
        await msg.answer(text=text, reply_markup=await settings_keyboard(lang=lang))


# # state="*" /har qaysi state(holatda) ham ishlaydi
# @dp.message_handler(CommandStart(), state="*")
# # @dp.message_handler(commands=['start'], state="*")
# async def show_channels(msg: types.Message):
#     user_lang = msg.from_user.language_code
#     fullname = msg.from_user.full_name
#     text = f"Qadirli {fullname}, bot dan foydalanish uchun bu kannal(lar)ga obuna bo'ling"
#     # await msg.answer(translator.translate(text=text, dest=user_lang).text)
#     channels_format = str()
#     for channel in CHANNELS:
#         chat = await bot.get_chat(channel)
#         invite_link = await chat.export_invite_link()
#         # logging.info(invite_link)
#         channels_format += f"\n👉 <a href='{invite_link}'>[{chat.title}]</a>\n"
#
#     await msg.answer(f"{translator.translate(text=text, dest=user_lang).text} \n"
#                      f"{channels_format}",
#                      reply_markup=check_button,
#                      disable_web_page_preview=True)


#
# @dp.callback_query_handler(text="check_subs", state="*")
# async def checker(call: types.CallbackQuery):
#     await call.answer()
#     result = str()
#     for channel in CHANNELS:
#         status = await subscription.check(user_id=call.from_user.id,
#                                           channel=channel)
#         user_lang = call.from_user.language_code
#         channel = await bot.get_chat(channel)
#         if status:
#             text = translator.translate(text="bu kanalga obuna bo'lgansiz!", dest=user_lang).text
#             invite_link = await channel.export_invite_link()
#             result += f"{text}\n✔<a href='{invite_link}'>{channel.title}</a>\n\n"
#             await call.message.delete()
#         else:
#             text = translator.translate(text="bu kanalga obuna bo'lmagansiz. ", dest=user_lang).text
#             invite_link = await channel.export_invite_link()
#             result += f"{text}\n❌<a href='{invite_link}'>{channel.title}</a> \n\n"
#     await call.message.answer(result, disable_web_page_preview=True)
#
