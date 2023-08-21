from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType
import asyncio
import logging
from core.settings import settings
from core.utils.commands import set_commands
from core.psql import check_user_exists, register_user



async def start_bot(bot: Bot):
    await set_commands(bot)
    await register_user(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот выключен!')


async def start():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - [%(levelname)s] -  %(name)s - "
                                   "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())