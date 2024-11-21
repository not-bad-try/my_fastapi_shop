from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate, ProductOut
from app.db.models.product import Product
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=ProductOut)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    """Создание нового товара"""
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get("/{product_id}", response_model=ProductOut)
async def get_product(product_id: int, db: Session = Depends(get_db)):
    """Получение товара по ID"""
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
