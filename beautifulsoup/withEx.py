# 파일 입출력
from bs4 import BeautifulSoup

file= open('sample.html',encoding='utf-8')
print(file.readline(),end='')
file.close()

with open('sample.html',encoding='utf-8') as file:
    print(file.readline(),end='')

# find() : 태그의 이름, 속성......
# find_all() : 전부다 검색
# ------------------------------------------------
print('========= div 태그 전부=========')
with open("sample.html",encoding='utf-8') as fp:
    soup= BeautifulSoup(fp,'html.parser')

    all_div=soup.find_all("div")
    print(all_div)

print('----------------------------------------')
print('========= div 태그 한개=========')
with open("sample.html",encoding='utf-8') as fp:
    soup= BeautifulSoup(fp,'html.parser')

    one_div=soup.find("div")
    print(one_div)

print('----------------------------------------')
print('========= 모든 p 태그 ========')
with open("sample.html",encoding='utf-8') as fp:
    soup= BeautifulSoup(fp,'html.parser')

    all_p=soup.find_all("p")
    print(all_p)





