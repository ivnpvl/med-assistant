import asyncio
from sqlalchemy import text, make_url
from sqlalchemy.orm import session, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from settings import settings


engine = create_async_engine(
    url=settings.database_URL,
    echo=True,
    pool_size=5,
    max_overflow=10,
)


async def main():
    async with engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        print(f"{res.all()=}")


asyncio.run(main())
