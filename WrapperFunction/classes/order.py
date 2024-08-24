import datetime
import uuid

from decimal import Decimal

from order_status import OrderStatus
from product import ProductItem


class Order:
    def __init__(self, order_number: str, order_date: datetime.date, total_amount: Decimal, items: list[ProductItem], status: OrderStatus) -> None:
        self.id = str(uuid.uuid4())
        self.order_number = order_number
        self.order_date = order_date
        self.total_amount = total_amount
        self.items = items
        self.status = status

    def cancel(self) -> None:
        pass
