from sqlalchemy.orm import Session

from app.models.supplier_model import Supplier


def get_all_suppliers(db: Session):
    return db.query(Supplier).all()


def create_supplier(db: Session, supplier):

    new_supplier = Supplier(
        supplier_name=supplier.supplier_name,
        contact_person=supplier.contact_person,
        email=supplier.email,
        phone=supplier.phone,
        address=supplier.address,
        lead_time_days=supplier.lead_time_days,
    )

    db.add(new_supplier)
    db.commit()
    db.refresh(new_supplier)

    return {
        "message": "Supplier created successfully ✅"
    }