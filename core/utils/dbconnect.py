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


    async def add_expense(self, user_id, summa, category, desc):
        expense_query = """INSERT INTO transactions (user_id, amount, category_id, description) 
        VALUES ($1, $2, $3, $4) RETURNING amount"""
        balance_query = """UPDATE users SET balance = balance - $1 WHERE user_id = $2"""
        async with self.connector.transaction():
            amount = await self.connector.fetchval(expense_query, user_id, summa, category, desc)
            await self.connector.execute(balance_query, amount, user_id)
        print(f'Расход добавлен в БД: {summa}')
        query = "SELECT balance FROM users WHERE user_id = $1"
        new_balance = await self.connector.fetchval(query, user_id)
        return new_balance

    # async def add_expense(self, user_id, summa, category, desc):
    #     query = "INSERT INTO transactions (user_id, amount, category_id, description) VALUES ($1, $2, $3, $4)"
    #     await self.connector.execute(query, user_id, summa, category, desc)
    #     print(f'Расход добавлен в БД: {summa}')
    #     query = "SELECT balance FROM users WHERE user_id = $1"
    #     result = await self.connector.fetchval(query, user_id)
    #     calculation = int(result) - int(summa)
    #     query = "UPDATE users SET balance = $1 WHERE user_id = $2"
    #     await self.connector.execute(query, calculation, user_id)


