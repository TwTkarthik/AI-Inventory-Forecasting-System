from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.purchase_order_schema import PurchaseOrderCreate, PurchaseOrderResponse
from app.services.purchase_order_service import (
    create_purchase_order,
    get_all_purchase_orders,
)

router = APIRouter(tags=["Purchase Orders"])


@router.post(
    "/purchase-orders",
    response_model=PurchaseOrderResponse,
)
def add_purchase_order(
    purchase_order: PurchaseOrderCreate,
    db: Session = Depends(get_db),
):
    return create_purchase_order(db, purchase_order)


@router.get(
    "/purchase-orders",
    response_model=List[PurchaseOrderResponse],
)
def fetch_purchase_orders(db: Session = Depends(get_db)):
    return get_all_purchase_orders(db)
