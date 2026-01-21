from typing import Union

from fastapi import FastAPI

from logic import predict_score

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/score")
def get_score(input_data: dict):
    # use the logic 
    result = predict_score(input_data)
    return result