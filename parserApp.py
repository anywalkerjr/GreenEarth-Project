from bs4 import BeautifulSoup as BS
import requests
import pandas as pd
from parserSecondPart import parasingLink

def parsingNewsApp():

  url = 'https://ecoportal.su/news.html'

  r = requests.get(url)

  bs = BS(r.content, "html.parser")


  temp = bs.find_all('div', 'index_anons')

  latestNews = []

  for div in temp:
    latestNews.append(parasingLink('https://ecoportal.su' + (div.find('a').get('href'))))
  return latestNews

