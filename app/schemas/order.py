from pydantic import BaseModel

# Базовая схема заказа
class OrderBase(BaseModel):
    product_id: int
    quantity: int
    total_price: float

#Схема для создания заказа
class OrderCreate(OrderBase):
    pass

# Схема для вывода заказа
class OrderOut(OrderBase):
    id: int

    class Config:
        orm_mode = True