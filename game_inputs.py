#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 13:34:11 2020

@author: WS
"""

print("""Route options include: 
WR: Vert""")
    
from math import pi
import play_functions as pf
from random import random

def wr_inputs(wr_one,wr_two,position):
    
    wr_rec_input = input(f"Would you like {wr_one['name']} to line up on the left (L) or right (R)? ")
    wr_one_line = input(f"How far in from the sideline would you like {wr_one['name']} to line up, on our 50 metre wide field? ")
    wr_two_line = input(f"How far in from the sideline would you like {wr_two['name']} to line up, on our 50 metre wide field? ")
    
    if wr_rec_input == 'L':
        wr_one_x = int(float(wr_one_line))
        wr_two_x = 50 - int(float(wr_two_line))
    else:
        wr_one_x = 50 - int(float(wr_one_line))
        wr_two_x = int(float(wr_two_line))
    
    wr_one_pos = [wr_one_x,position[1]]    
    wr_two_pos = [wr_two_x,position[1]]
    
    #wr_one['track_x'].append(wr_one_x)
    
    pf.add_position_to_track(wr_one,wr_one_pos)
    pf.add_position_to_track(wr_two,wr_two_pos)
    

def wr_route_options(wr_one,wr_two):
    
    wr_one_route = input(f"What route would you like {wr_one['name']} to run? ")
    
    wr_two_route = input(f"What route would you like {wr_two['name']} to run? ")
    
    wr_one['status'].append(wr_one_route)
    wr_two['status'].append(wr_two_route)
    
def wr_route_gen(wr_one,wr_two,time):
    
    if wr_one['status'][-1] == 'Vert':
        wr_one_coord = [wr_one['track_x'][-1],102]
        wr_one_x,wr_one_y,wr_one_z = pf.p_to_p_in_t(time,wr_one,wr_one_coord,'B')
        
    if wr_two['status'][-1] == 'Vert':
        wr_two_coord = [wr_two['track_x'][-1],102]
        wr_two_x,wr_two_y,wr_two_z = pf.p_to_p_in_t(time,wr_two,wr_two_coord,'B')
        
    return(wr_one_x,wr_one_y,wr_one_z,wr_two_x,wr_two_y,wr_two_z)    

def qb_inputs(qb):
    qb_y_input = float(input(f"How far behind the O-line would you like {qb['name']} to line up? "))
    if qb_y_input > 3:
        qb_y_input = 3
    qb_y = -qb_y_input
    
    option = 'Throw'#input(f"Would you like qb['name'] to Run, Throw or Handoff the ball? ')
    qb['status'].append(option)
    
    return(qb_y)
    
def rb_inputs(offense):
    choice = input(f"Would you like {offense['RB']['name']} to run or block? ")
    
    if 'un' in choice:
        print('He blocks instead')
    
    rb_action = 'Block'
    
    return(rb_action)

def te_inputs(offense):
    choice = input(f"Would you like {offense['RB']['name']} to run or block? ")
    
    if 'un' in choice:
        print('He blocks instead')
    
    rb_action = 'Block'
    
    return(rb_action)
    
def throw_inputs(offense):
    throw_side = input('Would you like to throw for the left (L) or right (R)? ')
    
    hangle_input = input('At what angle would you like to throw the ball up the pitch? ')
    hangle = float(hangle_input) * (pi/180)

    ballspeed_input = input('How fast would you like to throw the ball on release? ')
    ballspeed = float(ballspeed_input)
    
    vangle_input = input('What angle would you like to launch the ball at? ')
    vangle = (float(vangle_input)) * (pi/180)
    
    holdtime_input = input(f"How long would you like {offense['QB']['name']} to hold onto the ball for before releasing? ")
    holdtime = float(holdtime_input) 

    return(holdtime,throw_side,hangle,vangle,ballspeed)
