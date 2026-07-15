from typing import List

from fastapi import APIRouter

from app.schemas.product_schema import (
    ProductResponse,
    ProductCreate,
)

from app.services.product_service import (
    get_all_products,
    create_product,
)

router = APIRouter(tags=["Products"])


@router.get(
    "/products",
    response_model=List[ProductResponse]
)
def fetch_products():
    return get_all_products()


@router.post("/products")
def add_product(product: ProductCreate):
    return create_product(product)