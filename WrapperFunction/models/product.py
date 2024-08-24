from decimal import Decimal

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str
    price: Decimal

class ProductResponse(ProductBase):
    id: str

class ProductCreate(ProductBase):
    pass
