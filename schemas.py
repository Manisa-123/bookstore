from pydantic import BaseModel
from typing import List, Optional


class BookBase(BaseModel):
    title: str
    author: str
    price: float


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class OrderItemBase(BaseModel):
    book_id: int
    quantity: int


class OrderItemCreate(OrderItemBase):
    pass


class OrderItem(OrderItemBase):
    id: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    user_id: int
    total_cost: float


class OrderCreate(OrderBase):
    order_items: List[OrderItemCreate]


class Order(OrderBase):
    id: int
    order_items: List[OrderItem]

    class Config:
        orm_mode = True


from pydantic import BaseModel


class CartBase(BaseModel):
    user_id: int
    book_id: int
    quantity: int


class CartCreate(CartBase):
    pass


class Cart(CartBase):
    id: int

    class Config:
        orm_mode = True


class OrderItemBase(BaseModel):
    book_id: int
    quantity: int


class OrderBase(BaseModel):
    user_id: int
    total_cost: float
