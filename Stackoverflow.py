import requests                 # Simpler HTTP requests 
from bs4 import BeautifulSoup   # Python package for pulling data out of HTML and XML files
import pandas as pd             # Python package for data manipulation and analysis
import re                       # regular expressions
import string

Question=[]
No_Of_Votes=[]
No_Of_Accepted_Answers=[]
Views=[]

for i in range(1,42481):
    url = "https://stackoverflow.com/questions?tab=votes&page={}".format(i)             
    url_text = requests.get(url).text                    # Get the session text for the link
    url_soup = BeautifulSoup(url_text, 'html.parser')   # Get data from the HTML

    Question.append(url_soup.find_all(lambda tag: tag.name == 'a' and tag.get('class') == ['question-hyperlink']))
    No_Of_Votes.append(url_soup.find_all("span",class_="vote-count-post"))
    No_Of_Accepted_Answers.append(url_soup.find_all("div",class_='status answered-accepted'))
    Views.append(url_soup.find_all("div",class_='views'))

Question = [item for sublist in Question for item in sublist]
No_Of_Votes = [item for sublist in No_Of_Votes for item in sublist]
No_Of_Accepted_Answers=[item for sublist in No_Of_Accepted_Answers for item in sublist]
Views=[item for sublist in Views for item in sublist]

dataframe_columns = [ 'Question', 'No of Votes', 'No of accepted answers', 'Views'] 
dataframe = pd.DataFrame(columns=dataframe_columns)
for f, b, i ,j, k in zip(Question,No_Of_Votes,No_Of_Accepted_Answers,Views, range(0,len(Views))):
    dataframe.at[k,'Question'] = f.text
    dataframe.at[k,'No of Votes'] = b.text
    dataframe.at[k,'No of accepted answers'] = i.text.strip().replace("answers","")
    dataframe.at[k,'Views'] = j['title'].replace("views","")

dataframe.to_csv("Stackoverflow.csv")
