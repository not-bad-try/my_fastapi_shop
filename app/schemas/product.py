from pydantic import BaseModel

 #Базовая схема товара
class ProductBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    stock: int

#Схема для создания товара
class ProductCreate(ProductBase):
    pass

#Схема для вывода товара
class ProductOut(ProductBase):
    id: int

    class Config:
        orm_mode = True
