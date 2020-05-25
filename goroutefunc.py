#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:48:34 2020

@author: WS
"""

import AmericanFootballFunctionsv5 as AFF
import random
import matplotlib.pyplot as plt
from math import pi


"""Gather player details"""

import playerdeets as playerdeets

offense_input = input('Would you like to play as the Browns, Bucs or Ravens? ')
if offense_input == 'Browns':
    offense = playerdeets.browns_offense
elif offense_input == 'Bucs':
    offense = playerdeets.bucs_offense
elif offense_input == 'Ravens':
    offense = playerdeets.ravens_offense
else:
    print('I said "the Browns, Bucs or Ravens", moron.')

off_color = offense[0]
qb = offense[1]
wr_one = offense[2]
wr_two = offense[3]
rb = offense[4]

defense = playerdeets.cowboys_defense

def_color = defense[0]
linebacker = defense[1]
safety = defense[2]

"""Have an origin that I haven't figured out what to do with"""

origin = [25,0,0]

"""Gather user inputs"""

wr_rec_input = input('Would you like to throw to {} or to {}? '.format(wr_one[0],wr_two[0]))
if wr_rec_input == '{}'.format(wr_one[0]):
    wr = wr_one
    decoy = wr_two
if wr_rec_input == '{}'.format(wr_two[0]):
    wr = wr_two
    decoy = wr_one

#line up the receivers
wrside = input('Would you like {} to line up on the left (L) or right (R)? '.format(wr_rec_input))
wrecline_input = input('How far in from the sideline would you like {} to line up, on our theoretically 50 yards wide field? '.format(wr[0]))
if wrside == 'R':
    wreceiverline = 50 - float(wrecline_input)#50 is the width of the pitch.
elif wrside == 'L':
    wreceiverline = float(wrecline_input) 
wr_start = [wreceiverline,0]
wr.append(wr_start)

#decoy_input = input('How far in from the sideline would you like {} to line up, on our theoretically 50 yards wide field? '.format(decoy[0]))
decoy_input = random.randint(1,15)
if wrside == 'R':
    decoy_line = float(decoy_input)
elif wrside == 'L':
    decoy_line = 50 - float(decoy_input)
decoy_start = [decoy_line,0]
decoy.append(decoy_start)
  
qb_x = origin[0]
qb_y_input = input('How far behind the O-line would you like the QB to line up? ')
qb_y = -float(qb_y_input)
qb_position = [qb_x,qb_y]
qb.append(qb_position)

hangle_input = input('At what angle would you like to throw the ball up the pitch? ')
hangle = float(hangle_input) * (pi/180)

ballspeed_input = input('How fast would you like to throw the ball? ')
ballspeed = float(ballspeed_input)
    
vangle_input = input('What angle would you like to launch the ball at? ')
vangle = (float(vangle_input)) * (pi/180)

holdtime_input = input('How long would you like to hold onto the ball for before releasing? ')
holdtime = float(holdtime_input)

"""Define the function"""

