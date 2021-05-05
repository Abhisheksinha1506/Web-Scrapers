import requests                 # Simpler HTTP requests 
from bs4 import BeautifulSoup   # Python package for pulling data out of HTML and XML files
import pandas as pd             # Python package for data manipulation and analysis
import re                       # regular expressions
import json                     # Python package used to work with JSON data
from tqdm import tqdm           # python for displaying progressbar 
from datetime import datetime   # python package to retireve DateTime


url = 'https://quotes.toscrape.com/page/{}/'.format(page)         
url_text = requests.get(url).text                    # Get the session text for the link
url_soup = BeautifulSoup(url_text, 'html.parser')   # Get data from the HTML

Quote=url_soup.find_all("span",attrs={"itemprop" : "text"})
Author=url_soup.find_all("small",attrs={"itemprop" : "author"})

dataframe_columns = [ 'Author', 'Quote']
dataframe = pd.DataFrame(columns=dataframe_columns)
for f, b,j in zip(Author, Quote, range(0,len(Author))):
    dataframe.at[j,'Author'] = f.text.strip()
    dataframe.at[j,'Quote'] = b.text.strip()

print(dataframe.head(10))

