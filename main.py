from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
import asyncio
import logging
import asyncpg
from core.settings import settings
from core.handlres.basic import get_start, get_photo, get_hello, get_location, get_inline, get_balance
from core.filters.iscontact import IsTrueContact
from core.handlres.contact import get_fake_contact, get_true_contact
from core.utils.commands import set_commands
from core.handlres.callback import select_balans
from core.middlewares.dbmiddleware import DbSession
from core.handlres import form
from core.utils.statesform import StepsForm


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен')


async def create_pool():
    return await asyncpg.create_pool(user='postgres', password='Flatron1984', database='financebot',
                                             host='37.220.83.23', port=5432, command_timeout=60)

async def start():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - [%(levelname)s] -  %(name)s - "
                                   "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    pool_connect = await create_pool()

    dp = Dispatcher()
    dp.update.middleware.register(DbSession(pool_connect))
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_hello, F.text == 'Привет')
    dp.message.register(get_true_contact, F.contact, IsTrueContact())
    dp.message.register(get_fake_contact, F.contact)
    dp.message.register(get_location, F.location)
    dp.message.register(get_inline, Command(commands='inline'))
    dp.message.register(get_balance, F.text == 'Баланс')
    dp.callback_query.register(select_balans, F.data.startswith('balans'))
    dp.message.register(form.get_form, Command(commands='form'))
    dp.message.register(form.add_expenses, F.text == 'Расход')
    dp.message.register(form.add_exp_sum, StepsForm.GET_EXP_SUM)
    dp.message.register(form.add_exp_cat, StepsForm.GET_EXP_CAT)
    dp.message.register(form.add_exp_desc, StepsForm.GET_EXP_DESC)
    dp.message.register(form.get_name, StepsForm.GET_NAME)
    dp.message.register(form.get_last_name, StepsForm.GET_LAST_NAME)
    dp.message.register(form.get_age, StepsForm.GET_AGE)


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
