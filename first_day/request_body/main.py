from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()

@app.post('/items/') # curl -H 'Content-Type: application/json' -d '{ "name":"beka", "price":300.9 }' -X POST http://127.0.0.1:8000/items/
async def post_item(item: Item):
    return item