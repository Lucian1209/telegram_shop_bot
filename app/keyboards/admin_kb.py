from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def admin_keyboard() -> ReplyKeyboardBuilder:
    kb = ReplyKeyboardBuilder()
    
    kb.button(
        text="➕ Додати товар", 
        callback_data="admin_add"
        )
    kb.button(
        text="📝 Список товарів",
        callback_data="admin_list"
        )
    
    return kb
        