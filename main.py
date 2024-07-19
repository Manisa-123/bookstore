from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import schemas, crud
from services import is_valid_email

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/book/create", response_model=schemas.Book)
def create_book(
    title: str, author: str, price: int, db: Session = Depends(get_db)
):
    return crud.create_book(db=db, title=title, author=author, price=price)


@app.get("/book/list", response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):

    books = crud.get_books(db, skip=skip, limit=limit)
    return books


@app.get("/book/get/{id}", response_model=list[schemas.Book])
def read_book(id: int, db: Session = Depends(get_db)):
    book = crud.get_book_with_id(id=id, db=db)
    return book


@app.post("/users/create", response_model=schemas.User)
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    if not is_valid_email(email):
        raise HTTPException(status_code=400, detail=f"Invalid email address: {email}")
    return crud.create_user(db=db, name=name, email=email)


@app.get("/users/list", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/user/get/{id}", response_model=list[schemas.User])
def read_user(id: int, db: Session = Depends(get_db)):
    users = crud.get_user_with_id(db=db, id=id)
    return users


@app.post("/cart/create", response_model=schemas.Cart)
def add_to_cart(
    user_id: int, book_id: int, quantity: int, db: Session = Depends(get_db)
):
    return crud.add_to_cart(db=db, user_id=user_id, book_id=book_id, quantity=quantity)


@app.get("/cart/get/{user_id}", response_model=list[schemas.Cart])
def get_cart(user_id: int, db: Session = Depends(get_db)):
    return crud.get_cart_items(db, user_id=user_id)


@app.put("/cart/update/{id}")
def update_cart(id: int, quantity: int, book_id: int, db: Session = Depends(get_db)):
    return crud.update_cart(db=db, quantity=quantity, book_id=book_id, id=id)


@app.delete("/cart/{id}")
def delete_cart(id: int, db: Session = Depends(get_db)):
    return crud.delete_cart(db=db, id=id)


@app.get("/calculate")
def calculate_cart(user_id: int, db: Session = Depends(get_db)):
    return {"Total Cart Amount": crud.calculate_total_cost(db=db, user_id=user_id)}
