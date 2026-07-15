from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


class SupplierResponse(BaseModel):
    supplier_id: UUID
    supplier_name: str
    contact_person: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    address: Optional[str]
    lead_time_days: int
    created_at: datetime

    class Config:
        from_attributes = True


class SupplierCreate(BaseModel):
    supplier_name: str
    contact_person: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    lead_time_days: int = 0