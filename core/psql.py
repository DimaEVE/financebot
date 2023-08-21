import asyncpg


HOST = '37.220.83.23'
PORT = 5432
DB = 'financebot'
USER = 'postgres'
PSWD = 'Flatron1984'


async def check_user_exists(user_id):
    conn = await asyncpg.connection(user=USER, password=PSWD, da)


async def check_user_exists(connection, user_id):
    query = "SELECT COUNT(*) FROM users WHERE user_id = $1"
    result = await connection.fetchval(query, user_id)
    return result > 0


async def register_user(connection, user_id, username):
    query = "INSERT INTO users (user_id, username, balance) VALUES ($1, $2, 0.0)"
    await connection.execute(query, user_id, username)

