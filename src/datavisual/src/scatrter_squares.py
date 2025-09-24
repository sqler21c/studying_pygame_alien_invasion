import matplotlib.pyplot as plt


# x_value = [1, 2, 3, 4, 5]
x_value = range(1, 1001)
y_value = [n**2 for n in x_value]


plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
# ax.scatter(2, 4, s = 200)
# ax.scatter(x_value, y_value, color = 'red', s = 10)
# ax.scatter(x_value, y_value, color = (0, 0.8, 0), s = 10)
ax.scatter(x_value, y_value, c = y_value, cmap = plt.cm.Blues, s = 10)

# 그래프 타이틀, 축에 이름
ax.set_title("Squares Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

# 틱
ax.tick_params(labelsize = 14)

# 각축의 범위
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style = 'plain')
# ax.axis([x_value.min(), x_value.max, y_value.min, y_value.max])

plt.savefig("square_plot.png", bbox_inches = 'tight')

plt.show()