import requests                 # Simpler HTTP requests 
from bs4 import BeautifulSoup   # Python package for pulling data out of HTML and XML files
import pandas as pd             # Python package for data manipulation and analysis

url = 'https://books.toscrape.com/'         
url_text = requests.get(url).text                    # Get the session text for the link
url_soup = BeautifulSoup(url_text, 'html.parser')   # Get data from the HTML

Book_Title=[]
Availability=url_soup.find_all("p",attrs={"class" : "instock availability"})
Price=url_soup.find_all("p",attrs={"class" : "price_color"})
Books=url_soup.find_all("article",attrs={"class" : "product_pod"})
for book in Books:
    Book_Title.append(book.find('img')['alt'])

dataframe_columns = [ 'Book Title', 'Price', 'Availability']
dataframe = pd.DataFrame(columns=dataframe_columns)
for f, b, i, j in zip(Availability, Price, Book_Title, range(0,len(Availability))):
    dataframe.at[j,'Book Title'] = i.strip()
    dataframe.at[j,'Price'] = b.text.strip()[2:]
    dataframe.at[j,'Availability'] = f.text.strip()

print(dataframe.head(10))
