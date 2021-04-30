import requests 
from bs4 import BeautifulSoup

#import time
#import random as rand 

import pandas as pd

dataframe_columns = ['Ranking', 'Game_Title','Date', 'Rating' , 'Platform' , 'Summary' ]
dataframe = pd.DataFrame(columns=dataframe_columns)
Ranking=[]
Game_Title=[]
Rating=[]
Platform=[]
Summary=[]
Date=[]

for page in range(0,2): #Remember to update the number of pages 
    url = 'https://www.metacritic.com/browse/games/score/userscore/90day/filtered?page='+str(page)
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response  = requests.get(url, headers = user_agent)
    #time.sleep(rand.randint(3,30)) 
    soup = BeautifulSoup(response.text, 'html.parser')

    for detail in soup.find_all('td', class_='clamp-summary-wrap'):
        Ranking.append(detail.find('span', class_='title numbered').text.strip())
        Game_Title.append(detail.find('a', class_='title').find('h3').text.strip())
        Rating.append(detail.find('a', class_='metascore_anchor').text.strip())
        Platform.append(detail.find('div', class_='platform').find('span', class_="data").text.strip())
        Summary.append(detail.find('div', class_='summary').text.strip())
        Date.append(detail.find('div', class_='clamp-details').contents[-2].text)
    for f, b, i , j , k, m, l in zip(Ranking, Game_Title, Rating, Platform, Summary , Date, range(0,len(Ranking))):
        dataframe.at[l,'Ranking'] = f
        dataframe.at[l,'Game_Title'] = b
        dataframe.at[l,'Date'] = m
        dataframe.at[l,'Rating'] = i
        dataframe.at[l,'Platform'] = j
        dataframe.at[l,'Summary'] = k
