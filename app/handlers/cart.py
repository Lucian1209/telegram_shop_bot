from aiogram import Router, F
from aiogram.types import Message


router = Router()

# Very small in-memory cart example (not persistent)
CARTS = {}

@router.message(F.text == "Cart")
async def show_cart(message: Message):
    chat_id = message.chat.id
    cart = CARTS.get(chat_id, [])
    if not cart:
        await message.answer("Кошик порожній.")
        return
    lines = []
    total = 0
    for item in cart:
        lines.append(f"{item['name']} — {item['price']} UAH")
        total += item['price']
    lines.append(f"\nTotal: {total} UAH")
    await message.answer("\n".join(lines))

# Add command to add a demo item
@router.message(F.text.startswith("add "))
async def add_to_cart(message: Message):
    try:
        _, pid = message.text.split(maxsplit=1)
        pid = int(pid)
    except Exception:
        await message.answer("Вкажи id товару, наприклад: add 1")
        return
    prod = next((p for p in [{"id":1,"name":"T-Shirt","price":199},{"id":2,"name":"Mug","price":99}] if p['id']==pid), None)
    if not prod:
        await message.answer("Товар не знайдено")
        return
    cart = CARTS.setdefault(message.chat.id, [])
    cart.append(prod)
    await message.answer(f"Додано: {prod['name']}")
