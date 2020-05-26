#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 11:48:49 2020

@author: WS
"""
"""
Using http://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/ and Paul for the appending, and myself for the removing first values.
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
#from matplotlib.animation import HTMLWriter
new_x_one = []
x_data_one = [0,1,2,3,4,5,6,7,8,9]
new_y_one = []
y_data_one = [0,1,2,3,4,5,6,7,8,9]

new_x_two = []
x_data_two = [0,1,2,3,4,5,6,7,8,9]
new_y_two = []
y_data_two = [10,9,8,7,6,5,4,3,2,1]

fig = plt.figure()
ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
line_one, = ax.plot([], [], lw=2,color='red',ms=10)
line_two, = ax.plot([], [], lw=2,color='blue',ms=10)
#line_cos, = ax.plot([], [], lw=2,color='blue')

def init():
    line_one.set_data([], [])
    line_two.set_data([], [])
    #line_cos.set_data([], [])
    return line_one, line_two,
    #return line_cos,

def animate(i):
    if i >= 3:
        x_one = x_data_one[i]
        new_x_one.append(x_one)
        y_one = y_data_one[i]
        new_y_one.append(y_one)
        x_two = x_data_two[i]
        new_x_two.append(x_two)
        y_two = y_data_two[i]
        new_y_two.append(y_two)
    #y_cos = np.cos(i * 0.02 & np.pi)
    line_one.set_data(new_x_one, new_y_one)
    line_two.set_data(new_x_two, new_y_two)
    #line_cos.set_data(x, y_cos)
    return line_one, line_two,

"""
def animate(i):
    
    x = x_data[i]
    #new_x.append(x)
    y = y_data[i]
    #new_y.append(y)
    new_x = [x]
    new_y = [y]
    #y_cos = np.cos(i * 0.02 & np.pi)
    line.set_data(new_x, new_y)
    #line_cos.set_data(x, y_cos)
    return line,
    #return line_cos,
"""
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=10, interval=80, blit=True)

# set embed_frames=True to embed base64-encoded frames directly in the HTML
# #anim.save('animation.html', writer=HTMLWriter(embed_frames=True))

plt.show()