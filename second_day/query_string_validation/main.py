from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get('/items/')
async def get_items(q: Annotated[str | None, Query(min_length=3, max_length=50, pattern='^hello')] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id":"Bar"}]}

    if q:
        results.update({"q": q})
    
    return results

# query parameters list/multiple values
@app.get("/multiple/items/")
async def read_items(q: Annotated[list[str] | None, Query(
    alias="item-query",
    title="Query string",
    description="Query string for the items to search in the database that have a good match",
    min_length=3,
    deprecated=True
)] = ['foo', 'bar']):
    query_items = {"q": q}
    return query_items
