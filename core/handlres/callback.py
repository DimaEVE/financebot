from aiogram import Bot, Dispatcher
from aiogram.types import CallbackQuery, Message
from core.psql import get_user_balance


async def select_balance(callback_query: CallbackQuery):
    answer = await get_user_balance(callback_query.message, callback_query.from_user.id)
    await callback_query.message.answer(answer)
    await callback_query.answer()


async def inc_trans(callback_query: CallbackQuery):
    await callback_query.answer(f"ВВедите сумму дохода:")

