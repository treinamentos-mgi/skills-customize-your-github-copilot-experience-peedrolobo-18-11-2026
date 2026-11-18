from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Books API")

books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "Matilda", "author": "Roald Dahl"},
]


class BookCreate(BaseModel):
    title: str
    author: str


@app.get("/")
def read_root():
    return {"message": "Books API"}


@app.get("/books")
def list_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    new_book = {
        "id": max((item["id"] for item in books), default=0) + 1,
        "title": book.title,
        "author": book.author,
    }
    books.append(new_book)
    return new_book