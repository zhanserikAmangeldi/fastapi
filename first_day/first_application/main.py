from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def root():
    '''
    The description of root endpoint
    '''
    return {"response": "Hello, world!"}
