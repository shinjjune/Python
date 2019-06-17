from bs4 import BeautifulSoup
print("----------------태그와 속성을 이용해서 가져오기--------------------")

# find_all('태그명', {'속성명':'값'...})
# find('태그명', {'속성명':'값'...})

with open('sample.html', encoding='utf-8') as fp:
    soup = BeautifulSoup(fp,'html.parser')
#     div 안에 있는 id 속성이 sample_id 인 것
    sample_div_id = soup.find('div',{'id':'sample_id'})
    print(sample_div_id)
#     print(type(soup))

print('--------------- html 구조를 이용해서 일부 가져오기 -----------------')
with open('sample.html', encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    sample_div_id = soup.find('div',{'id':'sample_id'})
    sample_p= sample_div_id.find_all('p')
    print(sample_p)

    allp=soup.find_all('p')
    print(allp)


















