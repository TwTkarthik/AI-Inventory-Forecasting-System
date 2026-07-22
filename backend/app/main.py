from fastapi import FastAPI
from sqlalchemy import text

from app.api.products import router as product_router
from app.api.suppliers import router as supplier_router
from app.api.inventory import router as inventory_router

from app.db.database import engine
from app.db.base import Base

import app.models.product_model
import app.models.supplier_model
import app.models.inventory_model

app = FastAPI(
    title="AI Inventory Forecasting API",
    description="Backend API for AI-Powered Inventory Forecasting & Smart Warehouse Management System",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Inventory Forecasting API 🚀"
    }


@app.get("/health")
def health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {
            "status": "Database Connected ✅"
        }
    except Exception as e:
        return {
            "status": "Database Connection Failed ❌",
            "error": str(e)
        }


Base.metadata.create_all(bind=engine)

app.include_router(product_router)
app.include_router(supplier_router)
app.include_router(inventory_router)