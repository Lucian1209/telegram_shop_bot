from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from app.keyboards.admin_kb import admin_keyboard
from app.database.session import AsyncSessionLocal
from app.database.models import Product

router = Router()

class AddProduct(StatesGroup):
    name = State()
    description = State()
    price = State()
    photo_url = State()


# Перевірка адміна# Перевірка адміна
@router.message(F.text == "Адмін панель")
async def admin_panel(message: Message):
    kb = admin_keyboard()
    await message.answer("Ласкаво просимо до адмін панелі. Оберіть дію:", reply_markup=kb.as_markup(resize_keyboard=True))

@router.callback_query(F.data == "admin_add")
async def admin_add_product(callback_query, state: FSMContext):
    await callback_query.message.answer("Введіть назву товару:")
    await state.set_state(AddProduct.name)
    await callback_query.answer()

@router.message(AddProduct.name)
async def add_product_description(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введіть опис товару:")
    await state.set_state(AddProduct.description)

@router.message(AddProduct.description)
async def add_product_price(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Введіть ціну товару:")
    await state.set_state(AddProduct.price)

@router.message(AddProduct.price)
async def add_product_photo_url(message: Message, state: FSMContext):
    await state.update_data(price=float(message.text))
    await message.answer("Введіть URL фото товару:")
    await state.set_state(AddProduct.photo_url)

@router.message(AddProduct.photo_url)
async def process_photo(message: Message, state: FSMContext):
    data = await state.get_data()
    async with AsyncSessionLocal() as session:
        product = Product(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            photo_url=message.text
        )
        session.add(product)
        await session.commit()
    await message.answer(f"✅ Товар '{data['name']}' додано!")
    await state.clear()