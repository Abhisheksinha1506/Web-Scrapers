  
import requests                 # Simpler HTTP requests 
from bs4 import BeautifulSoup   # Python package for pulling data out of HTML and XML files
import pandas as pd             # Python package for data manipulation and analysis
import re                       # regular expressions


url = 'http://www.rajinikanthjokes.com/'  #Can be further extrapolated for mutiple pages 
url_text = requests.get(url).text                    # Get the session text for the link
url_soup = BeautifulSoup(url_text, 'html.parser')   # Get data from the HTML


Res_Quote=url_soup.find_all("font",attrs={"color" : "#660000"})

dataframe_columns = [ 'Quote']
dataframe = pd.DataFrame(columns=dataframe_columns)
for f, j in zip(Res_Quote, range(0,len(Res_Quote))):
    dataframe.at[j,'Quote'] = f.text.strip().replace("\n","").replace("\r","")
    

print(dataframe.head(10))    
