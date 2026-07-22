from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class PurchaseOrderItemCreate(BaseModel):
    product_id: UUID
    quantity: int
    unit_price: Decimal


class PurchaseOrderCreate(BaseModel):
    supplier_id: UUID
    expected_delivery: Optional[datetime] = None
    items: List[PurchaseOrderItemCreate]


class PurchaseOrderItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    item_id: UUID
    product_id: UUID
    quantity: int
    unit_price: Decimal


class PurchaseOrderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    purchase_order_id: UUID
    supplier_id: UUID
    supplier_name: str
    order_date: datetime
    expected_delivery: Optional[datetime] = None
    status: str
    items: List[PurchaseOrderItemResponse]
