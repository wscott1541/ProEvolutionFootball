#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:53:29 2020

@author: SoapBar
"""

"""
from https://blog.zhaytam.com/2018/08/21/creating-gifs-using-python-pillow/
Further details, including use of line rather than ellipse (although I could use ellipse for the ball, I suppose?)
Need to find method of iteratively adding coordinates
More information at https://note.nkmk.me/en/python-pillow-imagedraw/
"""

from PIL import Image, ImageDraw

import numpy as ny

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
"""
#inputs = times,off_color,def_color,origin,snaps,holds,throws,wrs,decoys,linebackers,safetys

def play_frame(time,times,pitch_width, pitch_length,snaps_line,holds_line,throws_line,wrs_line,decoys_line,linebackers_line,safetys_line,off_color,def_color):
    new_pitch_width = pitch_width * 10
    new_pitch_length = (pitch_length + 20) * 10
    
    img = Image.new('RGB', (new_pitch_width, new_pitch_length), 'green')
    draw = ImageDraw.Draw(img)
    
    #Draw lines on the pitch
    draw.line(((0,100),(new_pitch_width,100)), fill='white', width = 3)
    draw.line(((0,new_pitch_length-100),(new_pitch_width,new_pitch_length-100)), fill='white', width = 3)
    
    #Draw lines that are time dependent
    if time <= times[0]:
        draw.line(snaps_line,fill='orange',width=2)
        
    draw.line(holds_line,fill=off_color,width=6)
        
    if time > times[0] + times[1] and time <= times[0] + times[1] + times[2] and times[2] > 0:
        draw.line(throws_line,fill='orange',width=2)
    #if I'm doing this, I don't need to remove the lines once plotted (and it looks weird once thrown if it disappears)
        
    
    
    #Draw lines that are not time dependent
    draw.line(holds_line,fill=off_color,width=6)    
    draw.line(wrs_line,fill=off_color,width=6)
    draw.line(decoys_line,fill=off_color,width=6)
    
    draw.line(linebackers_line,fill=def_color,width=6)
    draw.line(safetys_line,fill=def_color,width=6)
    
    
    return img

def line_add(actual,prov,time):
    t_var = int(time * 1000)
    position = (10*actual[0][t_var],10*(10 + 100 - actual[1][t_var]))
    prov.append(position)
    

def animate_play(times,pitch_width, pitch_length,snaps,holds,throws,wrs,decoys,linebackers,safetys,off_color,def_color):
    t_sta = 0.001
    t_fin = times[0] + times[1] + 0.001
    if times[2] > 0:
        t_fin = times[0] + times[1] + times[2] + 0.001
    if times[3] > 0:
        t_fin = times[0] + times[1] + times[2] + times[3] + 0.001
    if times[3] > 4:
        t_fin = times[0] + times[1] + times[2] + times[3] + 0.001 - 4

    frames = []
    
    prov_snaps = [(10*snaps[0][0],10*(10 + pitch_length - snaps[1][0]))]
    
    prov_holds = [(10*holds[0][0],10*(10 + pitch_length - holds[1][0]))]
    prov_wrs = [(10*wrs[0][0],10*(10 + pitch_length - wrs[1][0]))]
    prov_decoys = [(10*decoys[0][0],10*(10 + pitch_length - decoys[1][0]))]
    
    prov_linebackers = [(10*linebackers[0][0],10*(100 + pitch_length - linebackers[1][0]))]
    prov_safetys = [(10*safetys[0][0],10*(10 + pitch_length - safetys[1][0]))]

    if times[2] > 0:
        prov_throws = [(10 * throws[0][0],10*(10 + pitch_length - throws[1][0]))]
    else:
        prov_throws = [(0,0),(0,0)]
    
    for t in ny.arange(t_sta,t_fin-3.5,0.001):###I need to make these not such insane intervals, which can be done here or in the line_add function - a structured approach to plotting (through snap, hold, throw, rac) might be best
        if t <= times[0]:
            line_add(snaps,prov_snaps,t)
        if t > times[0]:
            prov_snaps.append((0,0))
        snaps_line = tuple(prov_snaps)
        
        if times[2] > 0 and t > (times[0] + times[1]) and t < (times[0] + times[1] + times[2]):
            line_add(throws,prov_throws,t-(times[0] + times[1]))
        throws_line = tuple(prov_throws)
        
        line_add(holds,prov_holds,t)
        holds_line = tuple(prov_holds)
        line_add(wrs,prov_wrs,t)
        wrs_line = tuple(prov_wrs)
        line_add(decoys,prov_decoys,t)
        decoys_line = tuple(prov_decoys)
        
        line_add(linebackers,prov_linebackers,t)
        linebackers_line = tuple(prov_linebackers)#there's something off with the linebacker tbq
        line_add(safetys,prov_safetys,t)#safety doesn't appear until starts moving
        safetys_line = tuple(prov_safetys)
    
        new_frame = play_frame(t,times,pitch_width, pitch_length,snaps_line,holds_line,throws_line,wrs_line,decoys_line,linebackers_line,safetys_line,off_color,def_color)
        frames.append(new_frame)
    print(len(frames))
    #inputs = blahblahblah
    frames[0].save('PlayRoute.gif', format='GIF', append_images=frames[1:], save_all=True, duration=1, loop=0)
    print('It fucking worked (and your file is at...)')    
"""        
for i in range(1,10):
    position_one = (x_a[i],500-y_a[i])
    L_one.append(position_one)
    line_one = tuple(L_one)
    position_two = (x_b[i],500-y_b[i])
    L_two.append(position_two)
    line_two = tuple(L_two)
    
    
    
    #new_frame = create_image_with_ball(i, 500, 500, [x_a[i], 500 - y_a[i]],[x_b[i], y_b[i]], 20,'red','blue')
    new_frame = create_image_with_line(500,1000,line_one,line_two)
    frames.append(new_frame)
    #x_a += 40
    #y_a += 40

# Save into a GIF file that loops forever
#inputs = [2,4,6,10]
    #filename = 'AFF{}{}{}{}.gif'.format(inputs[0],inputs[1],inputs[2],inputs[3])

frames[0].save(filename, format='GIF', append_images=frames[1:], save_all=True, duration=200, loop=0)
#duration = milliseconds
#loop = 0 is infinite looping
"""