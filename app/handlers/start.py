from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from app.keyboards.main_menu import main_menu_keyboard

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    
    text = (
        "Вітаю! Це тестовий магазин.\n"
        "Використовуй меню, щоб переглянути каталог або кошик."
    )
    await message.answer(text, reply_markup=main_menu_keyboard())
