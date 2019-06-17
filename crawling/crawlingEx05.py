import requests

text=" "
req=requests.get("http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
source=req.text

while(1):
    source = source[source.find('<'):]    # < 검색
    if source.find('<!--') ==0:
        source =source[source.find('-->')+3:]   # 주석의 내용을 건너 뛰기
    elif source.find('<script>') ==0:
        source =source[source.find('</script>')+9:]  # 자바스크립트 내용을 건너뛰기
    else:
        source=source[source.find('>')+1:]   # > 을 찾는다
        for ch in source: # > 이후부터 한글자씩 추출
            if ch =='<':
                break
            elif ch == '\t' or ch== '\n':  # 탭과 개행 문자는 텍스트에 포함 시키지 않음
                continue
            else:
                text +=ch
        if text.endswith(' ') ==False:
            text += " "     # 순수 텍스트를 추출하기 위해 공백으로 분리
    if(source.find('<')==-1):
        break   # < 문자가 더이상 없는 경우 무한 루프 종료

lst=text.split()
print(lst)
print(len(lst))















