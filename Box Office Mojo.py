import requests                 # Simpler HTTP requests 
from bs4 import BeautifulSoup   # Python package for pulling data out of HTML and XML files
import pandas as pd             # Python package for data manipulation and analysis

url = 'https://www.boxofficemojo.com/year/world/?ref_=bo_nb_bns_tab'              
url_text = requests.get(url).text                    # Get the session text for the link
url_soup = BeautifulSoup(url_text, 'html.parser')   # Get data from the HTML

Ranking = url_soup.find_all("td", class_ ="a-text-right mojo-header-column mojo-truncate mojo-field-type-rank mojo-sort-column")
Movie_Name = url_soup.find_all("td", class_ ="a-text-left mojo-field-type-release_group")
WorldWide=url_soup.find_all("td", class_ ="a-text-right mojo-field-type-money")

World=[]
for colle in WorldWide:
    World.append(colle)

dataframe_columns = [ 'Ranking', 'Movie_Name' , 'WorldWide Collection', 'Domestic Collection' ,'Foreign Collection']
dataframe = pd.DataFrame(columns=dataframe_columns)
for f,b,l in zip(Ranking, Movie_Name, range(0,len(WorldWide))):
    dataframe.at[l,'Ranking'] = f.text
    dataframe.at[l,'Movie_Name'] = b.text

for i,j in zip(range(0,len(WorldWide)),range(0,len(World),3)):
    dataframe.at[i,'WorldWide Collection'] = World[i].text
    dataframe.at[i,'Domestic Collection'] = World[i+1].text
    dataframe.at[i,'Foreign Collection'] = World[i+2].text

print(dataframe.head(10))