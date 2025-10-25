import hmac
import hashlib
from typing import Dict

from app.config import settings

class WayForPayClient:
    def __init__(self, merchant=None, secret=None):
        self.merchant = merchant or settings.WAYFORPAY_MERCHANT
        self.secret = secret or settings.WAYFORPAY_SECRET

    def create_invoice(self, order_id: str, amount: int) -> Dict:
        # Return demo payload (in real life do HTTP POST to WayForPay)
        payload = {
            "order": order_id,
            "amount": amount,
            "currency": "UAH",
            "merchant": self.merchant,
            "url": "https://pay.wayforpay.com/demo"  # placeholder
        }
        # create signature example
        signature = self._sign([str(payload['merchant']), str(payload['order']), str(payload['amount'])])
        payload['signature'] = signature
        return payload

    def _sign(self, parts):
        data = ';'.join(parts)
        return hmac.new(self.secret.encode('utf-8'), data.encode('utf-8'), hashlib.sha256).hexdigest()

    def verify_callback(self, data: Dict, signature: str) -> bool:
        # Implement verification based on WFP docs - placeholder
        computed = self._sign([data.get('merchant', ''), data.get('order', ''), str(data.get('amount', ''))])
        return computed == signature
