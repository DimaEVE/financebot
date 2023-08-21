import asyncpg


async def on_startup_psql(dp):
    db_pool = await asyncpg.create_pool(
        host='37.220.83.23',
        port=5432,
        database='financebot',
        user='postgres',
        password='Flatron1984',
    )

    dp['db'] = db_pool


async def check_user_exists(connection, user_id):
    query = "SELECT COUNT(*) FROM users WHERE user_id = $1"
    result = await connection.fetchval(query, user_id)
    return result > 0


async def register_user(connection, user_id, username):
    query = "INSERT INTO users (user_id, username, balance) VALUES ($1, $2, 0.0)"
    await connection.execute(query, user_id, username)