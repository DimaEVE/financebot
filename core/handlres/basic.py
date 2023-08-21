from aiogram import Bot
from aiogram.types import Message
from aiogram import types, Bot, Dispatcher
from aiogram.filters.command import Command
from core.psql import get_user_balance, find_req


dp = Dispatcher()


# async def req_user(message: Message, bot: Bot):
#     user_id = message.from_user.id
#     async with dp['db'].acquire() as connection:
#         user_exists = await check_user_exists(connection, user_id)
#
#     if not user_exists:
#         await register_user(connection, user_id, message.from_user.username)
#         await message.answer('Вы успешно зарегистрированы!')
#
#     else:
#         await message.answer('Вы уже зарегистрированы.')


@dp.message(Command('balance'))
async def balance_command(message: Message, bot: Bot):
    await get_user_balance(message, bot)


@dp.message(Command('registration'))
async def registration(message: Message, bot: Bot):
    await find_req(message, bot)

