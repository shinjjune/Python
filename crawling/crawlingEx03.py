from bs4 import BeautifulSoup
from urllib import request
import urllib

soup=BeautifulSoup(urllib.request.urlopen(
    'https://movie.naver.com/movie/running/current.nhn').read(),'html.parser')
# print(soup)
print("예매순 1위 :", soup.find('ul',{'class':'top_thumb_lst'}).find('li').get('data-title'))

for i in soup.find('ul',{'class':'top_thumb_lst'}).find_all('li'):
    print(i.get('data-title'))




















