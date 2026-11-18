from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Books API")

books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "Matilda", "author": "Roald Dahl"},
]


class BookCreate(BaseModel):
    # TODO: Declare the required title and author fields.
    pass


@app.get("/")
def read_root():
    # TODO: Return a JSON message identifying this API.
    pass


@app.get("/books")
def list_books():
    # TODO: Return the books stored in the in-memory list.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Find and return the book, or raise HTTPException with status 404.
    pass


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    # TODO: Create a unique ID, add the book to the list, and return it.
    pass