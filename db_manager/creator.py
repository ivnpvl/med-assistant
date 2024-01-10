import asyncio
from sqlalchemy import text, make_url
from sqlalchemy.orm import session, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from settings import settings
from models import metadata


engine = create_async_engine(
    url=settings.database_URL,
    echo=True,
    pool_size=5,
    max_overflow=10,
)


async def main():
    async with engine.connect() as conn:
        await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)


asyncio.run(main())
