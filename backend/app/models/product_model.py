from sqlalchemy import (
    Column,
    String,
    Float,
    Integer,
    Text,
    DateTime,
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.base import Base


class Product(Base):
    __tablename__ = "products"

    product_id = Column(UUID(as_uuid=True), primary_key=True)
    supplier_id = Column(UUID(as_uuid=True), ForeignKey("suppliers.supplier_id"), nullable=True)
    sku = Column(String(100), unique=True, nullable=False)
    mpn = Column(String(100))
    product_name = Column(String(255), nullable=False)
    brand = Column(String(100))
    category = Column(String(100))
    description = Column(Text)

    selling_price = Column(Float, nullable=False)
    cost_price = Column(Float)

    barcode = Column(String(100), unique=True)
    unit = Column(String(50), nullable=False)

    lead_time_days = Column(Integer)

    weight = Column(Float)
    length = Column(Float)
    width = Column(Float)
    height = Column(Float)

    primary_image = Column(Text)

    status = Column(String(30))
    status_reason = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())

    supplier = relationship("Supplier", back_populates="products")
    inventory = relationship("Inventory", back_populates="product", uselist=False)
    purchase_order_items = relationship("PurchaseOrderItem", back_populates="product")