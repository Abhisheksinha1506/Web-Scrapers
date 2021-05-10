import requests                 # Simpler HTTP requests 
from bs4 import BeautifulSoup   # Python package for pulling data out of HTML and XML files
import pandas as pd             # Python package for data manipulation and analysis
import re                       # regular expressions

url = 'https://www.imdb.com/chart/boxoffice'              
url_text = requests.get(url).text                    # Get the session text for the link
url_soup = BeautifulSoup(url_text, 'html.parser')   # Get data from the HTML

movie_title = url_soup.find_all("td", class_ ="titleColumn")
gross_collection = url_soup.find_all("td", class_ ="ratingColumn")
collection=[]
for i in gross_collection:
    a=i.text.strip()
    collection.append(a)
weeks = url_soup.find_all("td", class_ ="weeksColumn")
dataframe_columns = [ 'Movie Name', 'Weekend Collection', 'Gross Collection' 'Weeks']
dataframe = pd.DataFrame(columns=dataframe_columns)
for f, j ,k in zip(movie_title, weeks, range(0,len(movie_title))):
    movie_name= re.sub(r" ?\([^)]+\)", "", f.text)
    dataframe.at[k,'Movie Name'] = movie_name.replace("\n",'')
    dataframe.at[k,'Weekend Collection'] = collection.pop(0)
    dataframe.at[k,'Gross Collection'] = collection.pop(0)
    dataframe.at[k,'Weeks'] = j.text
    
del dataframe['Gross CollectionWeeks']
print(dataframe.head(10))


    