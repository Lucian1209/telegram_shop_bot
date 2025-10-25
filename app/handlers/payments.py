from aiogram import Router, F
from aiogram.types import Message
from app.services.wayforpay import WayForPayClient

router = Router()

@router.message(F.text == "Checkout")
async def checkout(message: Message):
    # demo: create invoice for total 100
    wfp = WayForPayClient()
    invoice = wfp.create_invoice(order_id='demo-1', amount=100)
    await message.answer(f'Invoice created (demo): {invoice.get("url", "no-url")}')
