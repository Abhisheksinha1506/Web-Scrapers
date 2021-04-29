import requests                 # Simpler HTTP requests 
from bs4 import BeautifulSoup   # Python package for pulling data out of HTML and XML files
import pandas as pd             # Python package for data manipulation and analysis
import re                       # regular expressions
import json                     # Python package used to work with JSON data
from tqdm import tqdm           # python for displaying progressbar 
from datetime import datetime   # python package to retireve DateTime
url = 'https://www.imdb.com/chart/toptv'              # IMDb Top 250 list link
url_text = requests.get(url).text                    # Get the session text for the link
url_soup = BeautifulSoup(url_text, 'html.parser')   # Get data from the HTML

rows = url_soup.find_all("tr")
show_title = url_soup.find_all("td", class_ ="titleColumn")
imdb_rating = url_soup.find_all("td", class_ ="ratingColumn imdbRating")
dataframe_columns = [ 'Tv Show', 'year', 'rating']
dataframe = pd.DataFrame(columns=dataframe_columns)
for f, b, i in zip(show_title, imdb_rating,range(0,len(imdb_rating))):
    year = re.search('\(([^)]+)', f.text).group(1)
    show_name= re.sub(r" ?\([^)]+\)", "", f.text)
    show_name=show_name.split('.').pop(1)
    dataframe.at[i,'Tv Show'] = show_name.strip("\n")
    dataframe.at[i,'year'] = year.strip("\n")
    dataframe.at[i,'rating'] = b.text.strip("\n")
print(dataframe.head(10))


