from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.base import Base


class Inventory(Base):
    __tablename__ = "inventory"

    inventory_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )

    product_id = Column(
        UUID(as_uuid=True),
        ForeignKey("products.product_id"),
        nullable=False
    )

    quantity_on_hand = Column(Integer, default=0)
    reserved_quantity = Column(Integer, default=0)
    reorder_level = Column(Integer, default=10)
    warehouse_location = Column(String(100))
    last_stock_update = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    product = relationship("Product", back_populates="inventory")