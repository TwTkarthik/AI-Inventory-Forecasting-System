from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class InventoryCreate(BaseModel):
    product_id: UUID
    quantity_on_hand: int = Field(default=0)
    reserved_quantity: int = Field(default=0)
    reorder_level: int = Field(default=10)
    warehouse_location: Optional[str] = None


class InventoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    inventory_id: UUID
    product_id: UUID
    product_name: str
    quantity_on_hand: int
    reserved_quantity: int
    reorder_level: int
    warehouse_location: Optional[str] = None
    last_stock_update: Optional[datetime] = None