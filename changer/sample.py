from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn 
app = FastAPI()

class Item(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5

# In a real application, this would be a database or persistent storage
items_db = {
    "foo": {"name": "Foo Item", "price": 50.0},
    "bar": {"name": "Bar Item", "description": "A description", "price": 62.0, "tax": 20.2},
    "sde": {"name": "Bar Item", "description": "A description", "price": 62.0, "tax": 20.2},

}

@app.put("/items/{item_id}")
async def update_item(item_id: str, item: Item):
    """
    Updates an existing item in the database.

    Args:
        item_id: The ID of the item to update.
        item: The updated item data.

    Returns:
        A dictionary confirming the update and the updated item.
    """
    if item_id not in items_db:
        # In a real application, you might raise an HTTPException(status_code=404, detail="Item not found")
        return {"message": f"Item with ID '{item_id}' not found."}

    # Update the item in our "database"
    items_db[item_id].update(item.dict(exclude_unset=True))
    return {"message": "Item updated successfully", "updated_item": items_db[item_id]}


if __name__=='__main__':
  uvicorn.run('sample:app',port=8000,reload=False,host='0.0.0.0',log_level='debug')
