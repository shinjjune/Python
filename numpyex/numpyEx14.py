# 행렬의 곱셈
import numpy as np

x=np.arange(10)

print(x*100)

y=np.arange(12).reshape(3,4)

print(y*100)
# ------------------브로드 캐스팅---------------------
print()
x=np.arange(5)
y1=np.ones_like(x)
y2=1

print("y1=",y1)
print("x+y1=" ,x+y1)
print("x+y2=" ,x+y2)
print("x+1=" ,x+1)
# --------------------------------------------------
x=np.vstack([range(7)[i:i+3] for i in range(5)])
print("x \n",x)

y1=np.arange(5)[:,np.newaxis]
print("x+y1 브로드캐스팅 \n",x+y1)

y2=np.arange(3)
print("x+y2 브로드캐스팅 \n",x+y2)

print("----차원축소연산----")

x=np.array([4,2,1,3])

print(x)
print(np.sum(x))

print("max :", np.max(x))
print("min :", np.min(x))

print("argmin : ",x.argmin())    # 최소값의 위치
print("argmin : ",x.argmax())    # 최대값의 위치

# ------------- boolean 연산 --------------
print("====== np.any, np.all ========")

a=np.zeros((100,100),dtype=np.int)
print(np.any(a !=0))   # False
print(np.all(a ==0))   # True


a=np.array([1,2,3,2])
b=np.array([2,2,3,2])
c=np.array([6,4,4,5])

print((a<=b)&(b<=c).all())
# -----------------------------------------
x=np.array([[1,2],[3,4]])

print(x)
print("행 합계 :",x.sum(axis=1))  # axis=1 행방향
print("열 합계 :",x.sum(axis=0))  # axis=0 열방향






