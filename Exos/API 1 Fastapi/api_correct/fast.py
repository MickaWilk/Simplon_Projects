from fastapi import FastAPI
#from tips import preprocessing
from typing import Optional
import pandas as pd
import pickle
from typing import Union

app = FastAPI()


@app.get("/")
def predict(total_bill: Union[int, None] = '16',
    sex: Union[str, None] = 'Female',
    smoker: Union[str, None] = "No",
    day: Union[str, None] = "Sun",
    time: Union[str, None] = "Dinner",
    size: Union[int, None] = 2,
    ):
    """
    http://127.0.0.1:8000/?total_bill=16&sex=Female&smoker=No&day=Sun&time=Dinner&size=2
    \n
    Do something
    """
    X_user = X_user_build(total_bill,sex, smoker, day, time, size)
    pickled_model = pickle.load(open('pipline-api.pkl', 'rb'))
    pred = pickled_model.predict(X_user)[0]
    return {"prediction": f"{round(pred)}"}




def X_user_build(total_bill,sex, smoker, day, time, size):
    X_user = pd.DataFrame({
    "total_bill": [float(total_bill)],
    "sex": [sex],
    "smoker": [smoker],
    "day": [day],
    "time": [time],
    "size": [int(size)]
    })
    return  X_user
