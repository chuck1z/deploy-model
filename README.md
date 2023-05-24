# Deploy Model

Deploying an ML model may sound scary. We don't learn Tensorflow, model training, or even python as a CC participant. <br>
Through this repo, you can see the many ways you can deploy a model. <br>
1. The `starting-point` branch covers all the basic FastAPI stuffs, how a Rest API code looks like using python as its programming language
2. The `FastAPI-using-own-model` branch can be used as an example on model "deployment" using FastAPI
3. The `Express-TFJS` branch is an example of model "deployment" using nodejs. It requires extra work, you have to convert your model to json and its performance is not as good as native python
4. The `TF-Serving` and `TF-Serving-API` branches are used in tandem for TF Serving implementation. TF Serving is only used to host the model and the API can be used as an example of how to redirect request to a TF Serving backend. You can also ask your MD peer to make a direct request instead of making another API

# FastAPI

FastAPI is a modern web framework for building RESTful APIs in Python. It was first released in 2018 and has quickly gained popularity among developers due to its ease of use, speed and robustness. FastAPI is based on Pydantic and type hints to validate, serialize, and deserialize data.

Documentation: https://fastapi.tiangolo.com

Source Code: https://github.com/tiangolo/fastapi

To run this file, do
```bash
uvicorn main:app
```
or
```bash
uvicorn main:app --reload
```
to automatically restart the kernel everytime there's a change saved inside `main.py`

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
