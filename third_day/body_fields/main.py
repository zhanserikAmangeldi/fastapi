from typing import Annotated

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str
    description: str | None = Field(default=None, title="the description of the item", max_length=300)
    price: float = Field(gt=0, description="price of the item must be greater than zero")
    tax: float | None = None

app = FastAPI()

@app.put("/items/{item_id}")
async def read_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results
