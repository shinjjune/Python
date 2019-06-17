# 벡터화 연산(사칙연산)
import numpy as np

x=np.arange(1,10001)
y=np.arange(10001,20001)

# numpy 벡터화 연산
z=x+y
print(z)

# for 문
k=np.zeros_like(x)
for i in range(10000):
    k[i]=x[i]+y[i]

print(k)











