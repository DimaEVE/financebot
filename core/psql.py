import asyncpg
from aiogram import Bot
from aiogram.types import Message

async def connect_to_db():
    db_params = {
        'host': '37.220.83.23',
        'port': 5432,
        'database': 'financebot',
        'user': 'postgres',
        'password': 'Flatron1984'
    }

    db_pool = await asyncpg.create_pool(**db_params)
    return db_pool

async def check_user_exists(connection, user_id):
    query = "SELECT COUNT(*) FROM users WHERE user_id = $1"
    result = await connection.fetchval(query, user_id)
    return result > 0

async def register_user(connection, user_id, username):
    query = "INSERT INTO users (user_id, username, balance) VALUES ($1, $2, 0.0)"
    await connection.execute(query, user_id, username)


async def find_req(message: Message, bot: Bot):
    db_pool = await connect_to_db()

    async with db_pool.acquire() as connection:
        username = message.from_user.first_name
        user_id = message.from_user.id
        user_exists = await check_user_exists(connection, user_id)

        if not user_exists:
            await register_user(connection, user_id, username)
            await bot.send_message(message.chat.id, f"Вы успешно зарегистрированы под номером {user_id}.")
            print("Пользователь успешно зарегистрирован!")

        else:
            await bot.send_message(message.chat.id, f"Пользователь уже зарегистрирован.")
            print("Пользователь уже зарегистрирован.")

    await db_pool.close()


async def get_user_balance(message: Message, bot: Bot):
    db_pool = await connect_to_db()
    async with db_pool.acquire() as connection:
        user_id = message.from_user.id
        query = "SELECT balance FROM users WHERE user_id = $1"
        balance = await connection.fetchval(query, user_id)
        await bot.send_message(message.chat.id, f"Ваш текущий баланс: {balance}")
    await db_pool.close()



