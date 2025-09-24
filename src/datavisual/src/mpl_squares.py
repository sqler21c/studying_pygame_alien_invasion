import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
ax.plot(input_value, squares, linewidth = 3)

# 그래프 타이틀
ax.set_title("Square Number", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

# 틱 이름표  눈금이름 크기
ax.tick_params(labelsize = 14)

plt.show()
