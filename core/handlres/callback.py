from aiogram import Bot, Dispatcher
from aiogram.types import CallbackQuery, Message
from core.psql import get_user_balance


async def select_balance(call: CallbackQuery):
    answer = await get_user_balance(call.message, call.from_user.id)
    await call.message.answer(answer)
    await call.answer()


# async def inc_trans(callback_query: CallbackQuery):
#     await callback_query.answer(f"ВВедите сумму дохода:")


async def inc_trans(call: CallbackQuery, bot: Bot):
    answer = f'Ты выбрал доход'
    await call.message.answer(answer)
    await call.answer()
