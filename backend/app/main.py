from fastapi import FastAPI
from sqlalchemy import text
from app.api.products import router as product_router
from app.db.database import engine

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
app.include_router(product_router)