#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:33:43 2020

@author: WS
"""

print('Loading...')

import plays

import players

offense,o_colour,defense,d_colour = players.choose_teams()

down = 1
possession = 1
position = [25,0,0] #[x,y,z] format       

while down < 5 and possession == 1 and position < 100:
    
    down, possession, position = plays.choose_play(offense,o_colour,defense,d_colour,position)
    
    