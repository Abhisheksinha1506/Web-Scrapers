import requests                 # Simpler HTTP requests 
from bs4 import BeautifulSoup   # Python package for pulling data out of HTML and XML files
import pandas as pd             # Python package for data manipulation and analysis
import re                       # regular expressions
import string
Gems_Name=[]
Gems_desc=[]
No_of_downloads=[]
All_page=list(string.ascii_uppercase)
for i in All_page:
    url = "https://rubygems.org/gems?letter={}".format(i)             
    url_text = requests.get(url).text                    # Get the session text for the link
    url_soup = BeautifulSoup(url_text, 'html.parser')   # Get data from the HTML

    Last_Page=str(url_soup.find_all("span", class_="last"))
    Last_Page=re.findall(r'\d+', Last_Page)[0]
    for j in range(1,int(Last_Page)+1):
        url = "https://rubygems.org/gems?letter={}&page={}".format(i,j)             
        url_text = requests.get(url).text                    # Get the session text for the link
        url_soup = BeautifulSoup(url_text, 'html.parser')   # Get data from the HTML
        Gems_Name.append(url_soup.find_all("h2",class_="gems__gem__name"))
        Gems_desc.append(url_soup.find_all("p",class_="gems__gem__desc t-text"))
        No_of_downloads.append(url_soup.find_all("p",class_="gems__gem__downloads__count"))
    print("Done with {} at {}".format(i,j))

Gems_Name = [item for sublist in Gems_Name for item in sublist]
Gems_desc = [item for sublist in Gems_desc for item in sublist]
No_of_downloads=[item for sublist in No_of_downloads for item in sublist]

dataframe_columns = [ 'Gem Name', 'Gem Description', 'No of Downloads']
dataframe = pd.DataFrame(columns=dataframe_columns)
for f, b, i ,k in zip(Gems_Name,Gems_desc,No_of_downloads, range(0,len(Gems_Name))):
    dataframe.at[k,'Gem Name'] = f.text.strip().replace(" ","").split("\n")[0]
    dataframe.at[k,'Gem Description'] = b.text
    dataframe.at[k,'No of Downloads'] = i.text.replace("Downloads","").strip()

dataframe.to_csv("Rubygems.csv")

