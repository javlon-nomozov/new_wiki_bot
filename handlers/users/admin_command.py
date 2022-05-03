import asyncio

from aiogram.types import Message

from filters.admins_filter import BotAdminFilter
from loader import dp, bot, db


@dp.message_handler(BotAdminFilter(), commands='send_ad', commands_prefix='$')
async def send_ad(msg: Message):

    src_msg = msg.reply_to_message
    #
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        try:
            audio = src_msg.audio.file_id
            caption = src_msg.caption
            await bot.send_message(chat_id=user_id, audio=audio, caption=caption)
        except:
            pass
        try:
            video = src_msg.video.file_id
            caption = src_msg.caption
            await bot.send_message(chat_id=user_id, video=video, caption=caption)
        except:
            pass
        try:
            photo = src_msg.photo[-1].file_id
            caption = src_msg.caption
            await bot.send_message(chat_id=user_id, photo=photo, caption=caption)
        except:
            pass
        try:
            voice = src_msg.voice.file_id
            caption = src_msg.caption
            await bot.send_message(chat_id=user_id, voice=voice, caption=caption)
        except:
            pass
        try:
            document = src_msg.document.file_id
            caption = src_msg.caption
            await bot.send_message(chat_id=user_id, document=document, caption=caption)
        except:
            pass
        try:
            latitude = src_msg.location.latitude
            longitude = src_msg.location.longitude
            await bot.send_message(chat_id=user_id, latitude=latitude, longitude=longitude)
        except:
            pass
        try:
            await bot.send_message(chat_id=user_id, text=src_msg.text)
        except:
            pass
        await asyncio.sleep(0.05)
    await msg.reply(text='Xabar muvaffaqqiyatli tarqatildi🤩')





