from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio
import logging
from core.settings import settings
from core.utils.commands import set_commands
from core.psql import find_req
from aiogram import F
from aiogram.filters import Command


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот выключен!')


async def start():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - [%(levelname)s] -  %(name)s - "
                                   "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher()

    dp.message.register(find_req, F.text == 'user')
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())