def func(origin,qb,wreceiver,decoy,wrside,ballspeed,hangle,vangle,thold,linebacker,safety):
    
    lb_side_ran = random.randint(0,1)
    if lb_side_ran == 0:
        lb_x_val = -2
    if lb_side_ran == 1:
        lb_x_val = 2
    lb_x_start = origin[0] + lb_x_val
    lb_y_start = origin[1] + random.random()*10 
    lb_start = [lb_x_start,lb_y_start]
    linebacker.append(lb_start)
    
    """SNAP"""
    
    tsnap,snap_x,snap_y,snap_z = AFF.snap(origin,qb)
    snaps = [snap_x,snap_y,snap_z]
    
    qb_x, qb_y, qb_z = AFF.static(tsnap,qb)
    
    wr_x, wr_y, wr_z = AFF.verts(tsnap,wreceiver,1)
    AFF.finalise_deets(wreceiver,tsnap,wr_x,wr_y)
    
    decoy_x, decoy_y, decoy_z = AFF.verts(tsnap,decoy,1)
    AFF.finalise_deets(decoy,tsnap,decoy_x,decoy_y)
    
    lb_direction = random.randint(0,2)#runs at qb=0,left=1, right=2
    
    if lb_direction == 0:
        thru_oline = random.randint(0,50)
        if thru_oline != 0:
            lb_x, lb_y, lb_z = AFF.lb_rush_blocked(tsnap,linebacker,qb,origin)
        else:
            lb_x, lb_y, lb_z = AFF.p_to_stop(tsnap,linebacker,AFF.last_val(qb))
    else:
        if lb_direction == 1:
            lb_x, lb_y, lb_z = AFF.p_to_stop(tsnap,linebacker,[5,AFF.last_val(linebacker)[1]])
        if lb_direction == 2:
            lb_x, lb_y, lb_z = AFF.p_to_stop(tsnap,linebacker,[45,AFF.last_val(linebacker)[1]])
    AFF.finalise_deets(linebacker,tsnap,lb_x,lb_y)
    
    if lb_direction == 0:
        s_rand = random.randint(0,1)
        if s_rand == 0:
            s_start_x = 15
        if s_rand == 1:
            s_start_x = 35
    if lb_direction == 1:
        s_start_x = 35
    if lb_direction == 2:
        s_start_x = 15
    s_start_y = origin[1] + 20 + random.random() * 5
    s_start = [s_start_x,s_start_y]
    safety.append(s_start)
    
    s_x, s_y, s_z = AFF.static(tsnap,safety)
    
    cont_val = 1
    
    """HOLD"""
    
    qb_hold_x, qb_hold_y, qb_hold_z = AFF.verts(thold,qb,-1)
    
    if lb_direction == 0:
        if thru_oline == 0:
            lb_x_hold, lb_y_hold, lb_z_hold = AFF.point_to_chase(thold,linebacker,[qb_hold_x,qb_hold_y])
            sack_array = []
            for i in range(0,len(lb_x_hold)):
                if qb_hold_x[i] < lb_x_hold[i] + 0.75 * linebacker[3] and qb_hold_x[i] > lb_x_hold[i] - 0.75 * linebacker[3] and qb_hold_y[i] < lb_y_hold[i] + (linebacker[3] * 0.75) and qb_hold_y[i] > lb_y_hold[i] - (linebacker[3] * 0.75):
                    cont_val = 0
                    sack_array.append(i)
            if cont_val == 0:
                sack_pos = sack_array[int((len(sack_array))/2)]
                thold = sack_pos * 0.001
                qb_hold_x, qb_hold_y, qb_hold_z = AFF.verts(thold,qb,-1)
                lb_x_hold, lb_y_hold, lb_z_hold = AFF.point_to_chase(thold,linebacker,[qb_hold_x,qb_hold_y])
                throws = 0
        else:
            lb_x_hold, lb_y_hold, lb_z_hold = AFF.lb_rush_blocked(thold,linebacker,qb,origin)
    if lb_direction == 1:
        lb_x_hold, lb_y_hold, lb_z_hold = AFF.p_to_stop(tsnap,linebacker,[5,AFF.last_val(linebacker)[1]])
    if lb_direction == 2:
        lb_x_hold, lb_y_hold, lb_z_hold = AFF.p_to_stop(tsnap,linebacker,[45,AFF.last_val(linebacker)[1]])
    
    qb_x = AFF.join_two(qb_x,qb_hold_x)
    qb_y = AFF.join_two(qb_y,qb_hold_y)
    qb_z = AFF.join_two(qb_z,qb_hold_z)
    AFF.finalise_deets(qb,thold,qb_x,qb_y)
    holds = [qb_hold_x, qb_hold_y, qb_hold_z]
        
    lb_x = AFF.join_two(lb_x,lb_x_hold)
    lb_y = AFF.join_two(lb_y,lb_y_hold)
    lb_z = AFF.join_two(lb_z,lb_z_hold)
    AFF.finalise_deets(linebacker,thold,lb_x,lb_y)
    
    wr_hold_x, wr_hold_y, wr_hold_z = AFF.verts(thold,wreceiver,1)
    wr_x = AFF.join_two(wr_x,wr_hold_x)
    wr_y = AFF.join_two(wr_y,wr_hold_y)
    wr_z = AFF.join_two(wr_z,wr_hold_z)
    AFF.finalise_deets(wreceiver,thold,wr_x,wr_y)
    
    decoy_hold_x, decoy_hold_y, decoy_hold_z = AFF.verts(thold,decoy,1)
    decoy_x = AFF.join_two(decoy_x,decoy_hold_x)
    decoy_y = AFF.join_two(decoy_y,decoy_hold_y)
    decoy_z = AFF.join_two(decoy_z,decoy_hold_z)
    AFF.finalise_deets(decoy,thold,decoy_x,decoy_y)
    
    s_x, s_y, s_z = AFF.static(thold,safety)
    
    """THROW"""
    if cont_val == 1:
        tground = AFF.time_to_ground(qb,ballspeed,vangle)
    
        p_throw_x, p_throw_y, p_throw_z = AFF.throws(tground,ballspeed,qb,hangle,vangle,wrside)
        p_ball = [p_throw_x, p_throw_y, p_throw_z]
        
        tthrow,t_end,cont_val,possessor = AFF.throw_react(p_ball,wreceiver,linebacker,safety)
        #can use the t_end for distance thrown
        throw_x, throw_y, throw_z = AFF.throws(tthrow,ballspeed,qb,hangle,vangle,wrside)
        throws = [throw_x,throw_y,throw_z]
        
        wr_t_x, wr_t_y, wr_t_z = AFF.p_to_stop(tthrow,wreceiver,t_end)
        wr_x = AFF.join_two(wr_x,wr_t_x)
        wr_y = AFF.join_two(wr_y,wr_t_y)
        wr_z = AFF.join_two(wr_z,wr_t_z)
        AFF.finalise_deets(wreceiver,tthrow,wr_x,wr_y)
        
        decoy_t_x, decoy_t_y, decoy_t_z = AFF.verts(tthrow,decoy,1)
        decoy_x = AFF.join_two(decoy_x,decoy_t_x)
        decoy_y = AFF.join_two(decoy_y,decoy_t_y)
        decoy_z = AFF.join_two(decoy_z,decoy_t_z)
        AFF.finalise_deets(decoy,tthrow,decoy_x,decoy_y)
    
        if lb_direction != 0:
            lb_t_x, lb_t_y, lb_t_z = AFF.p_to_stop(tthrow,linebacker,t_end)
            lb_x = AFF.join_two(lb_x,lb_t_x)
            lb_y = AFF.join_two(lb_y,lb_t_y)
            lb_z = AFF.join_two(lb_z,lb_t_z)
            AFF.finalise_deets(linebacker,tthrow,lb_x,lb_y)
        
        s_t_x, s_t_y, s_t_z = AFF.p_to_stop(tthrow,safety,t_end)
        s_x = AFF.join_two(s_x,s_t_x)
        s_y = AFF.join_two(s_y,s_t_y)
        s_z = AFF.join_two(s_z,s_t_z)
        AFF.finalise_deets(safety,tthrow,s_x,s_y)
        
    """POST-THROW"""
    
    if cont_val == 1:
        
        if possessor == wreceiver[0]:#i.e., the ball was caught by the wide receiver
            p_trac,p_safety_racs,p_wr_racs = AFF.def_chase(safety,wreceiver,100,50,100)
            p_trac,p_lb_racs,p_wr_racs = AFF.def_chase(linebacker,wreceiver,100,50,100)
            
            if AFF.last_val(p_safety_racs[1]) < AFF.last_val(p_lb_racs[1]):
                trac,safety_racs,wreceiver_racs = AFF.def_chase(safety,wreceiver,100,50,100)
                
                lb_rac_x,lb_rac_y,lb_rac_z = AFF.point_to_chase(trac,linebacker,wreceiver_racs)
                lb_racs = [lb_rac_x,lb_rac_y,lb_rac_z]
                
            if AFF.last_val(p_lb_racs[1]) < AFF.last_val(p_safety_racs[1]):
                trac,lb_racs,wreceiver_racs = AFF.def_chase(linebacker,wreceiver,100,50,100)
                
                s_rac_x,s_rac_y,s_rac_z = AFF.point_to_chase(trac,safety,wreceiver_racs)
                safety_racs = [s_rac_x,s_rac_y,s_rac_z]
                
            decoy_rac_x, decoy_rac_y,decoy_rac_z = AFF.point_to_chase(trac,decoy,wreceiver_racs)
            decoy_x = AFF.join_two(decoy_x,decoy_rac_x)
            decoy_y = AFF.join_two(decoy_y,decoy_rac_y)
            decoy_z = AFF.join_two(decoy_z,decoy_rac_z)
                
        if possessor == linebacker[0]:
            trac,wreceiver_racs,lb_racs = AFF.def_chase(wreceiver,linebacker,0,50,100)
                
            s_rac_x,s_rac_y,s_rac_z = AFF.point_to_chase(trac,safety,lb_racs)
            safety_racs = [s_rac_x,s_rac_y,s_rac_z]
            
        if possessor == safety[0]:
            trac,wreceiver_racs,safety_racs = AFF.def_chase(wreceiver,safety,0,50,100)
                
            lb_rac_x,lb_rac_y,lb_rac_z = AFF.point_to_chase(trac,linebacker,safety_racs)
            lb_racs = [lb_rac_x,lb_rac_y,lb_rac_z]
            
        wr_x = AFF.join_two(wr_x,wreceiver_racs[0])
        wr_y = AFF.join_two(wr_y,wreceiver_racs[1])
        wr_z = AFF.join_two(wr_z,wreceiver_racs[2])
        
        lb_x = AFF.join_two(lb_x,lb_racs[0])
        lb_y = AFF.join_two(lb_y,lb_racs[1])
        lb_z = AFF.join_two(lb_z,lb_racs[2])
        
        s_x = AFF.join_two(s_x,safety_racs[0])
        s_y = AFF.join_two(s_y,safety_racs[1])
        s_z = AFF.join_two(s_z,safety_racs[2])
        
    wrs = [wr_x, wr_y, wr_z]
        
    decoys = [decoy_x, decoy_y, decoy_z]
        
    lbs = [lb_x, lb_y, lb_z]
        
    safetys = [s_x, s_y, s_z]
    
    times = [tsnap,thold,tthrow]
    if cont_val == 1:
        times.append(trac)
    
    return(snaps,holds,throws,wrs,decoys,lbs,safetys,times)

