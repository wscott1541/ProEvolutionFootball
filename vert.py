#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:48:34 2020

@author: WS
"""

#import AmericanFootballFunctionsv5 as AFF
import random
#import matplotlib.pyplot as plt
from math import pi

import play_functions as pf

import game_inputs as gi
    
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

    holdtime_input = input(f"How long would you like {offense['QB']['name']to hold onto the ball for before releasing? ")
    holdtime = float(holdtime_input)   
    
    return(throw_side,ballspeed,hangle,vangle,holdtime)

def play(offense,o_colour,defense,d_colour,position):

    origin = position
    
    wrec, decoy, wrec_line, decoy_line, qb_y = player_position_inputs(offense)
    
    wrec_position = [wrec_line,position[1]]
    pf.add_position(wrec,wrec_position)
    wrec_speeds = [0]
    dec_position = [[decoy_line,position[1]]]
    dec_speeds = [0]
    
    qb = offense['QB']
    qb_position = [[25,(origin[1]+qb_y)]]
    pf.add_position(qb,qb_position)
    
    rb = offense['RB']
    rb_position = [[(origin[0]-3),(origin[1]-7)]]
    pf.add_position(rb,rb_position)
    
    te = offense['TE']
    te_position = [[origin[0]+6,origin[1]]]
    pf.add_position(te,te_position)

    edge = defense['rusher']
    edge_position = [[origin[0]-6,origin[1]]]
    pf.add_position(edge,edge_position)
    
    lb_action_ran = random.randint(0,2)
    if lb_action_ran == 0:
        lb_action = 'Rush'
    else:
        lb_action = 'Hold'
    lb = defense['LB']
    lb_position = [[25,(position[1]+10)]]
    pf.add_position(lb,lb_position)
    
    s = defense['S']
    s_position = [[25,(position[1]+25)]]
    pf.add_position(s,s_position)
    
    cb_one = defense['CB1']
    cb_two = defense['CB2']
    if offense['WR1']['name'] == wrec['name']:
        cb_one_position = [[wrec_line,position[1]+5]]
        cb_two_position = [[dec_line,position[1]+5]]
    else:
        cb_one_position = [[dec_line,position[1]+5]]
        cb_two_position = [[wrec_line,position[1]+5]]
    pf.add_position(cb_one,cb_one_position)
    pf.add_position(cb_two,cb_two_position)
    
    throw_side,ballspeed, hangle, vangle, thold = throw_inputs(offense)
    
    """SNAP"""
    
    snap_x,snap_y,snap_z = pf.snap(origin,qb)
    tsnap = pf.snap_time(origin,qb)
    snaps = [snap_x,snap_y,snap_z]
    
    qb_x, qb_y, qb_z = pf.static(tsnap,qb)
    
    wr_x, wr_y, wr_z = pf.verts(tsnap,wrec,1)
    pf.finalise_pos_speed(tsnap,wrec,wr_x,wr_y)

    
    dec_x, dec_y, dec_z = pf.verts(tsnap,decoy,1)
    pf.finalise_pos_speed(tsnap,decoy,dec_x,dec_y)
    
    cb_one_x, cb_one_y, cb_one_z = pf.static(tsnap,cb_one)
    cb_one_x, cb_one_y, cb_one_z = pf.static(tsnap,cb_one)
    
    cont_val = 1
    
    """HOLD"""
    
    qb_hold_x, qb_hold_y, qb_hold_z = AFF.verts(thold,qb,-1)
    qb_x = pf.join_two(qb_x,qb_hold_x)
    qb_y = pf.join_two(qb_y,qb_hold_y)
    qb_z = pf.join_two(qb_z,qb_hold_z)
    pf.finalise_pos_speed(thold,qb,qb_x,qb_y)
    
    wr_hold_x, wr_hold_y, wr_hold_z = pf.verts(tsnap,wrec,1)
    wr_x = pf.join_two(wr_x,wr_hold_x)
    wr_y = pf.join_two(wr_y,wr_hold_y)
    wr_z = pf.join_two(wr_z,wr_hold_z)
    pf.finalise_pos_speed(thold,wrec,wr_x,wr_y)
    
    decoy_hold_x, decoy_hold_y, decoy_hold_z = pf.verts(tsnap,decoy,1)
    decoy_x = pf.join_two(decoy_x,decoy_hold_x)
    decoy_y = pf.join_two(decoy_y,decoy_hold_y)
    decoy_z = pf.join_two(decoy_z,decoy_hold_z)
    pf.finalise_pos_speed(thold,decoy,dec_x,dec_y)
    
    lb_x, lb_y, lb_z = pf.static(tsnap+thold,lb,lb_position)
    
    s_x, s_y, s_z = pf.static(tsnap+thold,s,s_position)    
    
    """THROW"""
    if cont_val == 1:
        tground = pf.time_to_ground(qb,ballspeed,vangle)
    
        p_throw_x, p_throw_y, p_throw_z = pf.throws(tground,ballspeed,qb,hangle,vangle,throw_side)
        p_ball = [p_throw_x, p_throw_y, p_throw_z]
        
        tthrow,t_end,possessor,cont_val = pf.throw_react(ball_arrays,throw_side,
                wrec,
                decoy,
                cb_one,
                cb_two,
                lb,
                s)
        
        if cont_val == 1 or possessor != 'NONE':
        
            throw_x, throw_y, throw_z = AFF.throws(tthrow,ballspeed,qb,hangle,vangle,throw_side)
            throws = [throw_x,throw_y,throw_z]
        
            wr_t_x, wr_t_y, wr_t_z = pf.p_to_p_in_t(tthrow,wreceiver,t_end)
            wr_x = pf.join_two(wr_x,wr_t_x)
            wr_y = pf.join_two(wr_y,wr_t_y)
            wr_z = pf.join_two(wr_z,wr_t_z)
            pf.finalise_pos_speed(tthrow,wreceiver,tthrow,wr_x,wr_y)
        
            decoy_t_x, decoy_t_y, decoy_t_z = AFF.verts(tthrow,decoy,1)
            decoy_x = AFF.join_two(decoy_x,decoy_t_x)
            decoy_y = AFF.join_two(decoy_y,decoy_t_y)
            decoy_z = AFF.join_two(decoy_z,decoy_t_z)
            AFF.finalise_deets(decoy,tthrow,decoy_x,decoy_y)
    
            if lb_direction != 0:
                lb_t_x, lb_t_y, lb_t_z = AFF.p_to_stop(tthrow,linebacker,t_end)
            else:
                    lb_t_x, lb_t_y, lb_t_z = AFF.static(tthrow,linebacker)
                    lb_x = AFF.join_two(lb_x,lb_t_x)
                    lb_y = AFF.join_two(lb_y,lb_t_y)
                    lb_z = AFF.join_two(lb_z,lb_t_z)
                    AFF.finalise_deets(linebacker,tthrow,lb_x,lb_y)
        
            s_t_x, s_t_y, s_t_z = AFF.p_to_stop(tthrow,safety,t_end)
            s_x = AFF.join_two(s_x,s_t_x)
            s_y = AFF.join_two(s_y,s_t_y)
            s_z = AFF.join_two(s_z,s_t_z)
            AFF.finalise_deets(safety,tthrow,s_x,s_y)
        
            qb_t_x, qb_t_y, qb_t_z = AFF.static(tthrow,qb)
            qb_x = AFF.join_two(qb_x,qb_t_x)
            qb_y = AFF.join_two(qb_y,qb_t_y)
            qb_z = AFF.join_two(qb_z,qb_t_z)
            AFF.finalise_deets(qb,tthrow,qb_x,qb_y)
        
        else:
            tthrow = tground
        
    else:
        tthrow = 0
        
        
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
            
            decoy_rac_x, decoy_rac_y, decoy_rac_z = AFF.static(trac,decoy)
            decoy_x = AFF.join_two(decoy_x,decoy_rac_x)
            decoy_y = AFF.join_two(decoy_y,decoy_rac_y)
            decoy_z = AFF.join_two(decoy_z,decoy_rac_z)
            
        if possessor == safety[0]:
            trac,wreceiver_racs,safety_racs = AFF.def_chase(wreceiver,safety,0,50,100)
                
            lb_rac_x,lb_rac_y,lb_rac_z = AFF.point_to_chase(trac,linebacker,safety_racs)
            lb_racs = [lb_rac_x,lb_rac_y,lb_rac_z]
            
            decoy_rac_x, decoy_rac_y, decoy_rac_z = AFF.static(trac,decoy)
            decoy_x = AFF.join_two(decoy_x,decoy_rac_x)
            decoy_y = AFF.join_two(decoy_y,decoy_rac_y)
            decoy_z = AFF.join_two(decoy_z,decoy_rac_z)
            
        wr_x = AFF.join_two(wr_x,wreceiver_racs[0])
        wr_y = AFF.join_two(wr_y,wreceiver_racs[1])
        wr_z = AFF.join_two(wr_z,wreceiver_racs[2])
        
        lb_x = AFF.join_two(lb_x,lb_racs[0])
        lb_y = AFF.join_two(lb_y,lb_racs[1])
        lb_z = AFF.join_two(lb_z,lb_racs[2])
        
        s_x = AFF.join_two(s_x,safety_racs[0])
        s_y = AFF.join_two(s_y,safety_racs[1])
        s_z = AFF.join_two(s_z,safety_racs[2])
        
        qb_rac_x, qb_rac_y, qb_rac_z = AFF.static(trac,qb)
        qb_x = AFF.join_two(qb_x,qb_rac_x)
        qb_y = AFF.join_two(qb_y,qb_rac_y)
        qb_z = AFF.join_two(qb_z,qb_rac_z)
    
    else:
        trac = 0
     
    holds = [qb_x, qb_y, qb_z]
    
    wrs = [wr_x, wr_y, wr_z]
        
    decoys = [decoy_x, decoy_y, decoy_z]
        
    lbs = [lb_x, lb_y, lb_z]
        
    safetys = [s_x, s_y, s_z]
    
    times = [tsnap,thold,tthrow,trac]
    
    return(snaps,holds,throws,wrs,decoys,lbs,safetys,times)

"""Run the function"""

snaps,holds,throws,wrs,decoys,lbs,safetys,times = func(origin,qb,wr,decoy,wrside,ballspeed,hangle,vangle,holdtime,linebacker,safety)
#func(origin,qb,wreceiver,decoy,target,wrside,ballspeed,vangle,thold,linebacker,safety)

"""Plot the outputs"""
AFF.plot_lines(times,off_color,def_color,origin,snaps,holds,throws,wrs,decoys,lbs,safetys)
