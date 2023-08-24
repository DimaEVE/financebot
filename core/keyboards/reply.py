from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_reply_keyboard():
    kb = ReplyKeyboardBuilder()
    kb.button(text='Баланс')
    kb.button(text='Кнопка 2')
    kb.button(text='Кнопка 3')
    kb.button(text='Отправить геолокацию', request_location=True)
    kb.button(text='Отправить контакт', request_contact=True)
    kb.adjust(2, 2, 1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Отправь свои данные")


