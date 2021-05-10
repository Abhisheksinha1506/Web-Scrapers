import requests                 # Simpler HTTP requests 
from bs4 import BeautifulSoup   # Python package for pulling data out of HTML and XML files
import pandas as pd             # Python package for data manipulation and analysis

url = 'https://www.rottentomatoes.com/browse/opening'              
url_text = requests.get(url).text                    # Get the session text for the link
url_soup = BeautifulSoup(url_text, 'html.parser')   # Get data from the HTML

Tomato_meter = url_soup.find_all("span", class_ ="tMeterScore")
Movie_name = url_soup.find_all("div", class_ ="media-list__title")
Cast=url_soup.find_all("p", class_ ="media-list__actors")
Rating=url_soup.find_all("p", class_ ="media-list__other_info")

dataframe_columns = [ 'Movie_Title', 'Cast' , 'Rating&Duration' , 'Rotten Tomatoes' ]
dataframe = pd.DataFrame(columns=dataframe_columns)
for f,b,i,k,l in zip(Movie_name, Cast, Rating, Tomato_meter, range(0,len(Cast))):
    dataframe.at[l,'Movie_Title'] = f.text
    dataframe.at[l,'Cast'] = b.text.replace("\n","")
    dataframe.at[l,'Rating&Duration'] = i.text.replace(" ","").replace("\n"," ")
    dataframe.at[l,'Rotten Tomatoes'] = k.text

print(dataframe.head(10))

