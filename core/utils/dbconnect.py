import asyncpg


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_data(self, user_id, user_name):
        query = f"INSERT INTO users (user_id, username, balance) VALUES ($1, $2, 0.0)"
        await self.connector.execute(query, user_id, user_name)