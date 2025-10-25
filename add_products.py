import asyncio
from app.database.session import AsyncSessionLocal
from app.database.models import Product

async def add_products():
    async with AsyncSessionLocal() as session:
        products = [
            Product(
                name="PixelPilot футболка",
                description="Стильна футболка з логотипом PixelPilot.",
                price=499.0,
                photo_url="https://upload.wikimedia.org/wikipedia/commons/1/11/Test-Logo.svg",
            ),
            Product(
                name="PixelPilot кепка",
                description="Кепка з логотипом PixelPilot.",
                price=299.0,
                photo_url="https://upload.wikimedia.org/wikipedia/commons/1/11/Test-Logo.svg",
            ),
        ]
        session.add_all(products)
        await session.commit()

asyncio.run(add_products())
