from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

df = pd.read_csv('akinatorIA3.csv', usecols=["Film préféré"])
for i in df.values.tolist():
    page = requests.get(f"https://www.imdb.com/find?q={str(i)}")
    soup = bs(page.content, 'html.parser')
    try:
        print(i, "|", soup.find(class_="ipc-metadata-list-summary-item__li").get_text())
    except:
        print("film pas trouvé")

# page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
# print(page)
# print(page.status_code)
# print(page.content)

# print(list(soup.children))
# print([type(item) for item in list(soup.children)])
# html = list(soup.children)[1]
# body = list(html.children)[3]
# print(list(html.children))
# print(list(body.children))
# p = list(body.children)[1]
# print(p.get_text())
