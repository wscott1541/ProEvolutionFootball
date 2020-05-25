#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:51:24 2020

@author: WS

"""

import numpy
import random    
from math import sqrt, atan, cos, sin, pi, tan

#constants
gravity = 9.80665

time_interval = 0.01

#def function(input):
#    output_one = 2 * input
#    output_two = 3 * input
#    output = [output_one,output_two]
#    return(output)

#throw_to = 20
#wrec = [40,0]
#qb = [20,0]
#hold = 2.5
#throw_speed = 28

def last_val(a):
    last = a[(len(a) - 1)]
    return(last)  

def acc_calc(a,b):
    if a != b:
        acc_one = 2*(10*0.9144) / (a ** 2)
        acc_two = 2*(10*0.9144) / ((b-a)**2)
    else:
        acc_one = 2*(40*0.9144) / (a**2)
        acc_two = 2*(40*0.9144) / (a**2)
    acc = (acc_one + acc_two)/2
    return(acc)
    
def speed_func(runner,time_val):
    speed = last_val(runner[2]) + runner[3] * time_val
    if speed > runner[2][0]:
        new_speed = runner[2][0]
    else:
        new_speed = speed
    return(new_speed)
    
def forty_speed(a):
    speed = (40 * 0.9144)/a
    return(speed)
    
def finalise_deets(runner,time,x_array,y_array):
    final_pos = [last_val(x_array),last_val(y_array)]
    runner.append(final_pos)
    new_speed = speed_func(runner,time)
    runner[2].append(new_speed)

def quad_one(a,b,c):
    x = (-b - sqrt((b**2) - 4 * a * c))/(2 * a)
    return(x)

def quad_two(a,b,c):
    x = (-b + sqrt((b**2) - 4 * a * c))/(2 * a)
    return(x)
    
def quad_greater(a,b,c):
    one = quad_one(a,b,c)
    two = quad_two(a,b,c)
    if one > two:
        x = one
    elif two > one:
        x = two
    return(x) 

def z_populating(height,equivalent):
    length = len(equivalent)
    z_val = height * (2/3)
    z_vals = []
    for i in range(0,length):
        z_vals.append(z_val)
    return(z_vals)

def join_two(a,b):
    blank = []
    for x in range(0,(len(a))):
        val = a[x]
        blank.append(val)
    for x in range(1,(len(b))):
        val = b[x]
        blank.append(val)
    return(blank)

def join_three(a,b,c):
    blank = []
    for x in range(0,(len(a))):
        val = a[x]
        blank.append(val)
    for x in range(1,(len(b))):
        val = b[x]
        blank.append(val)
    for x in range(1,(len(c))):
        val = c[x]
        blank.append(val)
    return(blank)

def o_line(origin):
    oline_x = list(numpy.arange(20,32.5,2.5))
    oline_y = [origin[1]] * len(oline_x)
    return(oline_x,oline_y)

def snap(origin,qb):
    qb_pos = qb[(len(qb)-1)]
    qb_x = qb_pos[0]
    qb_y = qb_pos[1]
    if qb_y == 0:
        qb_y = 0.001
    if qb_y < -2:
        qb_y = -2
    qb_z = qb[1] * (0.5)#completes the coordinates of where the qb will be
    
    #modelling a snap which is, in essence, not affected by gravity
    ballspeed = 15
    abs_y = abs(qb_y)
    snap_distance = sqrt((qb_z ** 2) + (abs_y ** 2))
    time_total = round((snap_distance / ballspeed),2)
    snangle = atan(qb_z/abs_y)
    z_speed = ballspeed * sin(snangle) 
    y_speed = ballspeed * cos(snangle)

    x_vals, y_vals, z_vals = [],[],[]

    t_sta = 0
    t_fin = time_total + time_interval

    for t in numpy.arange(t_sta,t_fin,time_interval):
        x_vals.append(qb_x)
        y_val = - y_speed * t
        y_vals.append(y_val)
        z_val = z_speed * t
        z_vals.append(z_val)
    return(time_total,x_vals,y_vals,z_vals)

def throw_angle(target,wrec_position,qb_position):
    qb_x = qb_position[0]
    qb_y = qb_position[1]
    wr_x = wrec_position[0]
    xdistance = abs(wr_x - qb_x)
    ydistance = target - qb_y
    if xdistance != 0:
        hangle = atan(ydistance/xdistance)
    if xdistance == 0:
        hangle = pi/2
    return(hangle)

#angle_of_throw = throw_angle(throw_to,wrec,qb)
    
#print(angle_of_throw)

def time_to_catch(ballspeed,qb_position,h_angle,wr_line,v_angle):
    qb_x = qb_position[0]
    wr_x = wr_line[0]
    x_distance = abs(wr_x - qb_x)
    x_speed = ballspeed * cos(h_angle) * cos(v_angle)
    time_a = x_distance / x_speed
    time_b = round(time_a,2)
    return(time_b)
    
def time_to_ground(qb,ballspeed,vangle):
    a = -gravity/2
    b = ballspeed * sin(vangle)
    c = qb[1]
    time_a = quad_greater(a,b,c)
    #((ballspeed * sin(vangle)) / gravity) + sqrt((2*qb[1]/(gravity)) + (((ballspeed * sin(vangle))**2)/(gravity ** 2)))
    time_b = round(time_a,2)
    return(time_b)
    
def time_to_out(ballspeed,hangle,vangle,qb_position):
    distance = qb_position[0]
    time_a = distance / ((ballspeed * cos(hangle)) * cos(vangle))
    time_b = round(time_a,2)
    return(time_b)

def hold_x(time,qbposition):
    x_vals = []
    t_sta = 0
    t_fin = time + time_interval
    for t in numpy.arange(t_sta,t_fin,time_interval):
        x_val = qbposition[0]
        x_vals.append(x_val)
    return(x_vals)

def throw_y(ballspeed,time,qb_position,hangle,vangle):
    y_vals = []
    t_sta = 0
    t_fin = time + time_interval
    for t in numpy.arange(t_sta,t_fin,time_interval):
        y_val = qb_position[1] + ballspeed * sin(hangle) * cos(vangle) * t
        y_vals.append(y_val)
    return(y_vals)

def throw_z(ballspeed,time,qb_height,vangle):
    z_vals = []
    t_sta = 0
    t_fin = time + time_interval
    for t in numpy.arange(t_sta,t_fin,time_interval):
        z_val = qb_height + ((ballspeed * sin(vangle)) * t - 0.5 * gravity * (t ** 2))
        z_vals.append(z_val)
    return(z_vals)
    
def throw_x(ballspeed,time,qb_position,hangle,vangle,wrside):
    if wrside == 'R':
        direction = 1
    elif wrside == 'L':
        direction = -1
    x_vals = []
    t_sta = 0
    t_fin = time + time_interval
    for t in numpy.arange(t_sta,t_fin,time_interval):
        x_val = qb_position[0] + direction * ballspeed * cos(hangle) * cos(vangle) * t
        x_vals.append(x_val)
    return(x_vals)
    
def throws(time,ballspeed,qb,hangle,vangle,wrecside):
    x_vals = throw_x(ballspeed,time,last_val(qb),hangle,vangle,wrecside)
    y_vals = throw_y(ballspeed,time,last_val(qb),hangle,vangle)
    z_vals = throw_z(ballspeed,time,qb[1],vangle)
    return(x_vals,y_vals,z_vals)

def run_after_catch(x_start,y_start,wrspeed,run_gen):#run_gen can be 1 or 2
    if x_start > 25:
        max_x = x_start
    elif x_start < 25:
        max_x = 50 - x_start
    max_y = 110 - y_start
    max_distance = sqrt((max_y ** 2) + (max_x ** 2))
    prov_distance = random.random() * max_distance
    wrrun_angle = (random.randint(0,100))/100
    wrrun_side = random.randint(0,2)
    if wrrun_side == 0:
        run_direc = -1
        max_x = x_start
    elif wrrun_side == 1:
        run_direc = 1
        max_x = 50 - x_start
    if prov_distance * cos(wrrun_angle) > max_x:
        prov_distance = max_x / cos(wrrun_angle)
    if prov_distance * sin(wrrun_angle) > max_y:
        prov_distance = max_y / sin(wrrun_angle)
    run_time = round(prov_distance/wrspeed,2)
    run_x = []
    t_sta = time_interval
    t_fin = run_time + time_interval
    for t in numpy.arange(t_sta,t_fin,time_interval):
        run_x_val = x_start + run_direc * wrspeed * cos(wrrun_angle) * t
        run_x.append(run_x_val)
    run_y = []
    for t in numpy.arange(t_sta,t_fin,time_interval):
        run_y_val = y_start + wrspeed * sin(wrrun_angle) * t
        run_y.append(run_y_val)
    distance_run = round(prov_distance * sin(wrrun_angle))
    return(run_time,run_x,run_y,distance_run)  
    
def vert_y(time,speed,start_position,direction):
    y_vals = []
    t_sta = 0
    t_fin = time + time_interval
    for t in numpy.arange(t_sta,t_fin,time_interval):
        y_val = start_position[1] + direction * speed * t
        y_vals.append(y_val)
    return(y_vals)
    
def vert_x(time,start_position):
     x_vals = []
     t_sta = 0
     t_fin = time + time_interval
     for t in numpy.arange(t_sta,t_fin,time_interval):
         x_val = start_position[0]
         x_vals.append(x_val)
     return(x_vals)
     
def vert_z(time,height):
     z_vals = []
     t_sta = 0
     t_fin = time + time_interval
     for t in numpy.arange(t_sta,t_fin,time_interval):
         z_val = height * (2/3)
         z_vals.append(z_val)
     return(z_vals)

def verts(time,wreceiver,direction):
    t_sta = 0
    t_fin = time + time_interval
    x_vals = []
    y_vals = []
    z_vals = []
    
    for t in numpy.arange(t_sta,t_fin,time_interval):
        speed = speed_func(wreceiver,t)
        p_x = vert_x(t,last_val(wreceiver))
        x_vals.append(last_val(p_x))
        p_y = vert_y(t,speed,last_val(wreceiver),direction)
        y_vals.append(last_val(p_y))
        p_z = vert_z(t,wreceiver[1])
        z_vals.append(last_val(p_z))
        
    #fin_speed = speed_func(wreceiver,time)    
    #wreceiver[2].append(fin_speed)
    
    #fin_position = [last_val(x_vals),last_val(y_vals)]
        
    return(x_vals,y_vals,z_vals)

def run_ball(time,angle,qb,speed,forward,side):
    qb_position = qb[2]
    if side == 'R':
        side_val = 1
    if side == 'L':
        side_val = -1
    t_sta = 0
    t_fin = time + time_interval
    move_x = []
    move_y = []
    for t in numpy.arange(t_sta,t_fin,time_interval):
        del_x = qb_position[0] + speed * sin(angle) * t * side_val * forward#these need fixing (maybe part of splitting into two?)
        move_x.append(del_x)
        del_y = qb_position[1] + speed * cos(angle) * t * forward
        move_y.append(del_y)
    return(move_x,move_y)

def p_to_p(start,objective,speed,height):
    
    x_disp = objective[0] - start[0]
    y_disp = objective[1] - start[1]
    
    distance = sqrt((x_disp ** 2) + (y_disp ** 2))
    
    if x_disp > 0:
        x_value = 1
    if x_disp < 0:
        x_value = -1
    if y_disp > 0:
        y_value = 1
    if y_disp < 0:
        y_value = -1
    
    if x_disp == 0:
        x_speed = 0
        x_value = 0
        y_speed = speed
    elif y_disp == 0:#don't strictly need, but whatever.
        x_speed = speed
        y_speed = 0
        y_value = 0
    elif x_disp == 0 and y_disp == 0:
        x_speed = 0
        x_value = 0
        y_speed = 0
        y_value = 0
    else:
        angle = atan(abs(y_disp)/abs(x_disp))
        x_speed = speed * cos(angle)
        y_speed = speed * sin(angle)
    
    x_vals = []
    y_vals = []
    z_vals = []
    
    time = round((distance/speed),2)
    
    t_sta = 0
    t_fin = time + time_interval
    for t in numpy.arange(t_sta,t_fin,time_interval):
        move_x = start[0] + x_value * x_speed * t
        x_vals.append(move_x)
        move_y = start[1] + y_value * y_speed * t
        y_vals.append(move_y)
        z_val = height * (2/3)
        z_vals.append(z_val)
    return(x_vals,y_vals,z_vals,time)

def p_to_stop(time,runner,objective):
    
    x_disp = objective[0] - last_val(runner)[0]
    y_disp = objective[1] - last_val(runner)[1]
    
    if x_disp > 0:
        x_value = 1
    if x_disp < 0:
        x_value = -1
    if y_disp > 0:
        y_value = 1
    if y_disp < 0:
        y_value = -1
    
    if x_disp == 0:
        x_comp = 0
        x_value = 0
        y_comp = 1
    elif y_disp == 0:#don't strictly need, but whatever.
        x_comp = 1
        y_comp = 0
        y_value = 0
    elif x_disp == 0 and y_disp == 0:
        x_comp = 0
        x_value = 0
        y_comp = 0
        y_value = 0
    else:
        angle = atan(abs(y_disp)/abs(x_disp))
        x_comp = cos(angle)
        y_comp = sin(angle)
    
    x_vals = []
    y_vals = []
    z_vals = []
    
    t_sta = 0
    t_fin = time + time_interval
    for t in numpy.arange(t_sta,t_fin,time_interval):
        speed = speed_func(runner,t)
        move_x = x_value * x_comp * speed * t
        new_x = last_val(runner)[0] + move_x
        if abs(move_x) <= abs(x_disp):
            x_vals.append(new_x)
        else:
            x_vals.append(objective[0])
        move_y = y_value * y_comp * speed * t
        new_y = last_val(runner)[1] + move_y
        if abs(move_y) <= abs(y_disp):
            y_vals.append(new_y)
        else:
            y_vals.append(objective[1])
        z_val = runner[1] * (2/3)
        z_vals.append(z_val)
    return(x_vals,y_vals,z_vals)
    
def lb_rush_blocked(time,linebacker,qb,origin):
    x_disp = last_val(qb)[0] - last_val(linebacker)[0]
    y_disp = last_val(qb)[1] - last_val(linebacker)[1]
    
    if x_disp > 0:
        x_value = 1
    if x_disp < 0:
        x_value = -1
    if y_disp > 0:
        y_value = 1
    if y_disp < 0:
        y_value = -1
    
    if x_disp == 0:
        x_comp = 0
        x_value = 0
        y_comp = 1
    elif y_disp == 0:#don't strictly need, but whatever.
        x_comp = 1
        y_comp = 0
        y_value = 0
    elif x_disp == 0 and y_disp == 0:
        x_comp = 0
        x_value = 0
        y_comp = 0
        y_value = 0
    else:
        angle = atan(abs(y_disp)/abs(x_disp))
        x_comp = cos(angle)
        y_comp = sin(angle)
    
    x_vals = []
    y_vals = []
    z_vals = []
    
    t_sta = 0
    t_fin = time + time_interval
    for t in numpy.arange(t_sta,t_fin,time_interval):
        speed = speed_func(linebacker,t)
        move_x = x_value * x_comp * speed * t
        new_x = last_val(linebacker)[0] + move_x
        move_y = y_value * y_comp * speed * t
        new_y = last_val(linebacker)[1] + move_y
        if new_y > origin[2]:
            x_vals.append(new_x)    
            y_vals.append(new_y)
        else:
            x_vals.append(last_val(x_vals))
            y_vals.append(last_val(y_vals))
        z_val = linebacker[1] * (2/3)
        z_vals.append(z_val)
    return(x_vals,y_vals,z_vals)

def p_to_p_in_t(time,player,objective):
    
    x_disp = objective[0] - last_val(player)[0]
    y_disp = objective[1] - last_val(player)[1]
    
    if x_disp > 0:
        x_value = 1
    if x_disp < 0:
        x_value = -1
    if y_disp > 0:
        y_value = 1
    if y_disp < 0:
        y_value = -1
    
    if x_disp == 0:
        x_comp = 0
        x_value = 0
        y_comp = 1
    elif y_disp == 0:#don't strictly need, but whatever.
        x_comp = 1
        y_comp = 0
        y_value = 0
    elif x_disp == 0 and y_disp == 0:
        x_comp = 0
        x_value = 0
        y_comp = 0
        y_value = 0
    else:
        angle = atan(abs(y_disp)/abs(x_disp))
        x_comp = cos(angle)
        y_comp = sin(angle)
    
    x_vals = []
    y_vals = []
    z_vals = []
    
    t_sta = 0
    t_fin = time + time_interval
    for t in numpy.arange(t_sta,t_fin,time_interval):
        speed = speed_func(player,t)
        move_x = last_val(player)[0] + x_value * x_comp * speed * t
        x_vals.append(move_x)
        move_y = last_val(player)[1] + y_value * y_comp * speed * t
        y_vals.append(move_y)
        z_val = player[1] * (2/3)
        z_vals.append(z_val)
    return(x_vals,y_vals,z_vals)
    
def point_to_chase(time,chaser,chase_arrays):
    t_sta = 0
    t_fin = time
    full_time = []
    for t in numpy.arange(t_sta,t_fin,time_interval):
        full_time.append(t)
    length = len(full_time)
    chasing_x = [last_val(chaser)[0]]
    chasing_y = [last_val(chaser)[1]]
    chasing_z = [chaser[1] * (2/3)]
    for i in range(1,length):
        x_disp = chase_arrays[0][i] - chasing_x[(i - 1)]
        y_disp = chase_arrays[1][i] - chasing_y[(i - 1)]
        
        if x_disp > 0:
            x_value = 1
        if x_disp < 0:
            x_value = -1
        if y_disp > 0:
            y_value = 1
        if y_disp < 0:
            y_value = -1
        
        if x_disp == 0:
            x_comp = 0
            x_value = 0
            y_comp = 1
        elif y_disp == 0:#don't strictly need, but whatever.
            x_comp = 1
            y_comp = 0
            y_value = 0
        elif x_disp == 0 and y_disp == 0:
            x_comp = 0
            x_value = 0
            y_comp = 0
            y_value = 0
        else:
            angle = atan(y_disp/x_disp)
            x_comp = abs(cos(angle))
            y_comp = abs(sin(angle))
        speed = speed_func(chaser,i*time_interval)
        move_x = chasing_x[(i - 1)] + x_value * x_comp * speed * time_interval
        chasing_x.append(move_x)
        move_y = chasing_y[(i - 1)] + y_value * y_comp * speed * time_interval
        chasing_y.append(move_y)
        z_val = chaser[1] * (2/3)
        chasing_z.append(z_val)
    return(chasing_x,chasing_y,chasing_z)
    
def point_to_chase_from_t(start,chase_arrays,chaser_speed,start_time,chase_time,height):
    t_sta = start_time + time_interval
    t_fin = chase_time + time_interval
    start_time = []
    full_time = []
    for t in numpy.arange(0,t_sta,time_interval):
        start_time.append(t)
    for t in numpy.arange(0,t_fin,time_interval):
        full_time.append(t)
    start_length = len(start_time)
    total_length = len(full_time) - start_length
    chasing_x = [start[0]]
    chasing_y = [start[1]]
    chasing_z = [height * (2/3)]
    for i in range(1,total_length):
        x_disp = chase_arrays[0][start_length + i] - chasing_x[(i - 1)]
        y_disp = chase_arrays[1][start_length + i] - chasing_y[(i - 1)]
        
        if x_disp > 0:
            x_value = 1
        if x_disp < 0:
            x_value = -1
        if y_disp > 0:
            y_value = 1
        if y_disp < 0:
            y_value = -1
        
        if x_disp == 0:
            x_speed = 0
            x_value = 0
            y_speed = chaser_speed
        elif y_disp == 0:#don't strictly need, but whatever.
            x_speed = chaser_speed
            y_speed = 0
            y_value = 0
        elif x_disp == 0 and y_disp == 0:
            x_speed = 0
            x_value = 0
            y_speed = 0
            y_value = 0
        else:
            angle = atan(y_disp/x_disp)
            x_speed = abs(chaser_speed * cos(angle))
            y_speed = abs(chaser_speed * sin(angle))
        move_x = chasing_x[(i - 1)] + x_value * x_speed * time_interval
        chasing_x.append(move_x)
        move_y = chasing_y[(i - 1)] + y_value * y_speed * time_interval
        chasing_y.append(move_y)
        z_val = height * (2/3)
        chasing_z.append(z_val)
    return(chasing_x,chasing_y,chasing_z)

def static(time,player):
    x_val = last_val(player)[0]
    y_val = last_val(player)[1]
    z_val = player[1] * (2/3)
    
    t_sta = 0
    t_fin = time + time_interval
    
    x_vals = []
    y_vals = []
    z_vals = []
    
    for t in numpy.arange(t_sta,t_fin,time_interval):
        x_vals.append(x_val)
        y_vals.append(y_val)
        z_vals.append(z_val)
        
    return(x_vals,y_vals,z_vals)    

def def_to_man(def_speed,def_pos,off_pos):
    
    x_disp = def_pos[0] - off_pos[0]
    y_disp = def_pos[1] - off_pos[1]
        
    if x_disp > 0:
        x_val = -1
    if x_disp < 0:
        x_val = 1
    if y_disp > 0:
        y_val = -1
    if y_disp < 0:
        y_val = 1
        
    if x_disp == 0:
        x_speed = 0
        y_speed = def_speed * y_val
    elif y_disp == 0:#don't strictly need, but whatever.
        x_speed = def_speed * x_val
        y_speed = 0
    elif x_disp == 0 and y_disp == 0:
        x_speed = 0
        y_speed = 0
    else:
        ratio = abs(y_disp/x_disp)
        angle = atan(ratio)
        x_speed = def_speed * cos(angle) * x_val
        y_speed = def_speed * sin(angle) * y_val
        
    return(x_speed,y_speed)

def def_speed_cal(def_speed,def_pos,off_pos,endzone,pitch_width):
    x_disp = def_pos[0] - off_pos[0]
    y_disp = def_pos[1] - off_pos[1]
    
    if x_disp > 0:
        x_val = -1
    if x_disp < 0:
        x_val = 1
    
    if def_pos[1] < endzone:
        y_val = 1
    if def_pos[1] > endzone:
        y_val = -1
    
    if x_disp == 0:
        x_speed, y_speed = def_to_man(def_speed,def_pos,off_pos)
    else:
        ratio = y_disp/x_disp
        if abs(endzone - def_pos[1]) < abs(endzone - off_pos[1]):
            if ratio > tan(60 * pi/180):
                x_speed, y_speed = def_to_man(def_speed,def_pos,off_pos)
            elif ratio < tan(30 * pi/180):
                x_speed = def_speed * cos(30 * pi/180) * x_val
                y_speed = def_speed * sin(30 * pi/180) * y_val
            else:
                x_speed = def_speed * x_val
                y_speed = 0
        if abs(endzone - def_pos[1]) >= abs(endzone - off_pos[1]):
            if ratio > tan(60 * pi/180):
                x_speed, y_speed = def_to_man(def_speed,def_pos,off_pos)
            elif ratio < tan(30 * pi/180):
                x_speed = def_speed * cos(45 * pi/180) * x_val
                y_speed = def_speed * sin(45 * pi/180) * y_val
            else:
                x_speed = def_speed * cos(60 * pi/180) * x_val
                y_speed = def_speed * sin(60 * pi/180) * y_val
    
    if abs(endzone - def_pos[1]) < 0.5:
        x_speed, y_speed = def_to_man(def_speed,def_pos,off_pos)
    
    if  pitch_width - def_pos[0] < 0.5 or def_pos[0] < 0.5:
        x_speed = 0
        y_speed = def_speed * y_val * (-1)
    
    separation = sqrt((x_disp**2) + (y_disp**2))
    if separation < 2 or separation > 20:
        x_speed, y_speed = def_to_man(def_speed,def_pos,off_pos)
    
    return(x_speed, y_speed)    
        

def off_speed_cal(off_speed,off_pos,def_pos,endzone,pitch_width):
    x_disp = off_pos[0] - def_pos[0]
    y_disp = off_pos[1] - def_pos[1]
    
    if x_disp > 0:
        x_val = 1
    if x_disp < 0:
        x_val = -1
    if x_disp == 0:
        if off_pos[0] < pitch_width/2:
            x_val = -1
        if off_pos[0] > pitch_width/2:
            x_val = 1
    
    if off_pos[1] < endzone:
        y_val = 1
    if off_pos[1] > endzone:
        y_val = -1
    
    if pitch_width - off_pos[0] < 0.5 or off_pos[0] < 0.5:
        if abs(x_disp) < 1.25 and y_disp:
            x_speed = 0
            y_speed = off_speed * y_val
        else:
            if off_pos[0] < 0.5:
                x_val = 1
            else:
                x_val = -1
            
    if abs(endzone - off_pos[1]) > abs(endzone - def_pos[1]):#defender closer to endzone 
        if pitch_width - off_pos[0] < 0.5 or off_pos[0] < 0.5 and abs(y_disp) < 3:
            if off_pos[0] < 0.5:
                x_val = 1
            else:
                x_val = -1
            
        if x_disp == 0:
            x_speed = off_speed * cos(30 * pi/180) * x_val
            y_speed = off_speed * sin(30 * pi/180) * y_val
        else:
            ratio = y_disp/x_disp
            if ratio > tan(60 * pi/180):
                x_speed = off_speed * cos(30 * pi/180) * x_val
                y_speed = off_speed * sin(30 * pi/180) * y_val
            elif ratio < tan(30 * pi/180):
                x_speed = off_speed * cos(60 * pi/180) * x_val
                y_speed = off_speed * sin(60 * pi/180) * y_val
            else:
                x_speed = off_speed * cos(45 * pi/180) * x_val
                y_speed = off_speed * sin(45 * pi/180) * y_val
    
    if abs(endzone - off_pos[1]) <= abs(endzone - def_pos[1]):#offense closer to endzone
        if pitch_width - off_pos[0] < 0.5 or off_pos[0] < 0.5:
            x_speed = 0
            y_speed = off_speed * y_val
        elif x_disp == 0:
            x_speed = 0
            y_speed = off_speed * y_val
        else:
            ratio = y_disp/x_disp
            if ratio > tan(60 * pi/180):
                x_speed = 0
                y_speed = off_speed * sin(30 * pi/180) * y_val
            elif ratio < tan(30 * pi/180):
                x_speed = off_speed * cos(45 * pi/180) * x_val
                y_speed = off_speed * sin(45 * pi/180) * y_val
            else:
                x_speed = off_speed * cos(60 * pi/180) * x_val
                y_speed = off_speed * sin(60 * pi/180) * y_val
    
    separation = sqrt((x_disp**2) + (y_disp**2))
    if separation > 20 or abs(off_pos[1] - endzone) < 3:
        x_speed = 0
        y_speed = off_speed * y_val
    
    return(x_speed,y_speed)

def def_chase(defender,runner,endzone,pitch_width,pitch_length):
    
    def_xs = [last_val(defender)[0]]
    def_ys = [last_val(defender)[1]]
    def_zs = [defender[1]*(2/3)]
    
    off_xs = [last_val(runner)[0]]
    off_ys = [last_val(runner)[1]]
    off_zs = [runner[1]*(2/3)]
    
    del_x = last_val(def_xs) - last_val(off_xs)
    del_y = last_val(def_ys) - last_val(off_ys)
    init_sep = sqrt((del_x**2) + (del_y**2))
    
    separations = [init_sep]
    
    t = 0
    while 0 < last_val(off_xs) and last_val(off_xs) < pitch_width and -1 < last_val(off_ys) and last_val(off_ys) < (pitch_length + 1) and last_val(separations) > defender[4]:
        
        def_x = last_val(def_xs)
        def_y = last_val(def_ys)
        def_pos = [def_x,def_y]
        
        off_x = last_val(off_xs)
        off_y = last_val(off_ys)
        off_pos = [off_x,off_y]
        
        p_def_speed = speed_func(defender,t)
        p_off_speed = speed_func(runner,t)
        
        def_x_speed,def_y_speed = def_speed_cal(p_def_speed,def_pos,off_pos,endzone,pitch_width)
        off_x_speed,off_y_speed = off_speed_cal(p_off_speed,off_pos,def_pos,endzone,pitch_width)
        
        def_x_val = last_val(def_xs) + def_x_speed * time_interval
        def_y_val = last_val(def_ys) + def_y_speed * time_interval
        off_x_val = last_val(off_xs) + off_x_speed * time_interval
        off_y_val = last_val(off_ys) + off_y_speed * time_interval
        
        def_xs.append(def_x_val)
        def_ys.append(def_y_val)
        def_zs.append(defender[1]*(2/3))
        off_xs.append(off_x_val)
        off_ys.append(off_y_val)
        off_zs.append(runner[1]*(2/3))
        
        x_sep = def_x - off_x
        y_sep = def_y - off_y
        sep =  sqrt((x_sep**2) + (y_sep**2))
        separations.append(sep)

        t += time_interval
        
    time = round(t,2)
    
    def_vals = [def_xs,def_ys,def_zs]
    off_vals = [off_xs,off_ys,off_zs]
    
    return(time,def_vals,off_vals)

def int_coords(start,ball_array):

    init_x_disp = ball_array[0][0] - start[0]
    init_y_disp = ball_array[1][0] - start[1]
    
    distances = [sqrt((init_x_disp**2)+(init_y_disp**2))]

    xs = [ball_array[0][1]]
    ys = [ball_array[1][1]]
    
    for i in range(1,len(ball_array[0])):
        x_disp = ball_array[0][i] - start[0]
        y_disp = ball_array[1][i] - start[1]
        
        distance = sqrt((x_disp**2)+(y_disp**2))
        if distance < last_val(distances):
            distances.append(distance)
            xs.append(ball_array[0][i])
            ys.append(ball_array[1][i])
    
    x = last_val(xs)
    y = last_val(ys)
    
    return(x,y)

def int_coord_t(start,ball_array):
    init_x_disp = ball_array[0][0] - start[0]
    init_y_disp = ball_array[1][0] - start[1]
    
    distances = [sqrt((init_x_disp**2)+(init_y_disp**2))]

    xs = [ball_array[0][1]]
    ys = [ball_array[1][1]]
    
    for i in range(1,len(ball_array[0])):
        x_disp = ball_array[0][i] - start[0]
        y_disp = ball_array[1][i] - start[1]
        
        distance = sqrt((x_disp**2)+(y_disp**2))
        if distance < last_val(distances):
            distances.append(distance)
            xs.append(ball_array[0][i])
            ys.append(ball_array[1][i])
    
    x = last_val(xs)
    y = last_val(ys)
    
    time = len(xs) * time_interval - time_interval
    
    #fin_distance = last_val(distances)
    
    return(x,y,time,distances)
    
def off_catch(wreceiver,ball_arrays):
    
    catchable = 0
    catchable_is = []
    runable = 0
    runable_is = []
    for i in range(1,len(ball_arrays[0])):
        x_disp = ball_arrays[0][i] - last_val(wreceiver)[0]
        y_disp = ball_arrays[1][i] - last_val(wreceiver)[1]
        distance = sqrt((x_disp**2) + (y_disp**2))
        speed = speed_func(wreceiver,i*time_interval)
        if distance < speed * i * time_interval + wreceiver[4] and ball_arrays[2][i] < wreceiver[1] + wreceiver[5] and ball_arrays[2][i] < ball_arrays[2][i-1]:
            catchable = 1
            catchable_is.append(i)
            if ball_arrays[2][i] < wreceiver[1]+wreceiver[4] and ball_arrays[2][i] > 0.3 * wreceiver[1]:
                runable = 1
                runable_is.append(i)
    
    if catchable == 1:
        min_catchable = catchable_is[0]
        max_catchable = last_val(catchable_is)
        catch_deets = [min_catchable,max_catchable]
    else:
        catch_deets = []        
    if runable == 1:
        min_runable = runable_is[0]
        max_runable = last_val(runable_is)
        run_deets = [min_runable,max_runable]
    else:
        run_deets = []      
    
    return(catchable,catch_deets,runable,run_deets)

def def_catch(defender,ball_arrays):
    
    blockable = 0
    blockable_is = []
    returnable = 0
    returnable_is = []
    for i in range(1,len(ball_arrays[0])):
        x_disp = ball_arrays[0][i] - last_val(defender)[0]
        y_disp = ball_arrays[1][i] - last_val(defender)[1]
        distance = sqrt((x_disp**2) + (y_disp**2))
        speed = speed_func(defender,i*time_interval)
        if distance < speed * i * time_interval + defender[4] and ball_arrays[2][i] < defender[1] + defender[5]:
            blockable = 1
            blockable_is.append(i)
            if ball_arrays[2][i] < defender[1]+defender[4] and ball_arrays[2][i] > 0.3 * defender[1]:
                returnable = 1
                returnable_is.append(i)
    
    if blockable == 1:
        min_blockable = blockable_is[0]
    else:
        min_blockable = []
    if returnable == 1:
        min_returnable = returnable_is[0]
    else:
        min_returnable = []
    
    return(blockable,min_blockable,returnable,min_returnable)
    
def throw_react(ball_arrays,wreceiver,linebacker,safety):
    
    catch_val,catch_deets,run_val,run_deets = off_catch(wreceiver,ball_arrays)
    
    lb_block,lb_min_block,lb_return,lb_min_return = def_catch(linebacker,ball_arrays)
    
    s_block,s_min_block,s_return,s_min_return = def_catch(safety,ball_arrays)
    
    if lb_block == 0 and s_block == 0:
        block_val = 0
        
    if lb_block == 1 and s_block == 1:
        block_val = 1
        if lb_min_block < s_min_block:
            block_min = lb_min_block
            return_val = lb_return
            return_min = lb_min_return
            interceptor = linebacker[0]
        if s_min_block < lb_min_block:
            block_min = s_min_block
            return_val = s_return
            return_min = s_min_return
            interceptor = safety[0]
    
    if lb_block == 0 and s_block == 1:
        block_val = 1
        block_min = s_min_block
        return_val = s_return
        return_min = s_min_return
        interceptor = safety[0]
        
    if lb_block == 1 and s_block == 0:
        block_val = 1
        block_min = lb_min_block
        return_val = lb_return
        return_min = lb_min_return
        interceptor = linebacker[0]
    
    if block_val == 1 and catch_val == 0:
        if return_val == 1:
            t = return_min * time_interval
            coords = [ball_arrays[0][return_min],ball_arrays[1][return_min]]
            cont_val = 1
            possessor = interceptor
        else:
            t = block_min * time_interval
            coords = [ball_arrays[0][block_min],ball_arrays[1][block_min]]
            cont_val = 0
    
    if block_val == 0 and catch_val == 1:
        if run_val == 1:
            t = run_deets[1] * time_interval
            coords = [ball_arrays[0][run_deets[1]],ball_arrays[1][run_deets[1]]]
            cont_val = 1
            possessor = wreceiver[0]
        else:
            t = catch_deets[1] * time_interval
            coords = [ball_arrays[0][catch_deets[1]],ball_arrays[1][catch_deets[1]]]
            cont_val = 0
    
    if block_val == 1 and catch_val == 1:
        if block_min < catch_deets[0]:
            if return_val == 1 and return_min < catch_deets[0]:
                t = return_min * time_interval
                coords = [ball_arrays[0][return_min],ball_arrays[1][return_min]]
                cont_val = 1
                possessor = interceptor
            else:
                t = block_min * time_interval
                coords = [ball_arrays[0][block_min],ball_arrays[1][block_min]]
                cont_val = 0
        else:
            if run_val == 1 and run_deets[1] < block_min:
                t = run_deets[1] * time_interval
                coords = [ball_arrays[0][run_deets[1]],ball_arrays[1][run_deets[1]]]
                cont_val = 1
                possessor = wreceiver[0]
            elif run_val == 1 and run_deets[0] < block_min:
                t = run_deets[0] * time_interval
                coords = [ball_arrays[0][run_deets[0]],ball_arrays[1][run_deets[0]]]
                cont_val = 1
                possessor = wreceiver[0]
            else:
                t = (block_min - 1) * time_interval
                coords = [ball_arrays[0][(block_min - 1)],ball_arrays[1][(block_min - 1)]]
                cont_val = 0
    
    if catch_val == 0 and block_val == 0:
        t = len(ball_arrays[0]) * time_interval
        coords = [last_val(ball_arrays[0]),last_val(ball_arrays[1])]
        cont_val = 0
    
    if cont_val == 0:
        possessor = 'None'
        
    time = round(t,2)
    
    return(time,coords,cont_val,possessor)
    
def distance_calc(one,two):
    x_disp = two[0] - one[0]
    y_disp = two[1] - one[1]   
    
    distance = sqrt((x_disp**2) + (y_disp**2))
    
    return(distance)
    
def player_details(name,height,forty,firstsplit,secondsplit,arm_length,vert_jump):
    height = 1.94
    speed = forty_speed(forty)
    acc = acc_calc(firstsplit,secondsplit,)
    player = [name, height, [speed,0], acc, arm_length, vert_jump]
    return(player)
        
        
        
        
        
        
    