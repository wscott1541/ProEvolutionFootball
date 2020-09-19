
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 18:56:32 2020

@author: WS
"""

#import AmericanFootballFunctionsv5 as AFF
import random
#import matplotlib.pyplot as plt
from math import pi

import play_functions as pf

import game_inputs as gi

def pull_offense(offense):
    quarterback = offense['QB']
    receiver_one = offense['WR1']
    receiver_two = offense['WR2']
    runningback = offense['RB']
    tightend = offense['TE']
    
    return(quarterback,receiver_one,receiver_two,runningback,tightend)
    
def pull_defense(defense):
    edgerusher = defense['rusher']
    linebacker = defense['LB']
    safety = defense['S']
    corner_one = defense['CB1']
    corner_two = defense['CB2']
    
    return(edgerusher,linebacker,safety,corner_one,corner_two)

def play(offense,o_colour,defense,d_colour,position,mtg):

    origin = position
    
    qb,wr_one,wr_two,rb,te = pull_offense(offense)
    
    edge,lb,s,cb_one,cb_two = pull_defense(defense)
    
    
    """SORT TEAM AND INPUTS"""
    
    
    qb_y = gi.qb_inputs(qb) + origin[1]
    qb_position = [origin[0],qb_y]
    
    pf.add_position_to_track(qb,qb_position)
        
    gi.wr_inputs(wr_one,wr_two,origin)

    rb_position = [(origin[0]-3),(origin[1]-7)]
    pf.add_position_to_track(rb,rb_position)
    
    
    te_position = [origin[0]+6,origin[1]]
    pf.add_position_to_track(te,te_position)

    
    edge_position = [origin[0]-6,origin[1]]
    pf.add_position_to_track(edge,edge_position)
    
    lb_action_ran = 1#random.randint(0,2)
    if lb_action_ran == 0:
        lb_action = 'Rush'
    else:
        lb_action = 'Hold'
    
    lb['status'].append(lb_action)
    lb_position = [25,(position[1]+10)]
    pf.add_position_to_track(lb,lb_position)
    
    
    s_position = [25,(position[1]+20)]
    pf.add_position_to_track(s,s_position)
    
    
    cb_one_position = [wr_one['track_x'][0],position[1]+5]
    cb_two_position = [wr_two['track_x'][0],position[1]+5]
    pf.add_position_to_track(cb_one,cb_one_position)
    pf.add_position_to_track(cb_two,cb_two_position)
    
    snap_x,snap_y,snap_z = pf.snap(origin,qb)
    tsnap = pf.snap_time(origin,qb)
    
    snaps = [snap_x,snap_y,snap_z]
    
    if qb['status'][-1] == 'Throw':
    
        gi.wr_route_options(wr_one,wr_two)
        
        thold,throw_side,hangle,vangle,ballspeed = gi.throw_inputs(offense)
        #do all receiver options before throw
                
        sack_val = 0
    
        if sack_val == 0:
        
            t_pre = thold+tsnap
            
            qb_x,qb_y,qb_z = pf.verts(thold,qb,-1)
            qb_pos = [qb_x[-1],qb_y[-1]]
            pf.add_position_to_track(qb,qb_pos)
    
            wr_one_x,wr_one_y,wr_one_z,wr_two_x,wr_two_y,wr_two_z = gi.wr_route_gen(wr_one,wr_two,t_pre)    
            
            pf.point_to_chase(t_pre,cb_one,[wr_one_x,wr_one_y],'Y')
            pf.point_to_chase(t_pre,cb_two,[wr_two_x,wr_two_y],'Y')
    
            tground = pf.time_to_ground(qb,ballspeed,vangle)
            
            p_throw_x, p_throw_y, p_throw_z = pf.throws(tground,ballspeed,qb,hangle,vangle,throw_side)
            p_ball = [p_throw_x, p_throw_y, p_throw_z]
            
            tthrow,t_end,possessor,cont_val = pf.throw_react(p_ball,throw_side,
                wr_one,
                wr_two,
                cb_one,
                cb_two,
                lb,
                s)

            if cont_val == 1:
                throw_x, throw_y, throw_z = pf.throws(tthrow,ballspeed,qb,hangle,vangle,throw_side)
                throws = [throw_x,throw_y,throw_z]     
                
                pf.catch_outcomes(possessor,t_end,tthrow,
                    wr_one,
                    wr_two,
                    cb_one,
                    cb_two,
                    s,
                    lb)
            
            else:
                tthrow = tground
                
                t_out = pf.time_to_out(ballspeed,hangle,vangle,qb)
                
                if t_out > tground:
                    tthrow = tground
                if t_out < tground:
                    tthrow = t_out
                
                throw_x, throw_y, throw_z = pf.throws(tthrow,ballspeed,qb,hangle,vangle,throw_side)
                throws = [throw_x, throw_y, throw_z]
                t_end = [throw_x[-1],throw_y[-1]]
                
                pf.miss_outcomes(throw_side,t_end,tthrow,
                    wr_one,
                    wr_two,
                    cb_one,
                    cb_two,
                    s,
                    lb)
                
        
    #holds = [qb_x, qb_y, qb_z]
    
    
    pf.plot_lines(o_colour,d_colour,origin,snaps,qb,throws,wr_one,wr_two,cb_one,cb_two,lb,s)
    
    

"""Run the function"""

import players

offense = players.browns_offense
defense = players.niners_defense

down = 1
possession = 1
position = [25,20,0] #[x,y,z] format
mtg = 10  

play(offense,'red',defense,'white',position,mtg)    
    
"""THROW"""
"""
    if cont_val == 1:
        
        
        
        
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
    """    
        
"""POST-THROW"""
"""
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
    """
