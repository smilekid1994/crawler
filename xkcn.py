import requests
#from bs4 import BeautifulSoup
#import time
#import random
import re

''' Get random image from xkcn.info
    - get random page at http://xkcn.info/page/{ramdom}
    - get random post in a list
    - get content of post
'''

def getRandomImg():
    pageURL = "http://xkcn.info/random"
    r = requests.get(pageURL)
    #pageHTML = BeautifulSoup(r.text, 'html.parser')
    '''
    homePageHTML = pageHTML.find(id='homePage')
    allAnchor = homePageHTML.find_all('a', {'class': ''})
    links = []
    for anchor in allAnchor:
        links.append(anchor.get('href'))
    postURL = random.choice(links)
    r = requests.get(postURL)
    postHTML = BeautifulSoup(r.text, 'html.parser')
    '''
    #imgTag = pageHTML.find_all('img', {'class': 'permalinkPrimaryPhoto'})
    imgTag = re.search(r'<img(.*?)class="permalinkPrimaryPhoto"(.*?)', r.text).group(0)
    imgUrl = re.search(r'src="(.*?)"', imgTag).group(1)
    return imgUrl
