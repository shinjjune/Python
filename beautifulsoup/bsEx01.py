# BeautifulSoup : 파이썬 3 버전에서는 beautifulsoup4 설치

from bs4 import BeautifulSoup

with open('sample.html', encoding='utf-8') as fp:
    soup=BeautifulSoup(fp,'html.parser')

print(soup)











