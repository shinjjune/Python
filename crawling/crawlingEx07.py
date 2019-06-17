"""
[문제] https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190107

 네이버 영화 랭킹 평점순(모든영화)의 주소를 참조하여 크롤링하고 조회된 순서대로 출력하세요
 --출력
 베일리 어게인
 보헤미안 랩소디
        :

"""
from bs4 import BeautifulSoup
from urllib import request
import urllib

soup=BeautifulSoup(urllib.request.urlopen(
    'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190613').read(),'html.parser')

# print(soup)
# print(soup.find_all('div','tit5'))   # 뽑아낼때 중점적으로..
for i in soup.find_all('div','tit5'):
    print(i.find('a').get('title'))


# print(soup.find('div',{'class':'tit5'}).find('a').get('title'))





