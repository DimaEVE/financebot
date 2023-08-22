from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsForm


async def get_inc_trans(message: Message, state: FSMContext):
    await message.answer(f'<<<Введите сумму дохода:>>>')
    await state.set_state(StepsForm.GET_INC_TRANS)


async def get_inc(message: Message):
    await message.answer(f'Вы указали сумму дохода: \r\n{message}\r\n.')