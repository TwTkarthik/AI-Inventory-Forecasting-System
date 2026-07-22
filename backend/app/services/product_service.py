from sqlalchemy.orm import Session, joinedload

from app.models.product_model import Product


def get_all_products(db: Session):
    products = db.query(Product).options(joinedload(Product.supplier)).all()

    response = []

    for product in products:
        response.append({
            "product_id": product.product_id,
            "sku": product.sku,
            "mpn": product.mpn,
            "product_name": product.product_name,
            "brand": product.brand,
            "category": product.category,
            "description": product.description,
            "selling_price": product.selling_price,
            "cost_price": product.cost_price,
            "barcode": product.barcode,
            "unit": product.unit,
            "lead_time_days": product.lead_time_days,
            "weight": product.weight,
            "length": product.length,
            "width": product.width,
            "height": product.height,
            "primary_image": product.primary_image,
            "status": product.status,
            "status_reason": product.status_reason,
            "supplier_id": product.supplier_id,
            "supplier_name": (
                product.supplier.supplier_name
                if product.supplier
                else None
            ),
            "created_at": product.created_at,
            "updated_at": product.updated_at,
        })

    return response

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