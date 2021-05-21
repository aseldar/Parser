import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


def get_data(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.2.193 Yowser/2.5 Safari/537.36"
    }

    # req = requests.get(url, headers)
    
    # with open('article.html', 'w', encoding='utf-8') as file:
    #     file.write(req.text)



    with open('article.html', encoding='utf-8') as file:
        src = file.read()
        
    soup = BeautifulSoup(src, 'lxml')
    headers2 = soup.find_all('h2')
    contetns = soup.find_all('p')
    for h2 in contetns:
        print(h2.text)



        # try:
        #     print(cleanhtml(h2))
        # except TypeError:
        #     pass



get_data('https://m.lenta.ru/articles/2021/04/29/latin/')