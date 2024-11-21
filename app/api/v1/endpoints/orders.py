from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.order import OrderCreate, OrderOut
from app.db.models.order import Order
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=OrderOut)
async def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    """Создание нового заказа"""
    new_order = Order(**order.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

@router.get("/{order_id}", response_model=OrderOut)
async def get_order(order_id: int, db: Session = Depends(get_db)):
    """Получение заказа по ID"""
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
