from aiogram.filters.callback_data import CallbackData


class TranInfo(CallbackData, prefix='trans'):
    bal: int
    trans: str
    cat: str
    date: int