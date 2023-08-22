from aiogram.types import Message, CallbackQuery
from aiogram import types, Bot, Dispatcher
from aiogram.filters.command import Command
from core.psql import get_user_balance, find_req
from core.keyboards.inline import get_inline_keyboard, inc_exp_trans
from aiogram.types import CallbackQuery
from core.handlres.form import get_inc_trans
from aiogram.fsm.context import FSMContext

dp = Dispatcher()


async def get_inline(message: Message, bot: Bot):
    await message.answer(f"Привет {message.from_user.first_name}. Показываю инлайн кнопки",
                         reply_markup=get_inline_keyboard())


# @dp.message(Command('balance'))
# async def balance_command(message: Message, bot: Bot):
#     await get_user_balance(message, bot)


@dp.message(Command('registration'))
async def registration(message: Message, bot: Bot):
    await find_req(message, bot)


async def select_balance_callback(query: CallbackQuery, bot: Bot):
    user_id = query.from_user.id
    balance = await get_user_balance(query.message, bot, user_id)
    my_balance = f"Ваш текущий баланс: {balance}"
    await query.message.edit_text(my_balance, reply_markup=inc_exp_trans())

    # await query.message.edit_text(f"Ваш текущий баланс: {balance}")
    await query.answer()


async def dohod(message: Message, bot: Bot, state: FSMContext):
    await message.answer(f" {message.from_user.first_name}. Ты выбрал доход",)
    await get_inc_trans(message, state)

