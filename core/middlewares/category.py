from aiogram.types import Message

#Категории расходов
async def handle_button(message: Message):
    await message.answer(f"Вы выбрали категорию: ")


