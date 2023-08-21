from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio
import logging
from core.settings import settings
from core.utils.commands import set_commands
from core.psql import check_user_exists, on_startup_psql, register_user
from aiogram.filters import Command


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен')


async def req_user(message: Message):
    user_id = message.from_user.id
    async with dp['db'].acquire() as connection:
        user_exists = await check_user_exists(connection, user_id)

        if not user_exists:
            await register_user(connection, user_id, message.from_user.username)
            await message.answer('Вы успешно зарегистрированы')

        else:
            await message.answer('Вы уже зарегестрированы')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот выключен!')


async def start():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - [%(levelname)s] -  %(name)s - "
                                   "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher()

    await on_startup_psql(dp)
    dp.register_message_handler(req_user, Command(commands='requser'))
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())