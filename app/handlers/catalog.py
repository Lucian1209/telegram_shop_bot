from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from app.keyboards.products_kb import products_keyboard as catalog_kb
from app.services.products import get_products

router = Router()

# Simple static demo catalog

@router.message(F.text == "Catalog")
async def show_catalog(message: Message):
    products = await get_products(page=1)
    if not products:
        await message.answer("Каталог порожній 😢")
        return

    for product in products:
        text = f"<b>{product.name}</b>\n{product.description}\n💰 Ціна: {product.price:.2f} грн"
        await message.answer_photo(
            photo=product.photo_url,
            caption=text,
            reply_markup=catalog_kb(product.id, page=1).as_markup(),
        )

    await message.answer("Сторінка 1", reply_markup=catalog_kb(page=1).as_markup())
