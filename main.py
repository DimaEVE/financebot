from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio
import logging
from core.settings import settings
from core.utils.commands import set_commands
from core.psql import find_req
from aiogram import F
from aiogram.filters import Command
from core.handlres import basic
from core.handlres.basic import get_inline, dohod
from core.handlres.callback import select_balance
from core.psql import get_user_balance
from core.handlres import form
from core.utils.statesform import StepsForm
from core.handlres.basic import select_balance_callback
from core.handlres.callback import inc_trans


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

    dp.message.register(basic.registration, Command(commands='registration'))
    dp.message.register(get_inline, Command(commands='inline'))
    dp.callback_query.register(select_balance_callback, lambda c: c.data == 'select_balance')
    dp.callback_query.register(dohod, F.data.startswith('inc'))
    #dp.callback_query.register(form.get_inc_trans, lambda c: c.data == 'inc_trans')
    #dp.message.register(form.get_inc_trans, F.text == 'Доход')
    dp.message.register(form.get_inc, StepsForm.GET_INC_TRANS)
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    #dp.message.register(basic.balance_command, Command(commands='balance'))
    # dp.callback_query(basic.process_show_balance, lambda c: c.data == 'show_balance')



    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())