from sqlalchemy.orm import Session
from models import Book, User, Cart
from fastapi import HTTPException


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()


def get_book_with_id(db: Session, id: int):
    return db.query(Book).filter(Book.id == id).all()


def create_book(db: Session, title: str, author: str, price: int):
    db_book = Book(title=title, author=author, price=price)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user_with_id(db: Session, id: int):
    return db.query(User).filter(User.id == id).all()


def create_user(db: Session, name: str, email: str):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_cart_items(db: Session, user_id: int):
    return db.query(Cart).filter(Cart.user_id == user_id).all()


def add_to_cart(db: Session, user_id: int, book_id: int, quantity: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db_cart_item = Cart(user_id=user_id, book_id=book_id, quantity=quantity)
    db.add(db_cart_item)
    db.commit()
    db.refresh(db_cart_item)
    return db_cart_item


def update_cart(db: Session, id: int, book_id: int, quantity: int):
    cart = db.query(Cart).filter(Cart.id == id).first()

    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    cart.quantity = quantity
    cart.book_id = book_id

    db.commit()


def delete_cart(db: Session, id: int):
    cart = db.query(Cart).filter(Cart.id == id).first()

    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    db.delete(cart)
    db.commit()


def calculate_total_cost(user_id: int, db: Session):
    cart = db.query(Cart).filter(Cart.user_id == user_id).all()
    total_amount = 0
    for item in cart:
        book = db.query(Book).filter(Book.id == item.book_id).first()
        total_amount += item.quantity * book.price
    return total_amount


def calculate_order_total(db: Session, user_id: int):
    cart_items = db.query(Cart).filter(Cart.user_id == user_id).all()
    total_cost = sum(item.book.price * item.quantity for item in cart_items)
    return total_cost
