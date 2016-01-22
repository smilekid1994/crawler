import requests
from bs4 import BeautifulSoup
import time
import random

''' Get random image from http://www.truyencuoihay.vn/
    - get random page at http://www.truyencuoihay.vn/?pagenumber=1
    - get random post in a list
    - get content of post
'''

def getRandomStory():
    page = int(time.time()) % 20
    pageURL = "http://www.truyencuoihay.vn/?pagenumber=%s" % page
    r = requests.get(pageURL)
    r.encoding = 'utf-8'
    pageHTML = BeautifulSoup(r.text, 'html.parser')
    divs = pageHTML.find_all('div', {'class': 'item-box'})
    div = random.choice(divs)
    des = div.find('div',{'class': "description"}).text
    title = div.find('h2', {'class':"product-title"}).text
    story = "%s\n%s" % (title, des)
    return story
