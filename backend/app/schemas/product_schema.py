from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


class ProductResponse(BaseModel):
    product_id: UUID
    sku: str
    mpn: Optional[str]
    product_name: str
    brand: Optional[str]
    category: Optional[str]
    description: Optional[str]
    selling_price: float
    cost_price: float
    barcode: Optional[str]
    unit: str
    lead_time_days: int
    weight: Optional[float]
    length: Optional[float]
    width: Optional[float]
    height: Optional[float]
    primary_image: Optional[str]
    status: str
    status_reason: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        
class ProductCreate(BaseModel):
    sku: str
    mpn: str | None = None
    product_name: str
    brand: str | None = None
    category: str | None = None
    description: str | None = None
    selling_price: float
    cost_price: float
    barcode: str | None = None
    unit: str
    lead_time_days: int = 0
    weight: float | None = None
    length: float | None = None
    width: float | None = None
    height: float | None = None
    primary_image: str | None = None
    status: str = "ACTIVE"