from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.psql import get_user_balance
from core.handlres.callback import select_balance


def get_inline_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text="Баланс", callback_data='select_balance')
    return kb.as_markup()


def inc_exp_trans():
    kb = InlineKeyboardBuilder()
    kb.button(text="Доход", callback_data='inc_trans')
    kb.button(text="Расход", callback_data='exp_trans')
    return kb.as_markup()

