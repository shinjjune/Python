import requests as req

# requests 모듈 : urllib(내장 라이브러리) 모듈을 편리하게 사용하도록 만든 것
# request.get('url',auth=('id','pass'))
# status_code --> 200
# encoding : 'utf-8'
# text

def get_html(url):
    html = ""
    res = req.get(url)
    if res.status_code ==200:
        html= res.text
        return html

from bs4 import BeautifulSoup

url='https://comic.naver.com/webtoon/detail.nhn?titleId=675554&no=702&weekday=mon'
html = get_html(url)
soup = BeautifulSoup(html,'html.parser')
print(soup)












