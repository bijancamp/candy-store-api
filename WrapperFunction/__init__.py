import datetime
import fastapi

from .classes.account import Account
from .classes.payment_card import PaymentCard
from .classes.product import ProductCatalog, Product
from .models.account import AccountCheckoutResponse
from .models.product import ProductResponse, ProductCreate


app = fastapi.FastAPI()

# In-memory instance of ProductCatalog for demo purposes
catalog = ProductCatalog()
catalog.add_product(Product(name="Candy Cane", description="A classic peppermint candy cane", price="1.99"))
catalog.add_product(Product(name="Lollipop", description="A sweet lollipop", price="0.99"))
catalog.add_product(Product(name="Gummy Bears", description="A bag of gummy bears", price="3.99"))
catalog.add_product(Product(name="Bubble Gum", description="Chewy bubble gum", price="0.50"))
catalog.add_product(Product(name="Jelly Beans", description="Assorted jelly beans", price="2.50"))


@app.get("/products", response_model=list[ProductResponse])
async def get_products():
    return [
        ProductResponse(
            id=str(product.id),
            name=product.name,
            description=product.description,
            price=product.price
        )
        for product in catalog.products
    ]

@app.post("/products", response_model=ProductResponse)
def add_product(product_data: ProductCreate):
    new_product = Product(
        name=product_data.name,
        description=product_data.description,
        price=product_data.price
    )

    catalog.add_product(new_product)

    return ProductResponse(
        id=str(new_product.id),
        name=new_product.name,
        description=new_product.description,
        price=new_product.price
    )

@app.post("/account/{account_id}/checkout", response_model=AccountCheckoutResponse)
def checkout():
    card = PaymentCard(
        '0123456789012345',
        datetime.date(2026, 1, 1),
        'Willy Wonka',
        '123'
    )

    account = Account(
        name="Willy Wonka",
        email="wonka@wonkaindustries.com",
        account_type="MEMBER",
        payment_card=card
    )

    status = account.checkout()

    return AccountCheckoutResponse(
        status=status
    )
