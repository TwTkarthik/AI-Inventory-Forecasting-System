from sqlalchemy import Column, Integer, Numeric, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base


class PurchaseOrderItem(Base):
    __tablename__ = "purchase_order_items"

    item_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )
    purchase_order_id = Column(
    UUID(as_uuid=True),
    ForeignKey("purchase_orders.purchase_order_id"),
    nullable=False,
    )
    product_id = Column(
    UUID(as_uuid=True),
    ForeignKey("products.product_id"),
    nullable=False,
    )
    quantity = Column(Integer, nullable=False)
    unit_price = Column(
    Numeric(10, 2),
    nullable=False
    )

    purchase_order = relationship("PurchaseOrder", back_populates="items")
    product = relationship(
    "Product",
    back_populates="purchase_order_items"
    )
