import requests
from bs4 import BeautifulSoup
import time
import random

''' Get random image from xkcn.info
    - get random page at http://xkcn.info/page/{ramdom}
    - get random post in a list
    - get content of post
'''

def getRandomImg():
    page = int(time.time()) % 20
    pageURL = "http://xkcn.info/page/%s" % page
    r = requests.get(pageURL)
    pageHTML = BeautifulSoup(r.text, 'html.parser')
    homePageHTML = pageHTML.find(id='homePage')
    allAnchor = homePageHTML.find_all('a', {'class': ''})
    links = []
    for anchor in allAnchor:
        links.append(anchor.get('href'))
    postURL = random.choice(links)
    r = requests.get(postURL)
    postHTML = BeautifulSoup(r.text, 'html.parser')
    img = postHTML.find(id='homePage').find('div', {'class':'gridItem'}).get("data-photo-high")
    return img
