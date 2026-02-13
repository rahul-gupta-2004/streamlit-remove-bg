# uvicorn json_handle:app --reload

from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

# Load initial data from JSON file into a Python List
with open("data.json", "r") as f:
    db = json.load(f)

# Helper function to save changes back to file
def save_db():
    with open("data.json", "w") as f:
        json.dump(db, f, indent=4)

# Data Model for adding/updating items
class Item(BaseModel):
    id: int
    name: str
    price: int

# --- API ENDPOINTS ---

# GET: Get all items
@app.get("/items")
def get_items():
    return db

# GET: Get one item by ID
@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in db:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}

# POST: Add a new item
@app.post("/items")
def add_item(item: Item):
    db.append(item.dict())
    save_db()
    return {"message": "Added successfully", "data": item}

# PUT: Update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(db):
        if item["id"] == item_id:
            db[index] = updated_item.dict()
            save_db()
            return {"message": "Updated successfully"}
    return {"error": "Item not found"}

# DELETE: Remove an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(db):
        if item["id"] == item_id:
            db.pop(index)
            save_db()
            return {"message": "Deleted successfully"}
    return {"error": "Item not found"}
