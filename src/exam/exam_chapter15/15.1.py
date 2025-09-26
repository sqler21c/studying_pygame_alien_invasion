import matplotlib.pyplot as plt

x_value = range(0, 50001)
y_value = [x**3 for x in x_value]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, s= 10)

# set title
ax.set_title("15.1 Exam", fontsize=14)
ax.set_xlabel("x_valule", fontsize=14)
ax.set_ylabel("3제곱", fontsize=14)

# tick
ax.axis([min(x_value), max(x_value), min(y_value), max(y_value)])

# ax.ticklabel_format(style='plain')

plt.show()