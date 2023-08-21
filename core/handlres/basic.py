from aiogram import Bot
from aiogram.types import Message
from core.psql import on_startup_psql, check_user_exists, register_user


async def req_user(message: Message, bot: Bot):
    user_id = message.from_user.id
    async with dp['db'].acquire() as connection:
        user_exists = await check_user_exists(connection, user_id)

    if not user_exists:
        await register_user(connection, user_id, message.from_user.username)
        await message.answer('Вы успешно зарегистрированы!')

    else:
        await message.answer('Вы уже зарегистрированы.')

