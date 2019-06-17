# 배열 인덱싱(fancy indexing)

import numpy as np

# booleam 인덱싱 --참, 거짓값을 골라냄

a=np.array([0,1,2,3,4,5,6,7,8,9])
idx=np.array([True, False,True, False,True, False,True, False,True, False])

print(a[idx])


# ------- 조건식 불리언 인덱싱
print(a%2 ==0)
print(a[a%2 ==0])

# 정수 배열 인덱싱
a=np.array([11,22,33,44,55,66,77,88,99])
idx=np.array([0,2,4,6,8])

print(a[idx])

# --------------------------------

idx=np.array([0,0,0,0,0,1,1,1,1,1,2,2,2,2,2])
print(a[idx])

# 다 차원 배열 인덱싱
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
print(a[:,[True,False,False,True]])










