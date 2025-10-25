from aiogram import Bot
from app.config import settings

bot: Bot | None = None

def get_bot() -> Bot:
    global bot
    if bot is None:
        bot = Bot(token=settings.BOT_TOKEN)
    return bot
