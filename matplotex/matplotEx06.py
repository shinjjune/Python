import matplotlib.pyplot as plt
import numpy as np

"""
fig=plt.figure()
ax=fig.add_subplot(1,1,1)

ax.set(xlim=[-3.5,3.5],ylim=[-1.2,1.2])

x=np.linspace(-np.pi,np.pi)
siny=np.sin(x)
cosy=np.cos(x)

ax.plot(x,siny,color='blue',linewidth=2)
ax.plot(x,cosy,color='red',linewidth=2)

plt.show()
"""
# -------------------------------------------
# tick (축에표시되는 숫자)
# fig=plt.figure()
# ax=fig.add_subplot(1,1,1)
#
# ax.set(xlim=[-3.5,3.5],ylim=[-1.2,1.2])
# ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])  # x 축에 표시될 값
#
# #  -파이 부터 +파이까지
# x=np.linspace(-np.pi,np.pi)
# siny=np.sin(x)
# cosy=np.cos(x)
#
# ax.plot(x,siny,color='blue',linewidth=2)
# ax.plot(x,cosy,color='red',linewidth=2)
#
# plt.show()
# ------------------------------------------
fig=plt.figure()
ax=fig.add_subplot(1,1,1)

ax.set(xlim=[-3.5,3.5],ylim=[-1.2,1.2])
ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])  # x 축에 표시될 값
ax.set_xticklabels(['$-\pi$','$-\pi/2$','$0$','$\pi/2$','$\pi$'])
"""
# outward 각각의 축을 바깥 방향으로 지정한 값만큼 이동
ax.spines['bottom'].set_position(('outward',20))
ax.spines['left'].set_position(('outward',20))
ax.spines['top'].set_position(('outward',20))
ax.spines['right'].set_position(('outward',20))
"""
'''
# data 값으로 위치 지정
ax.spines['bottom'].set_position(('data',-0.5))
ax.spines['left'].set_position(('data',0))
ax.spines['top'].set_position(('data',1))
ax.spines['right'].set_position(('data',2))
ax.spines['right'].set_color('none')
'''

# axes 비율로 설정한 위치로 이동
ax.spines['bottom'].set_position(('axes',0.75))
ax.spines['left'].set_position(('axes',0.25))
# ax.spines['top'].set_position(('data',1))
ax.spines['top'].set_color('none')
# ax.spines['right'].set_position(('data',2))
ax.spines['right'].set_color('none')




#  -파이 부터 +파이까지
x=np.linspace(-np.pi,np.pi)
siny=np.sin(x)
cosy=np.cos(x)

ax.plot(x,siny,color='blue',linewidth=2)
ax.plot(x,cosy,color='red',linewidth=2)

plt.show()


