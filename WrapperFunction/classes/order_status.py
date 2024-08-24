from enum import Enum


class OrderStatus(Enum):
    ORDERED = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELED = 4
