import pickle
from typing import Union

from fastapi import FastAPI

app = FastAPI()
pipe = pickle.load(open('pipline.pkl', 'rb'))

@app.get("/")
def predict(total_bill: Union[float, None] = 45.00
            ,sex:Union[str, None] = "female"
            ,smoker:Union[str, None] = 45.00
            ,day:Union[float, None] = 45.00
            ,time:Union[float, None] = 45.00
            ,size:Union[float, None] = 45.00):
    return { "response": total_bill, "smoker":smoker}
    # return { "response": pipe.predict()}




@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
