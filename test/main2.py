from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    price:float
    is_offer:bool = None

@app.post("/items/")
def create_item(item:Item):
    return {"message": f"Item created: {item.name}, Price: {item.price}, Is Offer: {item.is_offer}"}