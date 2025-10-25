from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def products_keyboard(product_id: int, page: int) -> InlineKeyboardBuilder:
    kb = InlineKeyboardBuilder()
    
    kb.button(
        text="Buy Now",
        callback_data=f"buy:{product_id}"
    )
    
    kb.button(
        text="Add to Cart",
        callback_data=f"add_to_cart:{product_id}"
    )
    
    nav_buttons = []
    if page > 1:
        nav_buttons.append(
            InlineKeyboardButton(
                text="Previous",
                callback_data=f"products_page:{page - 1}"
            )
        )
    nav_buttons.append(
        InlineKeyboardButton(
            text="Next",
            callback_data=f"products_page:{page + 1}"
        )
    )    
    kb.row(*nav_buttons)
    
    return kb

