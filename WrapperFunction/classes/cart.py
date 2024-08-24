import uuid

try:
    from product import Product
except ModuleNotFoundError:
    from WrapperFunction.classes.product import Product


class CartItem:
    def __init__(self, product: Product, quantity: int) -> None:
        self.id = str(uuid.uuid4())
        self.product = product
        self.quantity = quantity


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item: CartItem) -> None:
        existing_item = next((x for x in self.items if x.product == item.product), None)

        if existing_item:
            existing_item.quantity += item.quantity
        else:
            self.items.append(item)

    def remove_item(self, item: CartItem) -> None:
        self.items.remove(item)
