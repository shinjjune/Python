import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.set(xlim=[0.,8.],ylim=[0.,40.])

x=np.array([1,3,5,7])   # x 축의 값
y=np.array([10,20,15,30])   # x 축에 대응되는 y 축의 값

# ax.plot(x,y)  # plot() 는 꺾은선 그래프
# ax.plot(x,y,color='red',linewidth=0.5)  # 색상, 라인, 형식 지정 (line 2D)

# ax.plot(x,y, marker='^', color='darkgreen')
ax.scatter(x,y, marker='*', color='red')  # scatter() 이산값 그래프   



plt.show()






















