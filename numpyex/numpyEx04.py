# 배열의 차원과 크기 알아내기
# ndim : 배열의 차원 반환, shape : 배열의 크기 반환

import numpy as np
import step09_데이터분석.numpyex.numpyEx03 as ex03

# 1차원 배열의 속성
a=np.array([1,2,3])
print(a.ndim)
print(a.shape)


# 2차원 배열의 속성
c=np.array([[1,2,3],[4,5,6]])
print(c.ndim)
print(c.shape)

# 3차원 배열의 속성
print("차원 :",ex03.d.ndim)
print("크기 :",ex03.d.shape)












