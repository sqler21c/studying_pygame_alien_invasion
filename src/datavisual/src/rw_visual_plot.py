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
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # 랜덤워크의 포인트를 그립니디ㅏ
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)

    # ax.scatter(rw.x_values, 
    #            rw.y_values, 
    #            c=point_numbers, 
    #            cmap=plt.cm.Blues, 
    #            edgecolors='none', 
    #            s=1)

    ax.plot(rw.x_values, 
            rw.y_values, 
            linewidth=1)
    
    ax.set_aspect('equal')

    # 시작점과 끝점 강조
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], 
               rw.y_values[-1], 
               c='red',
               edgecolors='none', 
               s=100)
    
    #  축 제거
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("make another wak? (y/n): ")
    if keep_running == 'n':
        break