from sqlalchemy.future import select
from app.database.session import AsyncSessionLocal
from app.database.models import Product

async def get_products(page: int = 1, per_page: int = 10):
    offset = (page - 1) * per_page
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Product).offset(offset).limit(per_page)
        )
        products = result.scalars().all()  
    return products

async def get_product_by_id(product_id: int):
     async with AsyncSessionLocal() as session:
        result = await session.execute(select(Product).where(Product.id == product_id))
        return result.scalar_one_or_none()