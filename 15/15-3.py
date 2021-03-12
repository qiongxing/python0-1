import matplotlib.pyplot as plt

from random_wall import RandomWalk

while True:
    #创建一个randomWalk实例，并绘制所有点
    rw = RandomWalk(5000)
    rw.fill_walk()
    #调整窗口尺寸
    plt.figure(figsize=(10,6),dpi=128)
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values,rw.y_values)
    #突出起点终点
    plt.scatter(0,0,c='green',edgecolors='none',s=100,linewidth=0.5)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
    #隐藏坐标轴
    plt.xticks([])  #去掉x轴
    plt.yticks([])  #去掉y轴
    plt.show()
    keep_running = input("Make another walk?(y/n): ")
    if keep_running=="n":
        break