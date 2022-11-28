import pandas as pd
import os

class Data():
    def __init__(self):
        pass
    def get_data(self):
        return pd.read_csv(os.path.join(os.path.dirname(__file__), "akinator.csv"))
