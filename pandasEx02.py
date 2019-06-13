# 시리즈 연산 : numpy 처럼 벡터화 연산 가능
#             연산의 대상은 values 에만 적용, index 값이 불변
import pandas as pd
import step09_데이터분석.pandasex.pandasEx01 as ex01

div = ex01.city / 1000000
print( "div\n",div)
print("------시리즈 인덱싱------")

# 배열 인덱싱이나 인데스 라벨을 이용한 인덱싱 가능
print("대전:",ex01.city[1],ex01.city["대전"])
print("부산:",ex01.city[3],ex01.city["부산"])
print()
# 배열 인덱싱을 이용할 경우 자료의 순서 변경이 가능, 특정 자료 선택이 가능
print(ex01.city[[0,3,1]])
# same as
print(ex01.city[["서울","부산","대전"]])
print('-------------------------------------')
print(ex01.city[(ex01.city>200e4)&(ex01.city<400e4)])

# 슬라이싱
print(ex01.city[1:3])    #마지막 값은 exclusive
print(ex01.city['대전':"대구"])   #마지막 값은 inclusive

print("대전 :",ex01.city.대전)















