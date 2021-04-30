import requests                 # Simpler HTTP requests 
from bs4 import BeautifulSoup   # Python package for pulling data out of HTML and XML files
import pandas as pd             # Python package for data manipulation and analysis
import re                       # regular expressions
import json                     # Python package used to work with JSON data
from tqdm import tqdm           # python for displaying progressbar 
from datetime import datetime   # python package to retireve DateTime
url = 'https://editorial.rottentomatoes.com/guide/oscars-best-and-worst-best-pictures/'              
url_text = requests.get(url).text                    # Get the session text for the link
url_soup = BeautifulSoup(url_text, 'html.parser')   # Get data from the HTML

Ranking = url_soup.find_all("div", class_ ="countdown-index")
Movie_info = url_soup.find_all("div", class_ ="article_movie_title")
Year=url_soup.find_all("span", class_ ="subtle start-year")
Rotten_Score=url_soup.find_all("span", class_ ="tMeterScore")
Adj_Score=url_soup.find_all("div", class_ ="info countdown-adjusted-score")

dataframe_columns = ['Ranking', 'Movie_Title', 'Year' , 'Rotten Score' , 'Adjusted Score' ]
dataframe = pd.DataFrame(columns=dataframe_columns)
for f,b,i,e,k,l in zip(Ranking, Movie_info, Year, Rotten_Score, Adj_Score, range(0,len(Adj_Score))):
    dataframe.at[l,'Ranking'] = f.text
    dataframe.at[l,'Movie_Title'] = (b.text.strip(" "))[:-4].strip("\n")
    dataframe.at[l,'Year'] = i.text
    dataframe.at[l,'Rotten Score'] = e.text
    dataframe.at[l,'Adjusted Score'] = k.text.replace("Adjusted Score: ","")

print(dataframe.head(10))
