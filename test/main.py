from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"hello world!"}

@app.get("/me")
def read_me():
    return {"name":"My name is John Doe!"}

@app.get("/items/{item_id}")
def read_item(item_id:int, q:str =None):
    return {'item_id':item_id, 'query':q}