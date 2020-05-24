#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:18:15 2020

@author: WS
"""

import AmericanFootballFunctionsv5 as AFF

"""
Name, height, speed, acceleration, cradius, jump
AFF.player_details(name, height, forty, firstsplit,secondsplot,arm_length,jump)
"""

"""Cleveland Browns"""
#potentially import details in future
odell = AFF.player_details('Odell',1.81,4.43,1.57,2.58,0.83,0.98)

jarvis = AFF.player_details('Jarvis',1.82,4.77,1.57,2.58,0.81,0.72)

    
baker_height = 1.84
baker_speed = [0.5,0.5]
baker_acc = 0
name_baker = 'Baker'
prov_baker = [name_baker,baker_height,baker_speed,baker_acc]

chubb = AFF.player_details('Chubb',1.8,4.52,1.62,2.67,0.81,0.98)

browns_offense = ['red',prov_baker,odell,jarvis,chubb]

"""Tampa Bay Bucs"""

brady_height = 1.84
brady_speed = [0.5]
brady_acc = 0
brady_name = 'Brady'
prov_brady = [brady_name,brady_height,brady_speed,brady_acc]

evans = AFF.player_details('Evans',1.95,4.53,1.6,2.66,0.89,0.94)

godwin = AFF.player_details('Godwin',1.85,4.42,1.65,2.75,0.8,0.91)

name_jonesr = 'Jones'
height_jonesr = 1.8
speed_jonesr = [AFF.forty_speed(4.65),0]
acc_jonesr = 2 * (40 * 0.9144) / (4.65**2)
jonesr = [name_jonesr,height_jonesr,speed_jonesr,acc_jonesr]

bucs_offense = ['red',prov_brady,evans,godwin,jonesr]

"""Dallas Cowboys"""

vander = AFF.player_details('Vander Esch',1.94,4.65,1.56,2.69,0.86,1)

haha = AFF.player_details('HaHa Clinton-Dix',1.86,4.58,1.6,2.68,0.82,0.84)

cowboys_defense = ['blue',vander,haha]

"""Philadephia Eagles"""



"""Baltimore Ravens"""

lamar = AFF.player_details('Lamar',1.89,4.34,4.34,4.34,0.84,0.75)
ingram = AFF.player_details('Ingram',1.76,4.53,1.54,2.58,0.78,0.8)
marquise = AFF.player_details('Hollywood',1.76,4.34,4.34,4.34,0.8,0.8)
ravens_offense = ['purple',lamar,ingram,marquise,'Nah']

