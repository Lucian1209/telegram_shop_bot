import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import BotCommand
from app.config import settings
from app.loader import get_bot
from app.handlers import start, catalog, cart, payments

async def on_startup(bot: Bot):
    await bot.set_my_commands([
        BotCommand(command="start", description="Start"),
        BotCommand(command="cart", description="View cart"),
        BotCommand(command="orders", description="My orders"),
    ])
    print("Bot started")

async def main():
    bot = get_bot()
    dp = Dispatcher(storage=RedisStorage.from_url(settings.REDIS_URL))
    dp.include_router(start.router)
    dp.include_router(catalog.router)
    dp.include_router(cart.router)
    dp.include_router(payments.router)

    await on_startup(bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())
