import matplotlib.pyplot as plt

# x_values =list(range(1,6))
# y_values = [x**3 for x in x_values]

# plt.plot(x_values,y_values)

# plt.title("LiFanHe",fontsize=24)
# plt.xlabel("X",fontsize=14)
# plt.ylabel("Y",fontsize=14)

# plt.show()

x_values =list(range(1,5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values,y_values,edgecolors="none",s=40,c=y_values,cmap=plt.cm.YlGnBu)

plt.title("LiFanHe",fontsize=24)
plt.xlabel("X",fontsize=14)
plt.ylabel("Y",fontsize=14)
#设置刻度标记大小
plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis([0,5000,1,5000**3])

plt.show()