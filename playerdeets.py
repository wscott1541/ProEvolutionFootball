#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:18:15 2020

@author: WS
"""

import random
import AmericanFootballFunctionsv5 as AFF

"""
Name, height, speed, acceleration, cradius, jump
"""

"""Cleveland Browns"""
#potentially import details in future
wrspeed_odell = 8.2564333086
acc_odell = AFF.acc_calc(1.57,2.58)
cradius_odell = 0.83185
height_odell = 5 * 0.3045 + 11 * 0.0254
jump_odell = 0.98
name_odell = 'Odell'
odell = [name_odell,height_odell,wrspeed_odell,acc_odell,cradius_odell,jump_odell]

wrspeed_jarvis = (40 * 0.9144)/4.77
cradius_jarvis = 31.75 * 0.0254
height_jarvis = 5 * 0.3045 + 11 * 0.0254
acc_jarvis = AFF.acc_calc(1.73,2.84)
jump_jarvis = 0.72
name_jarvis = 'Jarvis'
jarvis = [name_jarvis,height_jarvis,wrspeed_jarvis,acc_jarvis,cradius_jarvis,jump_jarvis]
    
baker_height = 1.84
baker_speed = 0.5
name_baker = 'Baker'
prov_baker = [name_baker,baker_height,baker_speed]

rbspeed_chubb = (40 * 0.9144)/4.52
rbheight_chubb = 1.8
rbacc_one = 2*10 / (1.62 ** 2)
rbacc_two = 2*10 / ((2.67-1.62)**2)
rbacc_chubb = (rbacc_one + rbacc_two)/2
chubb = ['Chubb',rbheight_chubb,rbspeed_chubb,rbacc_chubb]

browns_offense = ['red',prov_baker,odell,jarvis,chubb]

"""Tampa Bay Bucs"""

brady_height = 1.84
brady_speed = 0.5
brady_name = 'Brady'
prov_brady = [brady_name,brady_height,brady_speed]

name_evans = 'Evans'
height_evans = 1.95
speed_evans = AFF.forty_speed(4.53)
acc_evans = AFF.acc_calc(1.6,2.66)
crad_evans = 0.89
jump_evans = 0.94
evans = [name_evans,height_evans,speed_evans,acc_evans,crad_evans,jump_evans]

name_godwin = 'Godwin'
height_god = 1.85
speed_god = AFF.forty_speed(4.42)
acc_god = AFF.acc_calc(1.65,2.75)
crad_god = 0.8
jump_god = 0.91
godwin = [name_godwin,height_god,speed_god,acc_god,crad_god,jump_god]

name_jonesr = 'Jones'
height_jonesr = 1.8
speed_jonesr = AFF.forty_speed(4.65)
acc_jonesr = 2 * (40 * 0.9144) / (4.65**2)
jonesr = [name_jonesr,height_jonesr,speed_jonesr,acc_jonesr]

bucs_offense = ['red',prov_brady,evans,godwin,jonesr]

"""Dallas Cowboys"""

lb_height = 1.94
lb_cradius = 0.86
lb_acc = AFF.acc_calc(1.56,2.69)
lb_jump = 1
lb_speed = 1 * (40 * 0.9144)/4.65
vander = ['Vander Esch', lb_height, lb_speed, lb_acc, lb_cradius, lb_jump]

s_height = 1.86
s_cradius = 0.82
s_jump = 0.84
s_speed = (40 * 0.9144)/4.58
s_acc = AFF.acc_calc(1.6,2.68)
haha = ['HaHa Clinton-Dix', s_height, s_speed, s_acc, s_cradius, s_jump]

cowboys_defense = ['blue',vander,haha]

"""Philadephia Eagles"""



"""Baltimore Ravens"""

lamar = AFF.player_details('Lamar',1.89,4.34,4.34,4.34,0.84,0.75)
ingram = AFF.player_details('Ingram',1.76,4.53,1.54,2.58,0.78,0.8)
marquise = AFF.player_details('Hollywood',1.76,4.34,4.34,4.34,0.8,0.8)
ravens_offense = ['purple',lamar,ingram,marquise,'Nah']

