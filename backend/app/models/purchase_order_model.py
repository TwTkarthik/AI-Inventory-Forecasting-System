from sqlalchemy import Column, String, DateTime, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"

    purchase_order_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )
    supplier_id = Column(
    UUID(as_uuid=True),
    ForeignKey("suppliers.supplier_id"),
    nullable=False)
    order_date = Column(DateTime(timezone=True), server_default=func.now())
    expected_delivery = Column(DateTime(timezone=True), nullable=True)
    status = Column(
    String(20),
    nullable=False,
    default="Pending")

    supplier = relationship("Supplier", back_populates="purchase_orders")
    items = relationship(
        "PurchaseOrderItem",
        back_populates="purchase_order",
        cascade="all, delete-orphan",
    )
