import asyncio
from app.database.session import engine, Base
from app.database import models

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(init_db())
print("Database created")