from bs4 import BeautifulSoup as bs
import pandas as pd
import requests


df = pd.read_csv('akinator.csv', usecols=["github name"])
ret = {}
for i in df.values.tolist():
    i = " ".join(i)
    print(i)
    try:
        r = requests.get( f"https://github.com/{i}" )
        ret[i] = bs(r.content).find("span", itemprop="name").getText().strip()
    except:
        print("Requête non trouvée\n")
[print(f"{i}:{j}") for i,j in ret.items()]
