import pickle
from typing import Union

from api_correct import fast

app = FastAPI()
pipe = pickle.load(open('pipline.pkl', 'rb'))

@app.get("/")
def ppredict(total_bill: Union[int, None] = '16',
    sex: Union[str, None] = 'Female',
    smoker: Union[str, None] = "No",
    day: Union[str, None] = "Sun",
    time: Union[str, None] = "Dinner",
    size: Union[int, None] = 2,
    ):

    x_user = get_user_df(total_bill, sex, smoker, day, time, size)
    pickle_model = pickle.load(open("pipeline_deploy.pkl", "rb"))
    pred = pickle_model.predict(x_user)
    return {"prédiction": f"{round(pred[0])}"}




@app.get("/items/{item_id}")
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
