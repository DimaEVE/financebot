from aiogram import Bot
from aiogram.types import Message
import json
from core.keyboards.reply import reply_keyboard, loc_tel_poll_keyboard, get_reply_keyboard


async def get_start(message: Message, bot: Bot):
    #await bot.send_message(message.from_user.id, f'<b>Привет {message.from_user.first_name}. Рад тебя видеть!</b>')
    await message.answer(f'<s>Привет {message.from_user.first_name}. Рад тебя видеть!</s>',
                         reply_markup=get_reply_keyboard())
    #await message.reply(f'<tg-spoiler>Привет {message.from_user.first_name}. Рад тебя видеть!</tg-spoiler>')


async def get_photo(message: Message, bot: Bot):
    await message.answer(f"Отлично ты отправил картинку, сохраним ее")
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')


async def get_hello(message: Message, bot: Bot):
    await message.answer(f"И тебе привет")
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)


async def get_location(message: Message, bot: Bot):
    await message.answer(f"Ты отправил локацию!\r\a {message.location.latitude}\r\n{message.location.longitude}")