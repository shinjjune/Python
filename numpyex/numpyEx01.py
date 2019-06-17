# numpy 넘파이 : 수치해석용 파이선 패키지
# ndarray : 다차원 배열 자료구조 클래스를 지원
# 선형 대수 계산

import numpy as np

# 1차원 배열 생성
ar=np.array([0,1,2,3,4,5,6,7,8,9])

print(ar)
# -----------------------------------------------
data=[0,1,2,3,4,5,6,7,8,9]


# 1. for 문 사용
answer=[]
for di in data :
    answer.append(2*di)
print("data의 배수 :", answer)

# 2. 벡터화 연산
x=np.array(data)
print("벡터화 연산 :", 2*x)

# 3. 벡터화 연산
a=np.array([1,2,3])
b=np.array([10,20,30])

print(2*a+b)
print("a는 2인가? ;",a==2)
print("b는 10보다 큰가?",b>10)
print((a==2)&(b>10))








