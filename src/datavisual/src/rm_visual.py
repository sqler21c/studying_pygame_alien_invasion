import matplotlib.pyplot as plt

from random_walk import RandomWalk

# create randomwalk
#  yrw = RandomWalk()
#  yrw.fill_walk()
#  y
#  yplt.style.use('classic')
#  yfig, ax = plt.subplots()
#  yax.scatter(rw.x_values, rw.y_values, s=15)
#  yax.set_aspect('equal')
#  yplt.show()

while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    ax.set_aspect('equal')
    plt.show()

    keep_running = input("make another wak? (y/n): ")
    if keep_running == 'n':
        break