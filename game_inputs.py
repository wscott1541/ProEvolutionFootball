#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 13:34:11 2020

@author: WS
"""

from random import random

def wr_inputs(offense):
    
    wr_rec_input = input(f"Would you like to throw to {offense['WR1']['name']} or to {offense['WR2']['name']}? ")
    if wr_rec_input == '{}'.format(offense['WR1']['name']):
        wr = offense['WR1']
        decoy = offense['WR2']
    if wr_rec_input == '{}'.format(offense['WR2']['name']):
        wr = offense['WR2']
        decoy = offense['WR1']
        
    wrside = input(f"Would you like {wr['name']} to line up on the left (L) or right (R)? ")
    wrecline_input = input(f"How far in from the sideline would you like {wr['name']} to line up, on our theoretically 50 yards wide field? ")
    if wrside == 'R':
        wrec_line = 50 - float(wrecline_input)#50 is the width of the pitch.
    elif wrside == 'L':
        wrec_line = float(wrecline_input) 
     
    decoy_input = random.randint(1,15)
    if wrside == 'R':
        decoy_line = float(decoy_input)
    elif wrside == 'L':
        decoy_line = 50 - float(decoy_input)
    
    qb_y_input = float(input(f"How far behind the O-line would you like {offense['QB']['name']} to line up? "))
    if qb_y_input > 3:
        qb_y_input = 3
    qb_y = -qb_y_input
    
    return(wr,decoy,wrec_line,decoy_line,qb_y)
    
def rb_inputs(offense):
    choice = input(f"Would you like {offense['RB']['name']} to run or block? ")
    
    if 'un' in choice:
        print('He blocks instead')
    
    rb_action = 'Block'
    
    return(rb_action)
    
