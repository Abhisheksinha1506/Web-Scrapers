import requests
from lxml import html
from fake_useragent import UserAgent
from w3lib.html import remove_tags


s = requests.Session()
ua = UserAgent()
s.headers.update({
    'User-Agent': ua.random
})

login_resp = s.get(url='https://mobile.twitter.com/login')
login_tree = html.fromstring(html=login_resp.content)
authenticity_token = login_tree.xpath("//input[@name='authenticity_token']/@value")[0]

data = {
    'authenticity_token': authenticity_token,
    'session[username_or_email]': '',
    'session[password]': '',
    'remember_me': '1',
    'wfa': '1',
    'commit': 'Log in',
    'ui_metrics': ''
}

s.post(url='https://mobile.twitter.com/sessions', data=data, headers={
    'referer': 'https://mobile.twitter.com/login',
    'content-type': 'application/x-www-form-urlencoded'
})

trump_resp = s.get(url='https://mobile.twitter.com/realDonaldTrump?p=s', headers={
    'referer': 'https://mobile.twitter.com/login'
})

trump_tree = html.fromstring(html=trump_resp.content)
last_tweet = remove_tags(html.tostring(trump_tree.xpath("//div[@class='tweet-text']/div")[0]))
print(last_tweet)
