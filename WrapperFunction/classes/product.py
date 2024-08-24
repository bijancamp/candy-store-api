from __future__ import annotations

import datetime
import uuid


class ProductCatalog:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        self.products.remove(product)


class Product:
    def __init__(self, name: str, description: str, price: str) -> None:
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.price = price
        self.items = []

    def add_item(self, item: ProductItem) -> None:
        self.items.append(item)

    def remove_item(self, item: ProductItem) -> None:
        self.items.remove(item)


class ProductItem:
    def __init__(self, upc: str, expiration: datetime.date, product: Product) -> None:
        self.id = str(uuid.uuid4())
        self.upc = upc
        self.expiration = expiration
        self.product = product
