from fastapi import FastAPI


app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}, 
    {"item_name": "Cherry"}, {"item_name": "Banana"}, {"item_name": "Apple"},
    {"item_name": "Mercedes"}, {"item_name": "BMW"}, {"item_name": "Toyota"},
    {"item_name": "Scooby Doo"}, {"item_name": "Micky mouse"}, {"item_name": "Tom and Jerry"}
    ]

@app.get('/items/')
async def get_items(offset: int = 0, limit: int = 10):
    return fake_items_db[offset : offset+limit]

@app.get("/items/{item_id}")
async def get_item(item_id: str, needy: str, q: str | None = None,  short: bool = False):   # by adding query parameter without default value (needy)
    item = {"item_id": item_id, "needy": needy}                                             # we make required query request
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

