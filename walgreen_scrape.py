import requests
from fake_useragent import UserAgent
import json 
from urllib.parse import urljoin
import sqlite3

ua = UserAgent()

extracted_products = []

def scraper(pageNumber=1):
    url = "https://www.walgreens.com/productsearch/v1/products/search"

    querystring = {"instart_disable_injection":"true"}

    payload = {"p":pageNumber,"s":24,"view":"allView","geoTargetEnabled":False,"abtest":["tier2","showNewCategories"],"deviceType":"desktop","q":"undefined","id":["350006"],"requestType":"tier3","sort":"Top Sellers","couponStoreId":"15196"}
    headers = {
        'content-type': "application/json",
        'User-Agent': ua.random
        }

    response = requests.post(url, data=json.dumps(payload), headers=headers, params=querystring)

    data = response.json()

    try:

        products = data['products']

        for product_info in products:
            pr_info = product_info['productInfo']
            pr = {
                'img': pr_info['imageUrl'],
                'price': pr_info['priceInfo']['regularPrice'],
                'id': pr_info['prodId'],
                'name': pr_info['productDisplayName'],
                'size': pr_info['productSize'],
                'url': urljoin(base='https://walgreens.com', url=pr_info['productURL'])
            }

            extracted_products.append(pr)
        
        pageNumber += 1
        scraper(pageNumber=pageNumber)
    except KeyError:
        return 

scraper()

connection = sqlite3.connect("walgreens.db")
c = connection.cursor()
try:
    c.execute('''
        CREATE TABLE products (
            id TEXT PRIMARY KEY,
            name TEXT,
            url TEXT,
            size TEXT,
            price TEXT,
            image TEXT
        )

    ''')

    connection.commit()
except sqlite3.OperationalError as e:
    print(e)

for product in extracted_products:
    try:
        c.execute('''
            INSERT INTO products (id, name, url, size, price, image) VALUES (
                ?,?,?,?,?,?
            )
        ''', (product['id'],
            product['name'],
            product['url'],
            product['size'],
            product['price'],
            product['img']))
    except sqlite3.IntegrityError:
        pass

connection.commit()
connection.close()
