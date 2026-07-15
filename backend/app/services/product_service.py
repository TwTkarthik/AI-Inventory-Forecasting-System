from sqlalchemy import text
from app.db.database import engine


def get_all_products():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM products"))
        return [dict(row._mapping) for row in result]


def create_product(product):

    query = text("""
        INSERT INTO products
        (
            sku,
            mpn,
            product_name,
            brand,
            category,
            description,
            selling_price,
            cost_price,
            barcode,
            unit,
            lead_time_days,
            weight,
            length,
            width,
            height,
            primary_image,
            status
        )

        VALUES
        (
            :sku,
            :mpn,
            :product_name,
            :brand,
            :category,
            :description,
            :selling_price,
            :cost_price,
            :barcode,
            :unit,
            :lead_time_days,
            :weight,
            :length,
            :width,
            :height,
            :primary_image,
            :status
        )
    """)

    with engine.begin() as connection:
        connection.execute(query, product.model_dump())

    return {
        "message": "Product created successfully ✅"
    }