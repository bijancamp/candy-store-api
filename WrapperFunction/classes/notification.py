import uuid

from account import Account
from notification_type import NotificationType
from order import Order


class Notification:
    def __init__(self, type: NotificationType, order: Order, recipient: Account) -> None:
        self.id = str(uuid.uuid4())
        self.type = type
        self.order = order
        self.recipient = recipient

    def send(self) -> None:
        pass
