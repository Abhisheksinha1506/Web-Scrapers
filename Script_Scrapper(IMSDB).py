import requests                 # Simpler HTTP requests 
from bs4 import BeautifulSoup   # Python package for pulling data out of HTML and XML files
import pandas as pd             # Python package for data manipulation and analysis

url = 'https://imsdb.com/scripts/A-Quiet-Place.html'              
url_text = requests.get(url).text                    # Get the session text for the link
url_soup = BeautifulSoup(url_text, 'html.parser')   # Get data from the HTML

Script=url_soup.find_all("td", class_ ="scrtext")

Name=Script[0].find("td").contents[2].text.strip().split("Writers")[0].strip()

Final_Script=Script[0].find("pre").text

file = open(Name + ".txt","w")
file.writelines(Final_Script)
file.close() #to change file access modes


