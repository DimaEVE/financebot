import asyncpg


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_data(self, user_id, user_name):
        query = f"INSERT INTO users (user_id, username, balance) VALUES ($1, $2, 0.0)"
        try:
            await self.connector.execute(query, user_id, user_name)
        except:
            print("Пользователь уже существует")

    async def get_user_balance(self, user_id):
        query = "SELECT balance FROM users WHERE user_id = $1"
        result = await self.connector.fetchval(query, user_id)
        return result
