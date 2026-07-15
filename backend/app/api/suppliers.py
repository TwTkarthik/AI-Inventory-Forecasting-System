from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.supplier_schema import (
    SupplierCreate,
    SupplierResponse,
)

from app.services.supplier_service import (
    create_supplier,
    get_all_suppliers,
)

router = APIRouter(tags=["Suppliers"])


@router.get(
    "/suppliers",
    response_model=List[SupplierResponse]
)
def fetch_suppliers(db: Session = Depends(get_db)):
    return get_all_suppliers(db)


@router.post("/suppliers")
def add_supplier(
    supplier: SupplierCreate,
    db: Session = Depends(get_db)
):
    return create_supplier(db, supplier)