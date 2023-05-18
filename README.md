# Basic REST API using FastAPI

### 1. Index
Endpoint: GET `/` <br>
Returns all items data as a dictionary. <br>

### 2. Query item by id
Endpoint: GET `/items/{item_id}` <br>
Parameters: <ul>
<li>item_id: integer representing the id of the item to be queried. </ul>
Returns the item corresponding to the provided item_id parameter. <br>
If no item corresponds to the provided item_id, raises a 404 Not Found error. <br>

### 3. Query item by parameters <br>
Endpoint: GET `/items/` <br>
Query parameters: <ul>
<li>name: (optional) string representing the name of the item to be queried.
<li>price: (optional) float representing the price of the item to be queried.
<li>count: (optional) integer representing the count of the item to be queried.
<li>category: (optional) string representing the category of the item to be queried. </ul>
Returns the items that match the provided query parameters. <br>
If no item matches the query parameters, returns an empty selection. <br>
If no query parameters are provided, returns all items. <br>

### 4. Add new item <br>
Endpoint: POST `/` <br>
Parameters: <ul>
<li>item: JSON data representing an item to be added. </ul>
Adds the provided item to the items data. <br>
If the item ID already exists in the data, raises a 400 Bad Request error. <br>

### 5. Update item <br>
Endpoint: PUT `/update/{item_id}` <br>
Path parameter: <ul>
<li>item_id: integer representing the id of the item to be updated. </ul>
Query parameters (all optional): <ul><br>
<li>name: string representing the new name of the item.
<li>price: float representing the new price of the item.
<li>count: integer representing the new count of the item. </ul>
Updates the attributes of the item with the provided item_id. <br>
If the item with the provided item_id does not exist in the data, raises a 404 Not Found error. <br>
If no update parameters are provided, raises a 400 Bad Request error. <br>

### 6. Delete item <br>
Endpoint: DELETE `/delete/{item_id}`
Parameters: <ul>
<li>item_id: integer representing the id of the item to be deleted. </ul>
Deletes the item with the provided item_id from the data. <br>
If the item with the provided item_id does not exist in the data, raises a 404 Not Found error.
