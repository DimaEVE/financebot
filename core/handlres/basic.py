from aiogram import Bot
from aiogram.types import Message
import json
from core.keyboards.reply import get_reply_keyboard
from core.keyboards.inline import select_finance, get_inline_keyboard
from core.utils.dbconnect import Request


async def get_inline(message: Message, bot: Bot):
    await message.answer(f"Привет, {message.from_user.first_name}. Показываю инлайн клавиатуру.",
                         reply_markup=get_inline_keyboard())


async def get_start(message: Message, bot: Bot, request: Request):
    await request.add_data(message.from_user.id, message.from_user.first_name)
    await message.answer(f'Привет <b>{message.from_user.first_name}</b>. Рад тебя видеть!',
                         reply_markup=get_reply_keyboard())


async def get_balance(message: Message, bot: Bot, request: Request):
    await message.answer(f'<b>{message.from_user.first_name}</b>, считаю баланс...')
    balance = await request.get_user_balance(message.from_user.id)
    await message.answer(f'Ваш баланс: {balance}')



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