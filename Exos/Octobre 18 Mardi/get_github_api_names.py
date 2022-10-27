from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
API_KEY = "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"

df = pd.read_csv('akinator.csv', usecols=["github name"])
ret = {}
for i in df.values.tolist():
    i = "".join(i)
    print(i)
    try:
        r = requests.get( f"https://api.github.com/users/{i}", auth=("MickaWilk",API_KEY) )
        print(r, r.json()['name'])
        ret[i] = r.json()['name']
    except:
        print("Requête non trouvée\n")
print(ret)
