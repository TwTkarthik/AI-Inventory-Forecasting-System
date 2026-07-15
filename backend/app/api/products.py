from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

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
def fetch_products(db: Session = Depends(get_db)):
    return get_all_products(db)


@router.post("/products")
def add_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    return create_product(db, product)