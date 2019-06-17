# 배열 연결
import numpy as np

a1=np.ones((2,3))
a2=np.zeros((2,2))

hs=np.hstack([a1,a2])
print(hs)

# ------------------------------------
b1=np.ones((2,3))
b2=np.zeros((3,3))


vs=np.vstack([b1,b2])
print(vs)

# ------------------------------------
c1=np.ones((3,4))
c2=np.zeros((3,4))

ds=np.dstack([c1,c2])
print(ds)







