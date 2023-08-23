from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


select_finance = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Баланс',
            callback_data='balans'
        )
    ],
    [
        InlineKeyboardButton(
            text='Поступление',
            callback_data='incoming'
        )
    ],
    [
        InlineKeyboardButton(
            text='Расходы',
            callback_data='exponse'
        )
    ],
])


def get_inline_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text="Баланс", callback_data='balans')
    kb.button(text="Поступление", callback_data='incoming')
    kb.button(text="Расходы", callback_data="exponse")

    kb.adjust(1, 2)
    return kb.as_markup()