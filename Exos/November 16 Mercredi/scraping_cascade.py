# import necessary libraries
from bs4 import BeautifulSoup as bs
import requests
import re


# function to extract html document from given url
def getHTMLdocument(url):
    response = requests.get(url)
    return response.text

url_to_scrape = "https://www.charlesbordet.com/fr/blog/"
html_document = getHTMLdocument(url_to_scrape)
soup = bs(html_document, 'html.parser')


# find all the anchor tags with "href"
# attribute starting with "https://"
# for link in soup.find_all('a',
#                           attrs={'href': re.compile("/fr/")}):
links = []
summaries = []


for h2 in soup.find_all("h2", {"class": "archive__item-title"}):
    for a in h2.find_all("a"):
        url = "https://www.charlesbordet.com" + a['href']
        links.append(url)


#Get summaries
for url in links:
    soup = bs(getHTMLdocument(url), 'html.parser')
    print('\n\n', url)
    summary = []
    for index, ul in enumerate(soup.find('ul', {"class": "toc__menu"})):
        # print ('\n', ul.a.text)
        ret = []
        ret.append(ul.a.text)
        for li in (ul.findChildren('li')):
            # print(li.a.text)
            ret.append(li.a.text)
        if ret: summary.append(ret)
    if summary: summaries.append(summary)
print(summaries)
# for truc in soup.find(class_= "toc"):
# print(tmp_soup)
