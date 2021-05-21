import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


def get_data(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.2.193 Yowser/2.5 Safari/537.36"
    }

    # req = requests.get(url, headers)
    
    # with open('lentaAricles.html', 'w', encoding='utf-8') as file:
    #     file.write(req.text)
    # print(get_data('https://lenta.ru/parts/text/'))

    with open('lentaAricles.html', encoding='utf-8') as file:
        src = file.read()
        
    soup = BeautifulSoup(src, 'lxml')
    articles = soup.find_all('div', class_="item article")
    
    lst = []
    for art in articles:
        try:

            rubrica = art.find('div', class_='info g-date item__info').find('a', class_="rubric item__rubric").get_text()

            text_head = art.find('div', class_='titles').find('h3').get_text()


            project_url = art.find('a', class_='js-dh picture').get('href')
            date_art = project_url.split('/')[2] + '-'  + project_url.split('/')[3] + '-' + project_url.split('/')[4]
            project_url = 'https://m.lenta.ru' + project_url
            # print(date_art, text_head, rubrica, project_url )
            lst.append(
                { 
                    'Date': date_art,
                    'Rubrica': rubrica,
                    'Topic': text_head,
                    'URL': project_url
                })
                
        except:
            pass
            # text_head = 'no text'
            # rubrica = 'No rubrica'
            # date_art = '1900-01-01'
            # project_url = 'https://lenta.ru'
        # time.sleep(1)

        
        # print(art)
    df = pd.DataFrame(lst)
    print(df) 


get_data('https://lenta.ru/parts/text/')

# def scraper(urls):

#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.2.193 Yowser/2.5 Safari/537.36"
#     }

#     for url in urls:


#         req = requests.get(url, headers)
        
#         with open('lentaAricles.html', 'w', encoding='utf-8') as file:
#             file.write(req.text)
    