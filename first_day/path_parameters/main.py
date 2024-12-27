from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


app = FastAPI()

@app.get('/items/{item_id}') # path parameter
async def read_item(item_id: int):
    '''
    Example of how to add the description to endpoint
    '''
    return {"item": item_id}


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName): # with using enum we can predefine parameter
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
    if model_name.value == ModelName.resnet:
        return {"model_name": model_name, "message": "LeCNN all the images!"}
    
    return {"model_name": model_name, "message": "Have some residuals"}
    

@app.get('/files/{file_path:path}') # to convert path, and to get `double-slash`
async def get_file(file_path:str):
    return {"file_path": file_path}