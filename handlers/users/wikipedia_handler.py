import logging
import wikipedia
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from googletrans import Translator

from aiogram import types

from data.config import GROUPS
from states.wikisearch_state import Wiki_states
from loader import dp, db, bot

from keyboards.default.wiki_themes_defolt import create_def_key

translator = Translator()


@dp.message_handler()
async def wiki(msg: types.Message, state: FSMContext):

    
    user = db.select_user(id=msg.from_user.id)
    lang = user[3]

    wikipedia.set_lang(lang)
    try:
        wiki_query = wikipedia.search(msg.text)
    except TypeError as err:
        wiki_query = []
        user = msg.from_user
        mention = user.get_mention()
        user_lang = lang
        query_lang = lang
        await msg.reply(translator.translate(text="bu til bilan ulanishda muammo bor:", dest=lang).text + lang)

        bot.send_message(GROUPS[0],
                         text=f"user: {mention}\ntype_error: {err}\nso'rov tili borasida muammo\nuser_lang {user_lang}\nquery_lang:{query_lang}")

    if not wiki_query == []:
        wiki_query = wikipedia.search(msg.text)
        key = await create_def_key(wiki_query, lang=lang)
        message = translator.translate(text="mavzulardan birini tanlang", dest=lang).text
        await msg.reply(message, reply_markup=key)
        await Wiki_states.w_theme.set()
    else:
        # lang = msg.from_user.language_code
        await msg.reply(translator.translate(text="Bunga o'xshash mavzu topilmadi", dest=lang).text)
    


@dp.message_handler(state=Wiki_states.w_theme)
async def w_search(msg: types.Message, state: FSMContext):
    
    user = db.select_user(id=msg.from_user.id)
    user_lang = user[3]
    wikipedia.set_lang(user_lang)

    if msg.text == "❌ Cancel":
        await msg.reply(translator.translate(text="Canceled", dest=user_lang).text, reply_markup=ReplyKeyboardRemove())
        await state.finish()
        # return
    

    try:
        result = wikipedia.summary(msg.text)
    except:
        result = translator.translate(text="Bunday malumot topilmadi", dest=user_lang).text
    describtion = translator.translate("bu bot yordamida har qaysi tildagi malumotlarni topishingiz mumkin",
                                       dest=user_lang).text

    # await msg.reply(f"{result}\n\n<a href='t.me/wikipedia_tobot'>Wikipedia Bot</a>\n{describtion}",
    # reply_markup=ReplyKeyboardRemove())

    text2 = ''
    n = 1
    n2 = 1
    for char in result:
        text2 += char
        if (n / 4000) in range(30):
            await msg.reply(f"{text2}\n\n<a href='t.me/wikipedia_tobot'>Wikipedia Bot</a>\n{describtion}")
            print(f"{n2} - paragraph")
            text2 = ''
            n2 += 1
        n += 1
    await msg.reply(f"{text2}\n\n<a href='t.me/wikipedia_tobot'>Wikipedia Bot</a>\n{describtion}",
                    reply_markup=ReplyKeyboardRemove())

    await state.finish()
