from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.inventory_schema import InventoryCreate, InventoryResponse
from app.services.inventory_service import create_inventory, get_all_inventory

router = APIRouter(tags=["Inventory"])


@router.get(
    "/inventory",
    response_model=List[InventoryResponse],
)
def fetch_inventory(db: Session = Depends(get_db)):
    return get_all_inventory(db)


@router.post("/inventory")
def add_inventory(
    inventory: InventoryCreate,
    db: Session = Depends(get_db),
):
    return create_inventory(db, inventory)
