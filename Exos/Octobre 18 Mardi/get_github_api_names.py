from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
API_KEY = "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"

df = pd.read_csv('akinator.csv', usecols=["github name"])
ret = {}
for i in df.values.tolist():
    i = " ".join(i)
    print(i)
    try:
        r = requests.get( f"https://api.github.com/user/", {'Authorization': f'Bearer {API_KEY}'} )
        print(r)
    except:
        print("Requête non trouvée\n")
[print(f"{i}:{j}") for i,j in ret.items()]
