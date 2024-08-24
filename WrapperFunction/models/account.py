from decimal import Decimal

from pydantic import BaseModel

from ..classes.order import OrderStatus


class AccountCheckoutBase(BaseModel):
    status: OrderStatus

class AccountCheckoutResponse(AccountCheckoutBase):
    pass
