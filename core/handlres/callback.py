from aiogram import Bot
from aiogram.types import CallbackQuery


async def select_balans(call: CallbackQuery, bot: Bot):
    answer = f'ты выбрал нажать на кнопку!'
    await call.message.answer(answer)
    await call.answer()