from typing import Annotated

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}") 
async def read_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None,
):
    '''
    curl -X 'PUT' 'http://localhost:8000/items/20?q=teting_curl_request' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{ 
            "name": "beka", 
            "description":"black_man", 
            "price":"0.0", 
            "tax":"0.5" 
        }'
    '''
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"Item": item})
    return results

@app.put("/severl_items/{item_id}")
async def update_item(item_id: int, item: Item, user: User, importance: Annotated[int, Body()], q: str | None = None):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}

    if q:
        results.update({"q":q})

    return results

@app.put("/single_items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results

