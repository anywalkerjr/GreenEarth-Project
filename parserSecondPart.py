from bs4 import BeautifulSoup as BS
import requests
import pandas as pd
def parasingLink(url):
    r = requests.get(url)

    bs = BS(r.content, "html.parser")

    
    temp = bs.find('text').find_all('p')
    text = ''
    for p in temp:  
        text += p.prettify(formatter="minimal")
    
    newsInfo = bs.find('newsinfo').text
    
    dict_news = {"title": bs.find('div', 'news_view_title').find('h1').text, 
                 "text": text.replace('\xa0', ' '), 
                 "views": (newsInfo[23:]).replace('\n\t/ Источник / \n\tПоделиться: \n', '').replace('👁 ','').replace('\n\t / \n\tПоделиться: \n', ''), 
                 "date": (newsInfo[:18]).replace('\n\t', '')
                 
    }
    return dict_news
