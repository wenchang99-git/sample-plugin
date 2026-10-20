
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Product(BaseModel):
    product_id: str
    name: str
    category: str
    in_stock: bool

app = FastAPI(
    title="Sample Product Plugin",
    description="A sample product lookup API for AI assistants",
    version="1.0.0"
)

# Sample product database
products = {
    "A5093": {
        "product_id": "A5093",
        "name": "Sample Energy Drink",
        "category": "Supplement",
        "in_stock": True
    },
    "P1001": {
        "product_id": "P1001",
        "name": "Sample Protein Powder",
        "category": "Nutrition",
        "in_stock": False
    }
}


@app.get("/")
def home():
    return {
        "message": "Sample Plugin API is running",
        "version": "1.0.0"
    }


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: str):
    product = products.get(product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product

@app.get("/products", response_model=list[Product])
def list_products():
    return list(products.values())
