import requests
from lxml import html
from urllib.parse import urljoin
from pymongo import MongoClient

def insert_to_db(list_currencies):
    client = MongoClient("mongodb://ahmed:testtest@cluster0-shard-00-00-pbhxl.mongodb.net:27017,cluster0-shard-00-01-pbhxl.mongodb.net:27017,cluster0-shard-00-02-pbhxl.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
    db = client["currencies"]
    collection = db["price"]
    for currency in list_currencies:
        exists = collection.find_one({'_id': currency['_id']})
        if exists:
            if exists['name'] == currency['name'] and (exists['price'] != currency['price'] or exists['market cap'] != currency['market cap'] or exists['change(24h)'] != currency['change(24h)']):
                collection.replace_one({'_id': exists['_id']}, currency)
                print(f"Old item: {exists} New Item: {currency}")
        else:
            collection.insert_one(currency)
    client.close()

def get(list_elements):
    try:
        return list_elements.pop(0)
    except:
        return ''

all_currencies = []

def scrape(url):
    resp = requests.get(url=url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    })

    tree = html.fromstring(html=resp.content)

    currencies = tree.xpath("//tr[@class='cmc-table-row sc-1ebpa92-0 kQmhAn']")
    for currency in currencies:
        c = {
            "_id": int(get(currency.xpath(".//td[1]/div/text()"))),
            'name': get(currency.xpath(".//td[2]/div/a/text()")),
            'market cap': get(currency.xpath(".//td[3]/div/text()")),
            'price': get(currency.xpath(".//td[4]/a/text()")),
            'change(24h)': get(currency.xpath(".//td[7]/div/text()"))
        }

        all_currencies.append(c)
    
    next_page = tree.xpath("(//a[@data-qa-id='table-listing-button-next']/@href)[1]")

    if len(next_page) != 0:
        next_page_url = urljoin(base=url, url=next_page[0])
        scrape(url=next_page_url)

scrape(url="https://coinmarketcap.com")
insert_to_db(all_currencies)
print(len(all_currencies))
