import requests                 # Simpler HTTP requests 
from bs4 import BeautifulSoup   # Python package for pulling data out of HTML and XML files
import pandas as pd             # Python package for data manipulation and analysis
import re                       # regular expressions
import json                     # Python package used to work with JSON data
from tqdm import tqdm           # python for displaying progressbar 
from datetime import datetime   # python package to retireve DateTime

Lang=input('Please input a Language: ')
url = 'https://github.com/search?o=desc&q={}&s=stars&type=Repositories'.format(Lang)         
url_text = requests.get(url).text                    # Get the session text for the link
url_soup = BeautifulSoup(url_text, 'html.parser')   # Get data from the HTML

Repo_name=url_soup.find_all("a",attrs={"class" : "v-align-middle"})
Repo_details=url_soup.find_all("p",attrs={"class" : "mb-1"})
Stars=url_soup.find_all(lambda tag: tag.name == 'a' and tag.get('class') == ['Link--muted'])
Primary=url_soup.find_all("span",attrs={"itemprop" : "programmingLanguage"})

dataframe_columns = [ 'Repo Name', 'Stars' , 'Primary', 'Details']
dataframe = pd.DataFrame(columns=dataframe_columns)
for f, b, i,k ,j in zip(Repo_name, Repo_details, Stars, Primary, range(0,len(Repo_name))):
    dataframe.at[j,'Repo Name'] = f.text.strip()
    dataframe.at[j,'Details'] = b.text.strip()
    dataframe.at[j,'Stars'] = i.text.strip()
    dataframe.at[j,'Primary'] = k.text.strip()

print(dataframe.head(10))

