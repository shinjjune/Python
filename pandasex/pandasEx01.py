# pandas : 표, 데이터를 다루기 위한  Series 클래스
#           DataFrame 클래스를 제공
# 파이썬에서 사용하는 엑셀

# 시리즈 데이터 : 데이터를 1차원 배열이나 리스트의 형식으로 표현한 것을
#   시리즈 클래스 생성자에 넣어 주면 시리즈 클래스 객체 생성
import pandas as pd
# 2017년 지역별 인구수
city = pd.Series([9857426, 1502227, 2475231, 3470635],
                 index=["서울","대전","대구","부산"])
# index : 인덱스 라벨(문자, 정수, 시간, 날짜)

print(type(city))
print("시리즈 데이터\n", city)

print("인덱스 :",city.index)
print("값 :",city.values)

city.name="지역별 인구수"
# city.index.name="도시"
print(city)







