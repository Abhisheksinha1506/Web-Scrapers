import requests                 # Simpler HTTP requests 
from bs4 import BeautifulSoup   # Python package for pulling data out of HTML and XML files
import pandas as pd             # Python package for data manipulation and analysis
import re                       # regular expressions
import json                     # Python package used to work with JSON data
from tqdm import tqdm           # python for displaying progressbar 
from datetime import datetime   # python package to retireve DateTime
url = 'https://www.billboard.com/charts/artist-100'              
url_text = requests.get(url).text                    # Get the session text for the link
url_soup = BeautifulSoup(url_text, 'html.parser')   # Get data from the HTML

Ranking = url_soup.find_all("div", class_ ="chart-list-item__rank")
Artist_Name = url_soup.find_all("span", class_ ="chart-list-item__title-text")
Peak_Position=url_soup.find_all("div", class_ ="chart-list-item__weeks-at-one")
Weeks_On_Chart=url_soup.find_all("div", class_ ="chart-list-item__weeks-on-chart")

dataframe_columns = [ 'Ranking', 'Artist_Name' , 'Peak_Position', 'Weeks_On_Charts']
dataframe = pd.DataFrame(columns=dataframe_columns)

for f,b,i,k,l in zip(Ranking, Artist_Name,Peak_Position,Weeks_On_Chart, range(0,len(Artist_Name))):
    dataframe.at[l,'Ranking'] = f.text.strip()
    dataframe.at[l,'Artist_Name'] = b.text.strip()
    dataframe.at[l,'Peak_Position'] = i.text.strip()
    dataframe.at[l,'Weeks_On_Charts'] = k.text.strip()


print(dataframe.head(10))


