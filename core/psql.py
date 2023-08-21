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
            await  register_user(connection, user_id, username)
            print("Пользователь успешно зарегистрирован!")

        else:
            print("Пользователь уже зарегистрирован.")

    await db_pool.close()


async def find(message: Message, bot: Bot):
    user_name = message.from_user.first_name
    user_id = message.from_user.id

