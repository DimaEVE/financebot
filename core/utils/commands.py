from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='balance',
            description='Проверить баланс'
        ),
        BotCommand(
            command='registration',
            description='Регистрация'
        ),
        BotCommand(
            command='inline',
            description='Показать кнопки'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
