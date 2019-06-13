# 시리즈와 딕셔너리 자료형
# 시리즈 객체는 라벨에 의해 인덱싱이 가능하므로
# 딕셔너리와 유사
# in 연산, item 메서들를 사용해서 인덱스, 밸루에 접근 가능

import pandas as pd
import step09_데이터분석.pandasex.pandasEx01 as ex01
print('--------------------------------------------')
print('서울' in ex01.city)
print('광주' in ex01.city)

for k,v in ex01.city.items():
    print("%s=%d" %(k,v))

print('--------딕셔너리 객체에서 시리즈 생성--------')
# 2015년 지역별 인구수
city = pd.Series({"서울":10022181,"대전":1518775,
                  "대구":2487829,"부산":3513777})

print(city)
print()
city = pd.Series({"서울":10022181,"대전":1518775,
                  "대구":2487829,"부산":3513777},
                 index=["서울","대전","대구","부산"])

print(city)
print("----------------인덱스 기반 연산1----------------------")
# 2015~2017년 인구 증가 계산
# 각 시리즈의 차이, 인덱스가 같은 데이터에 대해서만 차이를 계산

dist=ex01.city -city
print("지역별 인구 증감수\n", dist)
# --------------------------- 시리즈 값만 계산
dist=ex01.city.values-city.values
print("지역별 인구 증감수(values)\n", dist)

print("----------------인덱스 기반 연산2----------------------")

city = pd.Series({"서울":10022181,"대전":1518775,
                  "대구":2487829,"부산":3513777},
                 index=["대전","서울","대구","부산"])
print(city)
# --------------------------- 시리즈 값만 계산
dist_x=ex01.city.values-city.values
print("지역별 인구 증감수(values)\n", dist_x) # 정상적인 값이 나오지 않음

print("----------------인덱스 기반 연산3----------------------")

city = pd.Series({"서울":10022181,"대전":1518775,
                  "대구":2487829,"부산":3513777},
                 index=["서울","대전","대구","부산","인천"])
print(city)
# --------------------------- 시리즈 값만 계산
dist_x=ex01.city-city
print("지역별 인구 증감수\n", dist_x) #float64 : 인천의 NaN 때문

print("----------------인덱스 기반 연산4----------------------")
print(dist_x.notnull())    #bool 연산 수행

print(dist_x[dist_x.notnull()])   # Ture, dist_x 의 and 연산 수행

print("----------------인구 증가율 계산----------------------")
ratio=(ex01.city-city)/city *100
ratio=ratio[ratio.notnull()]

print("            단위(%)\n",ratio)

print("----------------인덱싱을 이용한 데이터 갱신 추가----------------------")
ratio['부산']=-1.23
print(ratio)

ratio['인천']=5.09
print(ratio)

print("----------------인덱싱을 이용한 데이터 삭제----------------------")
del ratio['서울']
print(ratio)










