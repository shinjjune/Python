# http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108

from urllib import request
import urllib

from bs4 import BeautifulSoup

# urlopen() 로 기상청 전국 중기 날씨 읽기
target=urllib.request.urlopen("http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

# print(target)

soup=BeautifulSoup(target,"html.parser")
# print(soup)

for location in soup.select('location'):
    print("도시 :", location.select_one('city').string)
#     날씨, 아침최저기온, 낮최고기온











