# 2차원 그리드 포인트

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(3)
y=np.arange(5)

X,Y = np.meshgrid(x,y)
print("X=", X)
print("Y=", Y)

print([list(zip(x,y))for x,y in zip(X,Y)])
plt.title("Grid point")
plt.scatter(X,Y)
plt.show()





















