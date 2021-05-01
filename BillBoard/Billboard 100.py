import requests                 # Simpler HTTP requests 
from bs4 import BeautifulSoup   # Python package for pulling data out of HTML and XML files
import pandas as pd             # Python package for data manipulation and analysis
import re                       # regular expressions
import json                     # Python package used to work with JSON data
from tqdm import tqdm           # python for displaying progressbar 
from datetime import datetime   # python package to retireve DateTime
url = 'https://www.billboard.com/charts/hot-100'              
url_text = requests.get(url).text                    # Get the session text for the link
url_soup = BeautifulSoup(url_text, 'html.parser')   # Get data from the HTML

Ranking = url_soup.find_all("span", class_ ="chart-element__rank__number")
Song_Name = url_soup.find_all("span", class_ ="chart-element__information__song")
Artist_Name=url_soup.find_all("span", class_ ="chart-element__information__artist")


dataframe_columns = [ 'Ranking', 'Song_Name' , 'Artist_Name']
dataframe = pd.DataFrame(columns=dataframe_columns)

for f,b,i,l in zip(Ranking, Song_Name, Artist_Name, range(0,len(Artist_Name))):
    dataframe.at[l,'Ranking'] = f.text
    dataframe.at[l,'Song_Name'] = b.text
    dataframe.at[l,'Artist_Name'] = i.text

print(dataframe.head(10))

