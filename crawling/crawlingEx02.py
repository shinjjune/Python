import requests as req

def get_html(url):
    html = ""
    res = req.get(url)
    if res.status_code ==200:
        html= res.text
        return html

from bs4 import BeautifulSoup

url='https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190601'
html = get_html(url)
soup = BeautifulSoup(html,'html.parser')
print(soup)