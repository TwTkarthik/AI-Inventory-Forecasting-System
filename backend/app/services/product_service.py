from sqlalchemy.orm import Session

from app.models.product_model import Product


def get_all_products(db: Session):
    return db.query(Product).all()


def create_product(db: Session, product):

    new_product = Product(
        sku=product.sku,
        mpn=product.mpn,
        product_name=product.product_name,
        brand=product.brand,
        category=product.category,
        description=product.description,
        selling_price=product.selling_price,
        cost_price=product.cost_price,
        barcode=product.barcode,
        unit=product.unit,
        lead_time_days=product.lead_time_days,
        weight=product.weight,
        length=product.length,
        width=product.width,
        height=product.height,
        primary_image=product.primary_image,
        status=product.status,
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return {
        "message": "Product created successfully ✅"
    }