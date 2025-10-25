from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Catalog")],
            [KeyboardButton(text="Cart"), KeyboardButton(text="Orders")],
        ],
        resize_keyboard=True,
        one_time_keyboard=False,
    )
    return keyboard