from fastapi import FastAPI
import pickle
import pandas as pd
from typing import Union
import numpy as np


app = FastAPI()

@app.get("/")
async def root(total_bill: Union[float, None] = 45,
               sex: Union[str, None] = "Female",
               smoker: Union[str, None] = "No",
               day: Union[str, None] = "Thur",
               time: Union[str, None] = "Dinner",
               size: Union[int, None] = 3):

    x_user = get_user_df(total_bill, sex, smoker, day, time, size)
    pickle_model = pickle.load(open("pipeline_deploy.pkl", "rb"))
    pred = pickle_model.predict(x_user)
    return {"prédiction": f"{round(pred[0])}"}

def get_user_df(total_bill, sex, smoker, day, time, size):
    x_user = pd.DataFrame({
        "total_bill" : [float(total_bill)],
        "sex" : [sex.capitalize()],
        "smoker" : [smoker.capitalize()],
        "day" : [day.capitalize()],
        "time" : [time.capitalize()],
        "size" : [int(size)]
    })
    return x_user
