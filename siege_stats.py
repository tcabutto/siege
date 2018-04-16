import bs4
import requests
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://r6stats.com/stats/uplay/Reload316/ranked'

def extract_source(url):
     agent = {"User-Agent":"Mozilla/5.0"}
     source=requests.get(url, headers=agent).text
     return source

def extract_data(source):
     soup=bs4.BeautifulSoup(source, 'lxml')
     names=soup.find_all('div')
     for i in names:
     print i

extract_data(extract_source(my_url))

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "lxml")