"""Run the function"""

snaps,holds,throws,wrs,decoys,lbs,safetys,times = func(origin,qb,wr,decoy,wrside,ballspeed,hangle,vangle,holdtime,linebacker,safety)
#func(origin,qb,wreceiver,decoy,target,wrside,ballspeed,vangle,thold,linebacker,safety)

"""Process the outputs"""

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
    plt.plot(throws[0],throws[1],color='orange')

#plot defense
plt.scatter(lbs[0][0],lbs[1][0],color=def_color)
plt.plot(lbs[0],lbs[1],color=def_color)
plt.scatter(safetys[0][0],safetys[1][0],color=def_color)
plt.plot(safetys[0],safetys[1],color=def_color)

#plot offensive line
olinex,oliney = AFF.o_line(origin)
plt.scatter(olinex,oliney,color=off_color)

plt.xlim([0,50])
plt.show()

plt.plot(snaps[1],snaps[2],color='orange')
#print('z2: ',snap_zvals)
plt.plot(holds[1],holds[2],color=off_color)
if len(throws[0]) == 1:
    plt.plot(lbs[1],lbs[2],color=def_color)
if len(throws[0]) > 1:
    plt.plot(throws[1],throws[2],color='orange')
plt.ylim([0,4])
plt.show()

print(times)