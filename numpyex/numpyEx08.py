import numpy as np

# zero : 배열 값을 0으로 초기화
z_ar=np.zeros(5)
print(z_ar)

# 다차원 배열 생성 : 인수에 튜플로 값을 지정
z_2dar=np.zeros((2,3),dtype='i')
print(z_2dar)

# 문자열 배열 생성
str_ar=np.zeros(5,dtype='U8')
str_ar[2]="abc"

print(str_ar)

# 1로 초기화 되는 배열 생성시 ones
o_ar=np.ones((2,3,4),dtype='i8')
print(o_ar)

ol=np.ones_like(o_ar,dtype='f')
zl=np.zeros_like(z_2dar,dtype='f8')
print(ol)
print(zl)

# empty : 기억 공간 생성, 값으로 초기화 하지 않는 명령(쓰레기값)
e_ar=np.empty((4,3,2))
print(e_ar)

print("-----------------수열--------------------")
# arange : numpy 의 range 명령
aran1 = np.arange(10)
print(aran1)

aran2 = np.arange(1,10,2)   # 끝 : 미포함
print(aran2)

lin_sp=np.linspace(0,100,5) # 끝 : 포함
print(lin_sp)

log_sp=np.logspace(0.1,1,10)
print(log_sp)









