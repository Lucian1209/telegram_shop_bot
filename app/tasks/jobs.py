from .celery_app import celery_app

@celery_app.task
def send_order_notification(order_id: int, chat_id: int, text: str):
    # Placeholder for sending notifications
    print(f"Notify {chat_id} about order {order_id}: {text}")
