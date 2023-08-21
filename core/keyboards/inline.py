from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


select_balance = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Баланс',
            callback_data='узнать баланс'
        )
    ]
])