import matplotlib.pyplot as plt

# axes 설정
fig=plt.figure()
ax=fig.add_subplot(1,1,1)

# set()
# ax.set(xlim=[0.,1.],ylim=[-0.5,2.5], title="matplotEx03",xlabel='x-Axis',ylabel='y=Axis')

ax.set_xlim([0.,1.])
ax.set_ylim([-0.5,2.5])
ax.set_title('matplotEx03',size=20)
ax.set_xlabel('x-Axis',size=10)
ax.set_ylabel('y-Axis',size=10)


plt.show()






















