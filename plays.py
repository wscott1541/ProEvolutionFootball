#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 12:53:45 2020

@author: WS
"""

import vert

print('Plays available include Vert')

def choose_play(offense,o_colour,defense,d_colour,position):
    play_choice = input('Select play: ')
    
    if play_choice == 'Vert':
        down, possession, position = vert.play(offense,o_colour,defense,d_colour,position)
        