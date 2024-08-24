import fastapi

from .classes.product import ProductCatalog, Product
from .models.product import ProductResponse, ProductCreate


app = fastapi.FastAPI()

# In-memory instance of ProductCatalog for demo purposes
catalog = ProductCatalog()


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
