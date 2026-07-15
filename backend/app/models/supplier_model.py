from sqlalchemy import Column, String, Integer, Text, DateTime, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.db.base import Base


class Supplier(Base):
    __tablename__ = "suppliers"

    supplier_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )
    supplier_name = Column(String(255), nullable=False)
    contact_person = Column(String(255))
    email = Column(String(255))
    phone = Column(String(20))
    address = Column(Text)
    lead_time_days = Column(Integer, server_default=text("0"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
