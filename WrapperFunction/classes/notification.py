import uuid

from enum import Enum

from account import Account
from notification import NotificationType
from order import Order


class NotificationType(Enum):
    ORDERED = 1
    SHIPPED = 2


class Notification:
    def __init__(self, type: NotificationType, order: Order, recipient: Account) -> None:
        self.id = str(uuid.uuid4())
        self.type = type
        self.order = order
        self.recipient = recipient

    def send(self) -> None:
        pass
