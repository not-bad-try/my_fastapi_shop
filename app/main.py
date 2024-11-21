from fastapi import FastAPI
from app.api.v1.endpoints import auth, products, orders

app = FastAPI(title="My FastAPI Shop")

# Роуты
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(orders.router, prefix="/orders", tags=["orders"])

@app.get("/")
async def root():
    return {"message": "Welcome to My FastAPI Shop"}
