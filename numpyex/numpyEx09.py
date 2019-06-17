import numpy as np

# 전치 연산-------------------------------------
ar=np.array([[1,2,3],[4,5,6]])
print(ar)

print(ar.T)   # 전치연산 T속성 사용

# 배열의 형태 변경-------------------------------
a=np.arange(12)
print(a)

b=a.reshape(3,4)
print(b)

print(a.reshape(4,-1))
# print(a.reshape(5,-1))  #정상적인 처리 안됨, 결과 없음

print(a.reshape(2,2,-1))

# 다차원 배열에서 1차원 배열로 펼치기
print(b.flatten())
print(b.ravel())

# --------------------------------------------
x=np.arange(5)
print(x)
print(x[:,np.newaxis])  #X배열에 대해서 차원을 1증가






