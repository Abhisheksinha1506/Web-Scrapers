import requests 
from bs4 import BeautifulSoup

#import time
#import random as rand 

import pandas as pd

dataframe_columns = ['Ranking', 'Movie_Title','Rating', 'Summary' , 'Movie Certificate' , 'Release Date' ]
dataframe = pd.DataFrame(columns=dataframe_columns)
Ranking=[]
Movie_Title=[]
Rating=[]
Summary=[]
Movie_Certification=[]
Release_Date=[]

for page in range(0,2): #Remember to update the number of pages 
    url = 'https://www.metacritic.com/browse/movies/score/metascore/all/filtered?page='+str(page)
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response  = requests.get(url, headers = user_agent)
    #time.sleep(rand.randint(3,30)) 
    soup = BeautifulSoup(response.text, 'html.parser')

    for detail in soup.find_all('td', class_='clamp-summary-wrap'):
        Ranking.append(detail.find('span', class_='title numbered').text.strip())
        Movie_Title.append(detail.find('a', class_='title').find('h3').text.strip())
        Rating.append(detail.find('a', class_='metascore_anchor').text.strip())
        Summary.append(detail.find('div', class_='summary').text.strip())
        Movie_Certification.append(detail.find('div', class_='clamp-details').contents[-2].text.replace("| ",""))
        Release_Date.append(detail.find('div', class_='clamp-details').find('span').text)

    for f, b, i , j , k, m, l in zip(Ranking, Movie_Title, Rating, Summary , Movie_Certification, Release_Date,  range(0,len(Ranking))):
        dataframe.at[l,'Ranking'] = f
        dataframe.at[l,'Movie_Title'] = b
        dataframe.at[l,'Rating'] = i
        dataframe.at[l,'Summary'] = j
        dataframe.at[l,'Movie Certificate'] = k
        dataframe.at[l,'Release Date'] = m


    
