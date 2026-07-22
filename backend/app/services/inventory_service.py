from sqlalchemy.orm import Session, joinedload

from app.models.inventory_model import Inventory


def get_all_inventory(db: Session):
    inventory_items = db.query(Inventory).options(joinedload(Inventory.product)).all()

    response = []

    for item in inventory_items:
        response.append({
            "inventory_id": item.inventory_id,
            "product_id": item.product_id,
            "product_name": item.product.product_name if item.product else None,
            "quantity_on_hand": item.quantity_on_hand,
            "reserved_quantity": item.reserved_quantity,
            "reorder_level": item.reorder_level,
            "warehouse_location": item.warehouse_location,
            "last_stock_update": item.last_stock_update,
        })

    return response


def create_inventory(db: Session, inventory):
    new_inventory = Inventory(
        product_id=inventory.product_id,
        quantity_on_hand=inventory.quantity_on_hand,
        reserved_quantity=inventory.reserved_quantity,
        reorder_level=inventory.reorder_level,
        warehouse_location=inventory.warehouse_location,
    )

    db.add(new_inventory)
    db.commit()
    db.refresh(new_inventory)

    return {
        "message": "Inventory created successfully ✅"
    }
