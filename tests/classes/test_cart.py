import pytest

from WrapperFunction.classes.cart import Cart, CartItem
from WrapperFunction.classes.product import Product


def test_add_item_to_cart():
    # Test adding a CartItem to a Cart
    cart = Cart()
    product = Product(name="Jelly Beans", description="Assorted jelly beans", price="2.50")
    item = CartItem(product=product, quantity=1)

    cart.add_item(item)

    assert len(cart.items) == 1
    assert cart.items[0] == item


def test_add_same_item_to_cart():
    # Test adding a CartItem of a product that already exists in the Cart
    cart = Cart()
    product = Product(name="Jelly Beans", description="Assorted jelly beans", price="2.50")
    item1 = CartItem(product=product, quantity=1)
    item2 = CartItem(product=product, quantity=2)

    cart.add_item(item1)
    assert item1.quantity == 1

    cart.add_item(item2)
    assert len(cart.items) == 1
    assert cart.items[0] == item1
    assert cart.items[0].quantity == 3


def test_remove_item_from_cart():
    # Test removing a CartItem from a Cart
    cart = Cart()
    product1 = Product(name="Jelly Beans", description="Assorted jelly beans", price="2.50")
    product2 = Product(name="Gummy Bears", description="A bag of gummy bears", price="3.99")
    item1 = CartItem(product=product1, quantity=1)
    item2 = CartItem(product=product2, quantity=1)

    cart.add_item(item1)
    cart.add_item(item2)
    assert len(cart.items) == 2

    cart.remove_item(item1)
    assert len(cart.items) == 1
    assert cart.items[0] == item2


def test_remove_nonexistent_cart_item():
    # Test attempting to remove a cart item that does not exist in the cart
    cart = Cart()
    product1 = Product(name="Jelly Beans", description="Assorted jelly beans", price="2.50")
    product2 = Product(name="Gummy Bears", description="A bag of gummy bears", price="3.99")
    item1 = CartItem(product=product1, quantity=1)
    item2 = CartItem(product=product2, quantity=1)

    cart.add_item(item1)
    
    with pytest.raises(ValueError):
        cart.remove_item(item2)
