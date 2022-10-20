from data_company import data

def price_filter(data):
    for i in data:
        if i["price"] > 500: print( i["company_name"], i["price"])


def find_partners(data):
    ret = []
    for i in data:
        for j in i['company_partners']:
            ret.append(j)
    print(sorted(set(ret)))

def average_price(data):
    n = 0; count = 0
    for i in data:
        n += i['price']
        count += 1
    return int(n / count)

def compagnies_stock(data):
    stock = {}
    ret = {}
    for i in data:
        for j in i['company_partners']:
            ret[j] = 0
            stock[j] = 0
    for i in data:
        for j in i['company_partners']:
            ret[j] += int(i['price'] / (2 * len(i['company_partners'])))
            stock[j] += i['stock'] / (2 * len(i['company_partners']))
    ret = {i:ret[i] for i in sorted(ret, key=ret.get, reverse=True)}
    l = []
    for i in ret:
        l.append({'company_name': i, 'stock': stock[i],'company_value': ret[i]})
    print(l)
compagnies_stock(data)
