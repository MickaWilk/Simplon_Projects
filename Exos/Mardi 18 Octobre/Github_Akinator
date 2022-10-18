from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
API_KEY = "30682404-934c5731ef7773f53b291d229"


df = pd.read_csv('akinator.csv', usecols=["Animal totem"])
ret = {}
for i in df.values.tolist():
    i = " ".join(i)
    print(i)
    try:
        r = requests.get( f"https://pixabay.com/api/?key={API_KEY}&image_type=photo&q={i}" ).json()
        ret[i] = r["hits"][0]["largeImageURL"]
        print(ret[i])
    except:
        print("Requête non trouvée\n")
[print(f"{i}:{j}") for i,j in ret.items()]
