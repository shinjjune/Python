import numpy as np

x=np.array([1,2,3])

print(type(x))
print(x.dtype)    # 만들어진 배열의 자료형

x=np.array([1.0,2.0,3.0])
print(x.dtype)
print("------------------------------")

x=np.array([1,2,3],dtype='f')
print(x.dtype)

"""
dtype='접두사'
b   불리언
i   정수
f   부동소수점   f8
O   객체
U   유니코드 문자열    U24
"""

# Inf(infinity), NaN(Not a Number)
# Inf : 무한대 1을 0으로 나누려고 하는 경우
# NaN : 0을 0으로 나누는 경우

z=np.array([0,1,-1,0]/np.array([1,0,0,0]))
print(z)






