#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:33:43 2020

@author: WS
"""

print('Loading...')

import new

import players

offense,o_colour,defense,d_colour = players.choose_teams()

down = 1
possession = 1
position = [25,0,0] #[x,y,z] format
mtg = 10       

while down < 5 and possession == 1 and position < 100:
    
    down, mtg, possession, position = new.play(offense,o_colour,defense,d_colour,position,mtg)
    
    