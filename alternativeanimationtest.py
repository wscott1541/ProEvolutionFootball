#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:53:29 2020

@author: SoapBar
"""

"""
from https://blog.zhaytam.com/2018/08/21/creating-gifs-using-python-pillow/
"""

from PIL import Image, ImageDraw

"""
def create_image_with_ball(width, height, ball_x, ball_y, ball_size,ball_color):
    img = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # draw.ellipse takes a 4-tuple (x0, y0, x1, y1) where (x0, y0) is the top-left bound of the box

    # and (x1, y1) is the lower-right bound of the box.

    draw.ellipse((ball_x, ball_y, ball_x + ball_size, ball_y + ball_size), fill=ball_color)
    draw.ellipse((ball_x, ball_y, ball_x + ball_size, ball_y + ball_size), fill=ball_color)
    return img
"""

def create_image_with_ball(start_time,width, height, ball_one, ball_two, ball_size,ball_one_color,ball_two_color):
    img = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # draw.ellipse takes a 4-tuple (x0, y0, x1, y1) where (x0, y0) is the top-left bound of the box

    # and (x1, y1) is the lower-right bound of the box.
    if start_time >= 4:
        draw.ellipse((ball_one[0], ball_one[1], ball_one[0] + ball_size, ball_one[1] + ball_size), fill=ball_one_color)
    if start_time >= 0:
        draw.ellipse((ball_two[0], ball_two[1], ball_two[0] + ball_size, ball_two[1] + ball_size), fill=ball_two_color)
    return img

#create the frames

frames = []
x_a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
y_a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
x_b = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
y_b = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

for i in range(6):
    new_frame = create_image_with_ball(i, 1000, 500, [x_a[i], 500 - y_a[i]],[x_b[i], y_b[i]], 20,'red','blue')
    frames.append(new_frame)
    #x_a += 40
    #y_a += 40

# Save into a GIF file that loops forever

frames[0].save('moving_ball2.gif', format='GIF', append_images=frames[1:], save_all=True, duration=200, loop=0)
#duration = milliseconds
#loop = 0 is infinite looping