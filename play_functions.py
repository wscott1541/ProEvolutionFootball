#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 13:34:22 2020

@author: WS
"""

gravity = 9.80665

time_interval = 0.01
rounding = 2

from math import sqrt, sin, cos, atan
import numpy

"""MISC"""

def join_two(a,b):
    blank = []
    for x in range(0,(len(a))):
        val = a[x]
        blank.append(val)
    for x in range(1,(len(b))):
        val = b[x]
        blank.append(val)
    return(blank)
    
def speed_func(runner,time_val):
    speed = runner['current speed'][-1] + runner['acc'] * time_val
    if speed > runner['speed']:
        new_speed = runner['speed']
    else:
        new_speed = speed
    return(new_speed)
    
def add_position(player,position):
    player['position'].append(position)
    
def finalise_pos_speed(time,player,x_array,y_array):
    final_pos = [x_array[-1],y_array[-1]]
    player['positions'].append(final_pos)
    new_speed = speed_func(player,time)
    player['current speed'].append(new_speed)
    
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

"""SNAP"""

def snap(origin,qb):
    qb_x = qb['position'][-1][0]
    qb_y = qb['position'][-1][1]
    if qb_y == origin[0]:
        qb_y = 0.001
    qb_z = qb['height'] * (0.5)#completes the coordinates of where the qb will be
    
    #modelling a snap which is, in essence, not affected by gravity
    ballspeed = 15
    abs_y = abs(qb_y)
    snap_distance = sqrt((qb_z ** 2) + (abs_y ** 2))
    time_total = round((snap_distance / ballspeed),3)
    snangle = atan(qb_z/abs_y)
    z_speed = ballspeed * sin(snangle) 
    y_speed = ballspeed * cos(snangle)

    x_vals, y_vals, z_vals = [],[],[]

    t_sta = 0
    t_fin = time_total + time_interval

    for t in numpy.arange(t_sta,t_fin,time_interval):
        x_vals.append(qb_x)
        y_val = origin[1] - y_speed * t
        y_vals.append(y_val)
        z_val = origin[2] - z_speed * t
        z_vals.append(z_val)
        
    return(x_vals,y_vals,z_vals)
    
def snap_time(origin,qb):
    qb_y = qb['position'][-1][1]
    ballspeed = 15
    abs_y = abs(qb_y)
    qb_z = qb['height'] * (0.5)
    snap_distance = sqrt((qb_z ** 2) + (abs_y ** 2))
    time_total = round((snap_distance / ballspeed),3)
    
    return(time_total)
    
"""THROW FUNCTIONS"""

def time_to_ground(qb,ballspeed,vangle):
    a = -gravity/2
    b = ballspeed * sin(vangle)
    c = qb['height']
    time_a = quad_greater(a,b,c)
    #((ballspeed * sin(vangle)) / gravity) + sqrt((2*qb[1]/(gravity)) + (((ballspeed * sin(vangle))**2)/(gravity ** 2)))
    time_b = round(time_a,rounding)
    return(time_b)
    
def time_to_out(ballspeed,hangle,vangle,qb_positions):
    distance = qb_positions[-1][0]
    time_a = distance / ((ballspeed * cos(hangle)) * cos(vangle))
    time_b = round(time_a,3)
    return(time_b)

def throw_x(ballspeed,time,qb_positions,hangle,vangle,wrside):
    if wrside == 'R':
        direction = 1
    elif wrside == 'L':
        direction = -1
    x_vals = []
    t_sta = 0
    t_fin = time + time_interval
    for t in numpy.arange(t_sta,t_fin,time_interval):
        x_val = qb_positions[-1][0] + direction * ballspeed * cos(hangle) * cos(vangle) * t
        x_vals.append(x_val)
    return(x_vals)
    
def throw_y(ballspeed,time,qb_positions,hangle,vangle):
    y_vals = []
    t_sta = 0
    t_fin = time + time_interval
    for t in numpy.arange(t_sta,t_fin,time_interval):
        y_val = qb_positions[-1][1] + ballspeed * sin(hangle) * cos(vangle) * t
        y_vals.append(y_val)
    return(y_vals)

def throw_z(ballspeed,time,qb,vangle):
    z_vals = []
    t_sta = 0
    t_fin = time + time_interval
    for t in numpy.arange(t_sta,t_fin,time_interval):
        z_val = qb['height'] + ((ballspeed * sin(vangle)) * t - 0.5 * gravity * (t ** 2))
        z_vals.append(z_val)
    return(z_vals)
        
def throws(time,ballspeed,qb,hangle,vangle,throw_side):
    x_vals = throw_x(ballspeed,time,qb['position'],hangle,vangle,throw_side)
    y_vals = throw_y(ballspeed,time,qb['position'],hangle,vangle)
    z_vals = throw_z(ballspeed,time,qb['height'],vangle)
    return(x_vals,y_vals,z_vals)

"""CATCH TESTS"""

def off_catch(player,ball_arrays):
    
    player_positions = player['position']
    player_speeds = player['current speed']
    
    catchable = 0
    catchable_is = []
    runable = 0
    runable_is = []
    for i in range(1,len(ball_arrays[0])):
        x_disp = ball_arrays[0][i] - player_positions[-1][0]
        y_disp = ball_arrays[1][i] - player_positions[-1][1]
        distance = sqrt((x_disp**2) + (y_disp**2))
        speed = speed_func(player,player_speeds,i*time_interval)
        if distance < speed * i * time_interval + player['arm'] and ball_arrays[2][i] < player['height'] + player['vert'] and ball_arrays[2][i] < ball_arrays[2][i-1]:
            catchable = 1
            catchable_is.append(i)
            if ball_arrays[2][i] < player['height']+player['arm'] and ball_arrays[2][i] > 0.3 * player['height']:
                runable = 1
                runable_is.append(i)
    
    if catchable == 1:
        min_catchable = catchable_is[0]
        max_catchable = catchable_is[-1]
        catch_deets = [min_catchable,max_catchable]
    else:
        catch_deets = []        
    if runable == 1:
        min_runable = runable_is[0]
        max_runable = runable_is[-1]
        run_deets = [min_runable,max_runable]
    else:
        run_deets = []      
    
    return(catchable,catch_deets,runable,run_deets)

def def_catch(player,ball_arrays):
    
    player_position = player['position']
    player_speeds = player['current speed']
    
    blockable = 0
    blockable_is = []
    returnable = 0
    returnable_is = []
    for i in range(1,len(ball_arrays[0])):
        x_disp = ball_arrays[0][i] - player_position[-1][0]
        y_disp = ball_arrays[1][i] - player_position[-1][1]
        distance = sqrt((x_disp**2) + (y_disp**2))
        speed = speed_func(player,player_speeds,i*time_interval)
        if distance < speed * i * time_interval + player['arm'] and ball_arrays[2][i] < player['height'] + player['vert']:
            blockable = 1
            blockable_is.append(i)
            if ball_arrays[2][i] < player['height']+player['arm'] and ball_arrays[2][i] > 0.3 * player['height']:
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

def store_details(catch_val,catch_potential_list,details,details_list):
    if catch_val == 1:
        catch_potential_list.append(catch_val)
        details_list.append(details)

def assessment_loop(details,kind):
    if kind == 'catch' or kind == 'block':
        v = 1
    if kind == 'run' or kind == 'return':
        v = 3
    
    times = [details[0][v]]
    catcher = [details[0][4]]
    for i in range(1,len(details)):
        if details[i][v] < times[-1]:
            times.append(details[i][v])
            catcher.append(details[i][0])
    
    time = times[-1]
    player = catcher[-1]
    
    return(time,player)
        
#def assess_catch(catch_potential,catch_details,block_potential,block_details):

"""THROW"""    
   
def throw_react(ball_arrays,throw_side,
                wr,
                dec,
                cb_one,
                cb_two,
                linebacker,
                safety):
    
    catch_potential = []
    catch_details = []
    
    if throw_side == 'L' and wr['position'][-1][0] < 30:
        wr_catch_v,wr_catch_deets,wr_run_val,wr_run_deets = off_catch(wr,ball_arrays)
        details = [wr_catch_v,wr_catch_deets,wr_run_val,wr_run_deets,wr]
        store_details(wr_catch_v,catch_potential,details,catch_details)
    if throw_side == 'R' and wr['position'][-1][0] > 20:
        wr_catch_v,wr_catch_deets,wr_run_val,wr_run_deets = off_catch(wr,ball_arrays)
        details = [wr_catch_v,wr_catch_deets,wr_run_val,wr_run_deets,wr]
        store_details(wr_catch_v,catch_potential,details,catch_details)
        
    if throw_side == 'L' and dec['position'][-1][0] < 30:
        dec_catch_v,dec_catch_deets,dec_run_val,dec_run_deets = off_catch(dec,ball_arrays)
        details = [dec_catch_v,dec_catch_deets,dec_run_val,dec_run_deets,dec]
        store_details(dec_catch_v,catch_potential,details,catch_details)
    if throw_side == 'R' and dec['position'][-1][0] > 20:
        dec_catch_v,dec_catch_deets,dec_run_val,dec_run_deets = off_catch(dec,ball_arrays)
        details = [dec_catch_v,dec_catch_deets,dec_run_val,dec_run_deets,dec]
        store_details(dec_catch_v,catch_potential,details,catch_details)
    
    block_potential = []
    block_details = []
    
    if throw_side == 'L' and cb_one['position'][-1][0] < 30:
        cb_one_block,cb_one_min_block,cb_one_return,cb_one_min_return = def_catch(cb_one,ball_arrays)
        details = [cb_one_block,cb_one_min_block,cb_one_return,cb_one_min_return,cb_one]
        store_details(cb_one_block,block_potential,details,block_details)
    if throw_side == 'R' and cb_one['position'][-1][0] > 20:
        cb_one_block,cb_one_min_block,cb_one_return,cb_one_min_return = def_catch(cb_one,ball_arrays)
        details = [cb_one_block,cb_one_min_block,cb_one_return,cb_one_min_return,cb_one]
        store_details(cb_one_block,block_potential,details,block_details)
    
    if throw_side == 'L' and cb_two['position'][0] < 30:
        cb_two_block,cb_two_min_block,cb_two_return,cb_two_min_return = def_catch(cb_two,ball_arrays)
        details = [cb_two_block,cb_two_min_block,cb_two_return,cb_two_min_return,cb_two]
        store_details(cb_two_block,block_potential,details,block_details)
    if throw_side == 'R' and cb_two['position'][-1][0] > 20:
        cb_two_block,cb_two_min_block,cb_two_return,cb_two_min_return = def_catch(cb_two,ball_arrays)
        details = [cb_two_block,cb_two_min_block,cb_two_return,cb_two_min_return,cb_two]
        store_details(cb_two_block,block_potential,details,block_details)

    lb_block,lb_min_block,lb_return,lb_min_return = def_catch(linebacker,ball_arrays)
    details = [lb_block,lb_min_block,lb_return,lb_min_return,linebacker]
    store_details(lb_block,block_potential,details,block_details)

    s_block,s_min_block,s_return,s_min_return = def_catch(safety,ball_arrays)
    details = [s_block,s_min_block,s_return,s_min_return,safety]
    store_details(lb_block,block_potential,details,block_details)
    
    if sum(catch_potential) != 0 or sum(block_potential) != 0:
        
        if sum(catch_potential) != 0 and sum(block_potential) != 0:
            catch_time,catcher = assessment_loop(catch_details,'catch')
            block_time,blocker = assessment_loop(catch_details,'block')
            
            if catch_time < block_time:
                possession = 1
                possessor = catcher
                t = catch_time
            if block_time < catch_time:
                possession = 0
                possessor = blocker
                t = block_time
        
        elif sum(catch_potential) != 0 and sum(block_potential) == 0:
            possession = 1
            t,possessor = assessment_loop(catch_details,'catch')
            
        elif sum(catch_potential) == 0 and sum(block_potential) != 0:
            possession = 0
            t,possessor = assessment_loop(catch_details,'block')
    
    try:
        coords = [ball_arrays[0][t],ball_arrays[1][t]]
        time = t * time_interval
    except:
        possession = 0
        possessor = 'NONE'
        coords = [ball_arrays[0][-1],ball_arrays[1][-1]]
        time = len(ball_arrays[0]) * time_interval
    
    new_time = round(time,rounding)
    
    return(new_time,coords,possessor,possession)
    
def throw_outcomes(possessor,coordinates,time,
                   wr_one,wr_one_x,wr_one_y,wr_one_z,
                   wr_two,wr_two_x,wr_two_y,wr_two_z,
                   cb_one,cb_one_x,cb_one_y,cb_one_z,
                   cb_two,cb_two_x,cb_two_y,cb_two_z,
                   s,
                   lb):
    if possessor['name'] == [wr_one]['name']:
        wr_one_t_x, wr_one_t_y, wr_one_t_z = p_to_p_in_t(time,wr_one,coordinates)
        wr_one_x = join_two(wr_one_x,wr_one_t_x)
        wr_one_y = join_two(wr_one_y,wr_one_t_y)
        wr_one_z = join_two(wr_one_z,wr_one_t_z)
        finalise_pos_speed(time,wr_one,wr_one_x,wr_one_y)
                    
        cb_one_t_x, cb_one_t_y, cb_one_t_z = point_to_chase(time,cb_one,[wr_one_t_x,wr_one_t_y])
        cb_one_x = join_two(cb_one_x,wr_one_t_x)
        cb_one_y = join_two(cb_one_y,wr_one_t_y)
        cb_one_z = join_two(cb_one_z,wr_one_t_z)
        finalise_pos_speed(time,wr_one,wr_one_x,wr_one_y)
                
    if possessor['name'] == [wr_two]['name']:
        wr_two_t_x, wr_two_t_y, wr_two_t_z = p_to_p_in_t(time,wr_two,coordinates)
        wr_two_x = join_two(wr_two_x,wr_two_t_x)
        wr_two_y = join_two(wr_two_y,wr_two_t_y)
        wr_two_z = join_two(wr_two_z,wr_two_t_z)
        finalise_pos_speed(time,wr_one,wr_two_x,wr_two_y)
                    
        cb_two_t_x, cb_two_t_y, cb_two_t_z = point_to_chase(time,cb_one,[wr_two_t_x,wr_two_t_y])
        cb_two_x = join_two(cb_two_x,cb_two_t_x)
        cb_two_y = join_two(cb_two_y,cb_two_t_y)
        cb_two_z = join_two(cb_two_z,cb_two_t_z)
        finalise_pos_speed(time,cb_two,cb_two_x,cb_two_y)
        
    if possessor['name'] == [cb_one]['name']:
        cb_one_t_x, cb_one_t_y, cb_one_t_z = p_to_p_in_t(time,wr_one,coordinates)
        cb_one_x = join_two(cb_one_x,wr_one_t_x)
        cb_one_y = join_two(cb_one_y,wr_one_t_y)
        cb_one_z = join_two(cb_one_z,wr_one_t_z)
        finalise_pos_speed(time,wr_one,wr_one_x,wr_one_y)
    
    if possessor['name'] == [cb_two]['name']:
        cb_two_t_x, cb_two_t_y, cb_two_t_z = p_to_p_in_t(time,cb_two,coordinates)
        cb_two_x = join_two(cb_two_x,cb_two_t_x)
        cb_two_y = join_two(cb_two_y,cb_two_t_y)
        cb_two_z = join_two(cb_two_z,cb_two_t_z)
        finalise_pos_speed(time,cb_two,cb_two_x,cb_two_y)
     
    s_x, s_y, s_z = p_to_p_in_t(time,s,coordinates)  
    temp_s = [s_x,s_z,s_z]

    if lb['status'] == 'Hold':         
        lb_x, lb_y, lb_z = p_to_p_in_t(time,s,coordinates)
        temp_lb = [lb_x,lb_z,lb_z]
        
    return(temp_s,temp_lb)

"""INDEPENDENT PLAYS"""
    
def static(time,player):
    player_position = player['position']
    x_val = player_position[-1][0]
    y_val = player_position[-1][1]
    z_val = player['height'][1] * (2/3)
    
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
    

def verts(time,player,direction):
    start_pos = player['position'][-1]
    
    #t_sta = 0
    t_fin = time + time_interval
    x_vals = [start_pos[0]]
    y_vals = [start_pos[1]]
    z_vals = [player['height']]
    
    for t in numpy.arange(time_interval,t_fin,time_interval):
        speed = speed_func(player,t)
        
        p_x = start_pos[0]
        x_vals.append(p_x)
        
        p_y = y_vals[-1] + speed * direction * t#vert_y(t,speed,last_val(wreceiver),direction)
        y_vals.append(p_y)
        
        p_z = player['height']
        z_vals.append(p_z)
        
    return(x_vals,y_vals,z_vals)

"""DEPENDENT PLAYS"""

def p_to_p_in_t(time,player,objective):
    
    position = player['position'][-1]
    
    x_disp = objective[0] - position[0]
    y_disp = objective[1] - position[1]
    
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
    
    x_vals = [position[0]]
    y_vals = [position[1]]
    z_vals = [player['height']]
    
    t_sta = time_interval
    t_fin = time + time_interval
    for t in numpy.arange(t_sta,t_fin,time_interval):
        speed = speed_func(player,t)
        move_x = x_vals[-1] + x_value * x_comp * speed * t
        x_vals.append(move_x)
        move_y = y_vals[-1] + y_value * y_comp * speed * t
        y_vals.append(move_y)
        z_val = player['height'] * (2/3)
        z_vals.append(z_val)
    return(x_vals,y_vals,z_vals) 
    
def point_to_chase(time,chaser,chase_arrays):
    t_sta = 0
    t_fin = time
    full_time = []
    for t in numpy.arange(t_sta,t_fin,time_interval):
        full_time.append(t)
    length = len(full_time)
    chasing_x = [chaser['position'][-1][0]]
    chasing_y = [chaser['position'][-1][1]]
    chasing_z = [chaser['height'] * (2/3)]
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

"""PLOT"""

import matplotlib.pyplot as plt

def plot_lines(off_color,def_color,origin,snaps,holds,throws,wrs,decoys,cb_ones,cb_twos,linebackers,safetys):
    #turn the field green, before plotting
    plt.rcParams['axes.facecolor'] = 'green'
    
    #plot throw and wr run
    plt.plot(snaps[0],snaps[1],color='orange')
    plt.scatter(wrs[0][0],wrs[1][0],color=off_color)
    plt.plot(wrs[0],wrs[1],color=off_color)

    plt.scatter(decoys[0][0],decoys[1][0],color=off_color)
    plt.plot(decoys[0],decoys[1],color=off_color)

    plt.scatter(holds[0][0],holds[1][0],color=off_color)
    plt.plot(holds[0],holds[1],color=off_color)
    if len(throws[0]) > 1:
        plt.plot(throws[0],throws[1],':',color='orange')

    #plot defense
    plt.scatter(cb_ones[0][0],cb_ones[1][0],color=def_color)
    plt.plot(cb_ones[0],cb_ones[1],color=def_color)
    plt.scatter(cb_twos[0][0],cb_twos[1][0],color=def_color)
    plt.plot(cb_twos[0],cb_twos[1],color=def_color)
    
    plt.scatter(linebackers[0][0],linebackers[1][0],color=def_color)
    plt.plot(linebackers[0],linebackers[1],color=def_color)
    plt.scatter(safetys[0][0],safetys[1][0],color=def_color)
    plt.plot(safetys[0],safetys[1],color=def_color)

    #plot offensive line
    #olinex,oliney = o_line(origin)
    #plt.scatter(olinex,oliney,color=off_color)

    plt.xlim([0,50])
    plt.show()
    
    """
    plt.plot(snaps[1],snaps[2],color='orange')
    #print('z2: ',snap_zvals)
    plt.plot(holds[1],holds[2],color=off_color)
    if len(throws[0]) == 1:
        plt.plot(linebackers[1],linebackers[2],color=def_color)
    if len(throws[0]) > 1:
        plt.plot(throws[1],throws[2],color='orange')
    plt.ylim([0,4])

    plt.show()
    """
    