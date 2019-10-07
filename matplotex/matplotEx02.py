import matplotlib.pyplot as plt

"""
axes 는 figure 내에서 축을 가지는 하나의 좌표평면
        데이터가 그려지는 곳
"""
# fig=plt.figure()
# ax=fig.add_subplot(2,2,2)  # 맨 뒤에 있는 1은 첫번째 칸을 의미
#
# plt.show()

# ------------------------------------------------

fig=plt.figure()
ax1=fig.add_subplot(1,2,1)  # 창을 가로 1칸 세로 2칸으로 쪼개서
ax2=fig.add_subplot(1,2,2)  # 첫번째에 ax1, 두번째에 ax2 를 그리기

plt.show()









