#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:49:48 2020

@author: WS
"""

def acc_calc(a,b):
    if a != b:
        acc_one = 2*(10*0.9144) / (a ** 2)
        acc_two = 2*(10*0.9144) / ((b-a)**2)
    else:
        acc_one = 2*(40*0.9144) / (a**2)
        acc_two = 2*(40*0.9144) / (a**2)
    acc = (acc_one + acc_two)/2
    return(acc)
    
def forty_speed(a):
    speed = (40 * 0.9144)/a
    return(speed)
    
def player_details(name,height,forty,firstsplit,secondsplit,arm_length,vert_jump):
    speed = forty_speed(forty)
    acc = acc_calc(firstsplit,secondsplit)
    player = {'name': name, 
              'height': height,
              'speed': speed,
              'acc': acc,
              'arm': arm_length,
              'vert': vert_jump,
              'current speed': [0],
              'position': []}
    return(player)
    
def qb_details(name, height):
    qb = {'name': name,
          'height': height,
          'speed': 0.5,
          'acc': 0.25,
          'current speed': [0],
          'position':[]}
    return(qb)
    
def offense_details(name,colour_a,colour_b,qb,wr_one,wr_two,running_back,tight_end):
    offense = {'name': name,
               'colour A': colour_a,
               'colour B': colour_b,
               'QB': qb,
               'WR1': wr_one,
               'WR2': wr_two,
               'RB': running_back,
               'TE': tight_end}
    return(offense)

def cb_details(name,height,forty,firstsplit,secondsplit,arm_length,vert_jump,cmp_pct):
    speed = forty_speed(forty)
    acc = acc_calc(firstsplit,secondsplit)
    cb = {'name': name, 
              'height': height,
              'speed': speed,
              'acc': acc,
              'arm': arm_length,
              'vert': vert_jump,
              'current speed': [0],
              'position': [],
              '%age': cmp_pct}
    return(cb)    
    
def defense_details(name,colour_a,colour_b,rusher,mlb,safety,cb_one,cb_two):
    defense = {'name': name,
               'colour A': colour_a,
               'colour B': colour_b,
               'rusher': rusher,
               'LB': mlb,
               'S': safety,
               'CB1': cb_one,
               'CB2': cb_two}
    return(defense)
    
"""Cleveland Browns"""

odell = player_details('Odell Beckham',1.81,4.43,1.57,2.58,0.83,0.98)
jarvis = player_details('Jarvis Landry',1.82,4.77,1.57,2.58,0.81,0.72)
chubb = player_details('Nick Chubb',1.8,4.52,1.62,2.67,0.81,0.98)
hooper = player_details('Austin Hooper',1.92,4.72,1.63,2.75,0.86,0.84)
baker = qb_details('Baker Mayfield',1.84)

browns_offense = offense_details('Cleveland Browns','red','black',baker,odell,jarvis,chubb,hooper)

"""San Francisco 49ers"""

n_bosa = player_details('Nick Bosa',1.92,4.79,4.79,4.79,0.84,0.85)
warner = player_details('Fred Warner',1.91,4.64,1.55,2.65,0.81,0.98)
ward = player_details('Jimmie Ward',1.79,4.47,1.56,2.54,0.79,0.97)
sherman = cb_details('Richard Sherman',1.9,4.56,1.61,2.65,0.81,0.97,62.3)
ahkello = cb_details('Ahkello Witherspoon',1.9,4.45,1.53,2.57,0.84,1.03,56.6)

niners_defense = defense_details('San Francisco 49ers','red','white',n_bosa,warner)


def choose_teams():
    offense_choice = input('Select offensive team: ')
    
    if offense_choice == 'Browns':
        offense = browns_offense

    defense_choice = input('Select defensive team: ')
    
    if defense_choice == '49ers':
        defense = niners_defense
    
    offense_colour = offense['colour A']
    
    if offense['colour A'] == defense['colour A']:
        defense_colour = defense['colour B']
    else:
        defense_colour = defense['colour A']
    
    return(offense,offense_colour,defense,defense_colour)
