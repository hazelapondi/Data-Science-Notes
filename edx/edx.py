import matplotlib.pyplot as plt
a = [1, 2, 3, 4]
b = [3, 9, 2, 6]
plt.plot(a, b)
plt.fill_between(a,b,0,color='green') #to fill up the area under the graph
plt.show()