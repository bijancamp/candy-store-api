import datetime
import pytest

from WrapperFunction.classes.product import ProductCatalog, Product, ProductItem


def test_add_product_to_catalog():
    # Test adding a Product to the ProductCatalog
    catalog = ProductCatalog()
    product = Product(name="Candy Cane", description="A classic peppermint candy cane", price="1.99")
    
    catalog.add_product(product)

    assert len(catalog.products) == 1
    assert catalog.products[0] == product


def test_remove_product_from_catalog():
    # Test removing a Product from the ProductCatalog
    catalog = ProductCatalog()
    product1 = Product(name="Lollipop", description="A sweet lollipop", price="0.99")
    product2 = Product(name="Gummy Bears", description="A bag of gummy bears", price="3.99")
    
    catalog.add_product(product1)
    catalog.add_product(product2)
    assert len(catalog.products) == 2

    catalog.remove_product(product1)
    assert len(catalog.products) == 1
    assert catalog.products[0] == product2


def test_remove_nonexistent_product():
    # Test attempting to remove a product that does not exist in the catalog
    catalog = ProductCatalog()
    product1 = Product(name="Bubble Gum", description="Chewy bubble gum", price="0.50")
    product2 = Product(name="Jelly Beans", description="Assorted jelly beans", price="2.50")
    
    catalog.add_product(product1)

    with pytest.raises(ValueError):
        catalog.remove_product(product2)


def test_add_item_to_product():
    # Test adding a ProductItem to a Product
    product = Product(name="Bubble Gum", description="Chewy bubble gum", price="0.50")
    item = ProductItem(upc="012345678905", expiration=datetime.date(2024, 12, 31), product=product)

    product.add_item(item)

    assert len(product.items) == 1
    assert product.items[0] == item


def test_remove_item_from_product():
    # Test removing a ProductItem from a Product
    product = Product(name="Jelly Beans", description="Assorted jelly beans", price="2.50")
    item1 = ProductItem(upc="193914919193", expiration=datetime.date(2024, 12, 15), product=product)
    item2 = ProductItem(upc="934139834911", expiration=datetime.date(2024, 11, 30), product=product)

    product.add_item(item1)
    product.add_item(item2)
    assert len(product.items) == 2

    product.remove_item(item1)
    assert len(product.items) == 1
    assert product.items[0] == item2


def test_remove_nonexistent_product_item():
    # Test attempting to remove a product item that does not exist in a product
    product = Product(name="Jelly Beans", description="Assorted jelly beans", price="2.50")
    item1 = ProductItem(upc="193914919193", expiration=datetime.date(2024, 12, 15), product=product)
    item2 = ProductItem(upc="934139834911", expiration=datetime.date(2024, 11, 30), product=product)
    
    product.add_item(item1)

    with pytest.raises(ValueError):
        product.remove_item(item2)
