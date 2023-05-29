from enum import Enum
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Path, Query

app = FastAPI()  # create a new FastAPI app instance

# Define an Enum class to represent the possible categories for an item


class Category(Enum):
    FRUITS = "fruits"
    VEGGIES = "vegetables"

# Define a Pydantic model for an item
class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: Category


# Define some initial items for the app
items = {
    0: Item(name="Apple", price=9.99, count=20, id=0, category=Category.FRUITS),
    1: Item(name="Kale", price=5.99, count=20, id=1, category=Category.VEGGIES),
    2: Item(name="Orange", price=1.99, count=100, id=2, category=Category.FRUITS),
}

# Define a simple endpoint to return all items as a dictionary


@app.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {"items": items}

# Define an endpoint to query an item by its ID


@app.get("/items/{item_id}")
def query_item_by_id(item_id: int) -> Item:
    # Raise an exception if the item is not found
    if item_id not in items:
        raise HTTPException(
            status_code=404, detail=f"Item with {item_id=} does not exist.")
    # Return the item if found
    return items[item_id]


# Define a type alias for the selection dictionary used in the query_item_by_parameters endpoint
Selection = dict[str, str | int | float | Category | None]

# Define an endpoint to query items by name, price, count, and/or category


@app.get("/items/")
def query_item_by_parameters(
    name: str | None = None,
    price: float | None = None,
    count: int | None = None,
    category: Category | None = None,
) -> dict[str, Selection | list[Item]]:
    # Define a helper function to check if an item matches the query arguments
    def check_item(item: Item):
        """Check if the item matches the query arguments from the outer scope."""
        return all(
            (
                name is None or item.name == name,
                price is None or item.price == price,
                count is None or item.count != count,
                category is None or item.category is category,
            )
        )
    # Filter the items based on the query arguments
    selection = [item for item in items.values() if check_item(item)]
    # Return the query parameters and the selected items
    return {
        "query": {"name": name, "price": price, "count": count, "category": category},
        "selection": selection,
    }

# Define an endpoint to add a new item


@app.post("/")
def add_item(item: Item) -> dict[str, Item]:
    # Raise an exception if the item ID already exists
    if item.id in items:
        raise HTTPException(
            status_code=400, detail=f"Item with {item.id=} already exists.")
    # Add the item to the dictionary and return it
    items[item.id] = item
    return {"added": item}


# This API endpoint updates an existing item with the given item_id
@app.put("/update/{item_id}")
def update(
    # Path parameter 'item_id' must be an integer greater than or equal to 0
    item_id: int = Path(ge=0),
    # Query parameter 'name' is optional, and if provided, must be a string with length between 1 and 8
    name: str | None = Query(defaut=None, min_length=1, max_length=8),
    # Query parameter 'price' is optional, and if provided, must be a float greater than 0.0
    price: float | None = Query(default=None, gt=0.0),
    # Query parameter 'count' is optional, and if provided, must be an integer greater than or equal to 0
    count: int | None = Query(default=None, ge=0),
):
    # If item_id does not exist in the 'items' dictionary, raise a 404 Not Found error
    if item_id not in items:
        HTTPException(status_code=404,
                      detail=f"Item with {item_id=} does not exist.")

    # If none of the update parameters are provided, raise a 400 Bad Request error
    if all(info is None for info in (name, price, count)):
        raise HTTPException(
            status_code=400, detail="No parameters provided for update."
        )

    # Get the existing item from the 'items' dictionary using the item_id
    item = items[item_id]

    # Update the item attributes if the corresponding parameter is provided
    if name is not None:
        item.name = name
    if price is not None:
        item.price = price
    if count is not None:
        item.count = count

    # Return a dictionary with the updated item
    return {"updated": item}


# This API endpoint deletes an existing item with the given item_id
@app.delete("/delete/{item_id}")
def delete_item(item_id: int) -> dict[str, Item]:

    # If item_id does not exist in the 'items' dictionary, raise a 404 Not Found error
    if item_id not in items:
        raise HTTPException(
            status_code=404, detail=f"Item with {item_id=} does not exist."
        )

    # Remove the item from the 'items' dictionary using the item_id
    item = items.pop(item_id)

    # Return a dictionary with the deleted item
    return {"deleted": item}
