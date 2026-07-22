from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload

from app.models.purchase_order_item_model import PurchaseOrderItem
from app.models.purchase_order_model import PurchaseOrder
from app.models.supplier_model import Supplier
from app.schemas.purchase_order_schema import PurchaseOrderCreate


def create_purchase_order(db: Session, purchase_order: PurchaseOrderCreate):
    # Validate supplier
    supplier = (
        db.query(Supplier)
        .filter(Supplier.supplier_id == purchase_order.supplier_id)
        .first()
    )

    if not supplier:
        raise HTTPException(
            status_code=404,
            detail="Supplier not found"
        )

    # Create Purchase Order
    new_purchase_order = PurchaseOrder(
        supplier_id=purchase_order.supplier_id,
        expected_delivery=purchase_order.expected_delivery,
        status="Pending",
    )

    # Add Purchase Order Items
    for item in purchase_order.items:
        new_purchase_order.items.append(
            PurchaseOrderItem(
                product_id=item.product_id,
                quantity=item.quantity,
                unit_price=item.unit_price,
            )
        )

    db.add(new_purchase_order)
    db.commit()
    db.refresh(new_purchase_order)

    # Return response matching PurchaseOrderResponse schema
    return {
        "purchase_order_id": new_purchase_order.purchase_order_id,
        "supplier_id": new_purchase_order.supplier_id,
        "supplier_name": supplier.supplier_name,
        "order_date": new_purchase_order.order_date,
        "expected_delivery": new_purchase_order.expected_delivery,
        "status": new_purchase_order.status,
        "items": [
            {
                "item_id": item.item_id,
                "product_id": item.product_id,
                "quantity": item.quantity,
                "unit_price": item.unit_price,
            }
            for item in new_purchase_order.items
        ],
    }


def get_all_purchase_orders(db: Session):
    purchase_orders = (
        db.query(PurchaseOrder)
        .options(
            joinedload(PurchaseOrder.supplier),
            joinedload(PurchaseOrder.items).joinedload(
                PurchaseOrderItem.product
            ),
        )
        .all()
    )

    response = []

    for purchase_order in purchase_orders:
        response.append(
            {
                "purchase_order_id": purchase_order.purchase_order_id,
                "supplier_id": purchase_order.supplier_id,
                "supplier_name": purchase_order.supplier.supplier_name
                if purchase_order.supplier
                else None,
                "order_date": purchase_order.order_date,
                "expected_delivery": purchase_order.expected_delivery,
                "status": purchase_order.status,
                "items": [
                    {
                        "item_id": item.item_id,
                        "product_id": item.product_id,
                        "quantity": item.quantity,
                        "unit_price": item.unit_price,
                    }
                    for item in purchase_order.items
                ],
            }
        )

    return response