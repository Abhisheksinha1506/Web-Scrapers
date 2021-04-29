import requests                 # Simpler HTTP requests 
from bs4 import BeautifulSoup   # Python package for pulling data out of HTML and XML files
import pandas as pd             # Python package for data manipulation and analysis
import re                       # regular expressions
import json                     # Python package used to work with JSON data
from tqdm import tqdm           # python for displaying progressbar 
from datetime import datetime   # python package to retireve DateTime

url = 'https://www.imdb.com/movies-in-theaters'              
url_text = requests.get(url).text                    # Get the session text for the link
url_soup = BeautifulSoup(url_text, 'html.parser')   # Get data from the HTML

rows = url_soup.find_all("tr")
movie_title = url_soup.find_all("h4")
generes = url_soup.find_all("p", class_ ="cert-runtime-genre")
run_time = url_soup.find_all("time")
desc = url_soup.find_all("div", class_ ="outline")
director_cast=url_soup.find_all("div", class_ ="txt-block")
director=[]
for d in director_cast:
    director.append(d.find('a', href=True).text)
    
del director[1::2]
dataframe_columns = [ 'Movie_Title', 'genre', 'runtime', 'desc']
dataframe = pd.DataFrame(columns=dataframe_columns)
for f, b, i , j , k, l in zip(movie_title, run_time, desc, director, generes , range(0,len(director))):
    dataframe.at[l,'Movie_Title'] = f.text
    dataframe.at[l,'genre'] = k.select_one("span").text
    dataframe.at[l,'runtime'] = b.text
    dataframe.at[l,'desc'] = i.text.strip("\n")
    dataframe.at[l,'director'] = j

print(dataframe.head(10))
