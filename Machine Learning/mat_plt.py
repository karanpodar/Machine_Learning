from cProfile import label
from matplotlib import pyplot as plt
import numpy as np
import random as rand

# print(plt.style.available)   # shows list of all the available styles
# plt.style.use('fivethirtyeight')  #uses the given style
# plt.xkcd()    # to use a comic style - inbuilt

# dev_x = np.arange(25, 35)
# dev_x_ind = np.arange(len(dev_x))
# width = 0.25
# lin_y = np.linspace(10, 50, 10)
# dev_y = np.empty_like(lin_y, np.int8)

# print(dev_x.shape)
# print(dev_x)
# print(dev_y.shape)
# print(dev_y)
# print(lin_y.shape)
# print(lin_y)

# plt.plot(dev_x, lin_y, label='Linear data')    # to plot a linear graph
# plt.bar(dev_x, dev_y, label='Random Data')     # to plot a bar graph

# plt.plot(dev_x, lin_y, color='k', linestyle='--', label='Linear data')   #k-- is format string, k is for black and -- is for dashed lines
# plt.plot(dev_x, dev_y, color='b', marker='.', label='Random Data')  # b is also format string in which line will be blue colored and . is dots marker

# plt.plot(dev_x, lin_y, 'k--', label='Linear data')   #k-- is format string, k is for black and -- is for dashed lines
# plt.plot(dev_x, dev_y, 'b', label='Random Data')     # b is also format string in which line will be blue colored 

# plt.plot(dev_x, dev_y, color='b', linewidth=4, label='Random Data')  # b is also format string in which line will be blue colored with linewidth

# plt.bar(dev_x_ind, lin_y, width=width, label='Linear data')    # to plot a bar graph with 2 different bar and widths
# plt.bar(dev_x_ind + width, dev_y, width=width, label='Random Data')     # to plot a bar graph with 2 different bar and widths
# plt.xticks(ticks=dev_x_ind, labels=dev_x)    # since we are using dev_x_ind to plot to update the x axis labels we use xticks methods in bar graph

# plt.xlabel('Age')
# plt.ylabel('Random Integer')
# plt.title('Matplotlib Basics')
# plt.legend(['Linear data', 'Random Data'])
# plt.tight_layout()  # to fit other parameter correctly in the figure
# plt.grid(True)  # to add grids

# plt.savefig('path') # to save the graph in local machine 

pie_slice = [rand.randint(100, 150), rand.randint(151, 200)]
pie_label = ['Rand_1', 'Rand_2']
pie_color = ['Red', 'Green']
pie_explode = [0, 0.2]
print(pie_slice)
plt.pie(pie_slice, labels= pie_label, colors=pie_color, shadow=True, startangle=90, explode=pie_explode, wedgeprops={'edgecolor': 'black'})

plt.show()