from typing import Optional, Iterable

from asyncpg import create_pool, Pool
from config import conf
from loguru import logger


class Database:
    def __init__(self, user, passwd, name, port=5432, host='localhost') -> None:
        self.user = user
        self.passwd = passwd
        self.name = name
        self.host = host
        self.port = port
        self.pool: Optional[Pool] = None

    async def connect(self) -> None:
        self.pool = await create_pool(
            user=self.user,
            password=self.passwd,
            database=self.name,
            host=self.host,
            port=self.port
        )
        logger.success('🟢 successfully connected!')

    async def execute_multiple(self, *queries: Iterable) -> None:
        """executes multiple queries at once"""
        for query in queries:
            await self.pool.execute(query)

    async def exists(self, field: str, value: str, table: str) -> None:
        query = f'select {field} from {table} where {field}=$1 limit 1'
        return not not await self.pool.fetchval(query, value)

    async def close(self, dp=None) -> None:
        await self.pool.close()
        logger.info('🔴 successfully disconnected')


db = Database(**conf.db.asdict())