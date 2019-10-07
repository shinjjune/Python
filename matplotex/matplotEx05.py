import matplotlib.pyplot as plt

# 축의 최소값 최대값
# fig=plt.figure()
# ax=fig.add_subplot(1,1,1)
#
# ax.set_xlim(left=0,right=3)
# ax.set_ylim(bottom=-2,top=1)
#
# plt.show()

# -----------------------------------

fig=plt.figure()
ax=fig.add_subplot(1,1,1)

ax.set_xlim(left=0,right=30)
ax.set_ylim(bottom=200,top=0)

ax.set_xlabel('temperature($^{\circ}$C)')
ax.set_ylabel('depth(m)')



plt.show()


















