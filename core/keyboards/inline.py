from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.middlewares.category import handle_button


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


def inkey_exponse():
    kb = InlineKeyboardBuilder()
    kb.button(text="Продукты", callback_data="Groceries")
    kb.button(text="Дети", callback_data="Children")
    kb.button(text="Кафе и рестораны", callback_data="Cafes and Restaurants")
    kb.button(text="Здоровье и фитнес", callback_data="Health and Fitness")
    kb.button(text="Кварплата", callback_data="Rent")
    kb.button(text="Кредит", callback_data="Credit")
    kb.button(text="Машина", callback_data="Car")
    kb.button(text="Отдых и развлечения", callback_data="Leisure and Entertainment")
    kb.button(text="Подарки", callback_data="Gifts")

    kb.adjust(3, 3, 3)
    return kb.as_markup()