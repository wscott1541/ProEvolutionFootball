#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:01:19 2020

@author: WS
"""

##import math
##PI = math.pi
##print(PI)

#import matplotlib.pyplot as plt
#x = [1, 2, 3, 4]
#print(x)
#y = [x**2 for i in x]
#print(y)
#plt.plot(x,y)
#plt.show()

#import matplotlib.pyplot as plt

#a = [1,2,3,4]
#b = [1,4,9,16]
#plt.plot(a,b)
#plt.show()

#xs = list(range(0,20))
#ys = [x**2 for x in xs]
#plt.plot(xs,ys)
#plt.show()

#xs = list(range(0,20))
#ys = [x**2 for x in xs]
#runliney = list(range(0,350))
#runlinex = [15] * len(runliney)
#plt.plot(runlinex,runliney)
#plt.plot(xs,ys)
#plt.show()

#to do
#equations for the throw (arcing the throw for correct time - constant angle with inputted speed)
#gather data
#work out how to pick odell - i.e. type 'odell' and get that to define the variables
#work out time dependency and animation

#wr_name = input ('Enter a number: ')


#import widereceiverset

#widereceiver(wr_name)

#test_text = input ('Enter a number: ')
#wreceiver = int(test_text)

#test_number = int(test_input)
#wreceiver = '{}'.format(test_input)

#print(wreceiver)

#print(widereceiverset.wrspeed)

#import pandas as pd

#df = pd.read_csv(r'/Users/SoapBar/Documents/Test/widereceiversets.csv')
#print(df)

#test_text = input ('Enter a number: ')#anything entered is automatically a string
#print(test_text)

#if test_text == "4":#quotes because input is a string
#    b = 8
#    print(b)
#    
#else: 
#    print('fuck you')
    
##widereceiver runs

#define wide receiver

#wrlineup_input = input ('Where will your receiver line up (ideally an integer between 21 and 30): ')
#wreceiverline = int(wrlineup_input)
#catchline = wreceiverline + 1

#import matplotlib.pyplot as plt

#xs = list(range(15,catchline))
#ys = [(2.5 * x - (2.5*15)) for x in xs]
#runliney = list(range(0,35))
#runlinex = [wreceiverline] * len(runliney)
#olinex = list(range(10,21))
#oliney = [2] * len(olinex)
#print(olinex)
#print(oliney)
#xhashmarksleft = list(range(1,4))
#yhashmarkset = [0,5,10,15,20,25,30]
#yhashmarks = [yhashmarkset] * len(xhashmarksleft)
#xhashmarksright = list(range(27,30))
#print(len(xhashmarksleft))
#plt.rcParams['axes.facecolor'] = 'green'#has to go before the plot
#plt.plot(xhashmarksleft,yhashmarks,color='white')
#plt.plot(xhashmarksright,yhashmarks,color='white')
#plt.plot(xhashmarks,([5] * yhashmarks),color='white')  
#plt.plot(runlinex,runliney,color='blue')
#plt.plot(xs,ys,'#f0a000')       
#plt.scatter(15,0,color = 'blue')
#plt.plot(olinex,oliney,color='blue')
#plt.xlim([0,30])
#plt.show()

#wrside = input('Would you like your wr to line up on the left (L) or right (R)?')
#print(wrside)
#if wrside == 'R':
#    print('FUCKYES')

#import random

#print(random.randint(0,1))

#holdtime_input = input('How long would you like to hold onto the ball for before releasing? ')
#holdtime = float(holdtime_input)

#import random

#if holdtime < 0.75:
#    print('In trying to get the ball away too soon, you fumble the football.')
#    recovery = random.randint(0,1)
#    if recovery == 0:
#        print('Fortunately, an offensive lineman sits on the football but, while you retain possession, your chance at glory is gone.')
#    elif recovery == 1:
#        fumble_return = random.randint(0,1)
#        if fumble_return == 0:
#            print('You dive for the ball, but a defensive lineman leaps on the ball and, simultaneously, your wrist.  There is a sickening crunch those in the crowd will later swear they heard to whoever in the pub gives them time to tell their tale.  You will never throw a football again.')
#        if fumble_return == 1:
#            print("The ball spills out, bobbles, and is seized by a linebacker.  He charges forward.  You dive forward, hoping to dislodge and recover the ball once more.  Your helmet connects with the linebacker's shoulder. There is a sickening crunch those in the crowd will later swear they heard to whoever in the pub gives them time to tell their tale.  You will never walk again.")    

#wrspeed_jarvis = (40 * 0.9144)/4.77
#cradius_jarvis = 31.75 * 0.0254

#print(wrspeed_jarvis)
#print(cradius_jarvis)

#from math import sin

#height = (75 * sin(0.785398)) ** 2 - (0.05)**2
#print(height)

#holdtime = 2

#holdlist = [0] * int(holdtime)

#print(holdlist)

#from math import pi

#angle = 45 * (pi/180)
#print(angle)
#print(pi/4)

#def height_t(i,s,u,t,a):
#    h = s + u * t + 0.5 * a * (t ** 2)
#    return(h)

#heights = height()    

#def func(a):
#    b = 2 * a[0]
#    c = 2 * a[1]
#    return([b,c])

#in_put = [2,3]

#output = func(in_put)

#print(output)

#q = []

#for x in range(6):
#    y = 2 * x
#    q.append(y)
    
#def height_t(s,u,t,a):
#    h = s + u * t + 0.5 * a * (t ** 2)
#    return(h)

#h_vals = []
#x_vals = []
#for x in range(1, 6, 0.1):
#    height = height_t(0.5,8,x,9.8)
#    h_vals.append(height)
#    x_vals.append(x)

#print('x: ',x_vals)
#print('h: ',h_vals)

#import matplotlib.pyplot as plt

#plt.plot(x_vals,h_vals)

'''
this is now a bit of a mess, but could redefine as positions by defining all as equations (once worked out how to fix the integer step issue)

catch = []

for i in range()
if h[i] = x[i]
c = 1
catch.append(c)

if catch != []
catchval = 1
except could start with catchval = 0, append to catchval and remove

'''

#import numpy

#for i in numpy.arange(0,5.5,0.5):
#    print(i)

#a = [0,1,2,3]
#b = [4,5,6]
#for x in range(0,2):
#    c = b[x]
#    a.append(c)
#print(a)

#can add the hold to the throw.
"""
#for i in range(0,(len(wr_y_catch)+1)):
#    if throw_yvals[i] < wr_y_catch[i] + (cradius * 1.25) and throw_yvals[i] > wr_y_catch[i] - (cradius * 0.3) and throw_xvals[i] < wr_x_catch[i] + cradius and throw_xvals[i] > wr_x_catch[i] - cradius and throw_zvals[i] < wrheight + 0.3 * cradius and throw_zvals[i] > wrheight * 0.25:
#        catch_val = 1
#        times_array.append[i]
"""
#import AmericanFootballFunctionsv2 as AFF
#import numpy

#time = 5
#speed = 0.5
#wr_start = [25,0]

#wr_y_catch = AFF.vert_y(time,speed,wr_start)

#print('wr_y_catch: ',wr_y_catch)

#y_vals = []
#t_sta = 0
#t_fin = time + 0.001
#for t in numpy.arange(t_sta,t_fin,0.001):
#    y_val = wr_start[1] + speed * t
#    y_vals.append(y_val)

#print('y_vals: ',y_vals)
"""
#def test2(a,b,c):
#    summative = a + b + c
#    multiplicative = a * b * c
#    return 'abc',summative,multiplicative

#a, b, c = test2(1,2,3)

#print(a)
#print(b)
#print(c)
"""
#import random

#print(random.random())
#print(random.randint(0,3))

#a = [1,2,3,4]
#b = a[(len(a)-1)]
#print(b)

#def test2(a,b,c):
#    summative = a + b + c
#    multiplicative = a * b * c
#    return('abc',summative,multiplicative)

#d, e, f = test2(1,2,3)

#print(d)
#print(e)
#print(f)

#a = [0,1,2,3]
#b = [4,5,6]
#a.append(b)
#print(a)

#def func_one(a,b):
#    c = a * b
#    return(c)

#def func_two(a,b,c):
#    d = func_one(a,b) + c
#    return(d)
#    
#e = func_two(2,2,3)
#print(e)

#fuck = ['balls',0]
#output = 'You literally threw the ball behind {}.'.format(fuck[0])  

#print(output)

#import random
#val = random.random()
#print(round(val,3))

#wr_option = random.randint(0,1)
#print(wr_option)

#x_vals, y_vals, z_vals = [],[],[]
#print(x_vals)
#print(y_vals)

#a = [0,[1,2]]
#b = a[1][0]
#print(b)

#import AmericanFootballFunctionsv2 as AFF

#a = [1,2,3]
#b = [4,5,6]
#c = [7,8,9]
#d = AFF.join_three(a,b,c)

#print(a)
#print(d)

#e = [1,2,3]
#f = [4,5,6]
#g = AFF.join_two(e,f)

#print(e)
#print(g)

#h = [1,2]

#def join_two(a,b):
#    blank = []
#    for x in range(0,(len(a))):
#        val = a[x]
#        blank.append(val)
#    for x in range(0,(len(b))):
#        val = b[x]
#        blank.append(val)
#    return(blank)

#def join_three(a,b,c):
#    blank = []
#    for x in range(0,(len(a))):
#        val = a[x]
#        blank.append(val)
#    for x in range(0,(len(b))):
#        val = b[x]
#        blank.append(val)
#    for x in range(0,(len(c))):
#        val = c[x]
#        blank.append(val)
#    return(blank)

    
#i = [1,2]
#j = [3,4]

#k,l,m = join_two(i,j)

#print(k)
#print(l)
#print(m)

#g = join_two(e,f)
#print(g)
#print(e)
#print(f)

#g = join_two(a,e)
#print(g)

#def join_three(a,b,c):
#    d = join_two(a,b)
#    e = join_two(d,c)
#    return(e)

#h = join_three(a,b,c)
#print(h)
#qbheight = 2
#qbspeed = 0.5
#qb_x = 1
#qb_y = 2

#qbposition = [qb_x,qb_y]
#qb = [qbheight,qbspeed,qbposition]

#a = qb[2][1]
#print(a)

#a = round(1.75)
#b = round(1.25)

#print(a)
#print(b)
#import AmericanFootballFunctionsv2 as AFF
#g = 9.8
#u = 15
#s = 0.5
#time_a = AFF.quad_one(-g,u,-s)
#time_b = AFF.quad_two(-g,u,-s)
#print(time_a)
#print(time_b)
#time_c = AFF.quad_greater(-g,u,-s)
#print(time_c)

#import matplotlib.pyplot as plt
#import numpy
#import AmericanFootballFunctionsv2 as AFF

#from math import sin, cos, atan

#def point_to_point(start,objective,speed,time):
    
#    x_disp = objective[0] - start[0]
#    y_disp = objective[1] - start[1]
    
#    if x_disp > 0:
#        x_value = 1
#    if x_disp < 0:
#        x_value = -1
#    if y_disp > 0:
#        y_value = 1
#    if y_disp < 0:
#        y_value = -1
    
#    if x_disp == 0:
#        x_speed = 0
#        y_speed = speed
#    elif y_disp == 0:#don't strictly need, but whatever.
#        x_speed = speed
#        y_speed = 0
#    elif x_disp == 0 and y_disp == 0:
#        x_speed = 0
#        y_speed = 0
#    else:
#        angle = atan(abs(y_disp)/abs(x_disp))
#        x_speed = speed * cos(angle)
#        y_speed = speed * sin(angle)
#    
"""    x_vals = []
    y_vals = []
    
    t_sta = 0
    t_fin = time + 0.001
    for t in numpy.arange(t_sta,t_fin,0.001):
        move_x = start[0] + x_value * x_speed * t
        x_vals.append(move_x)
        move_y = start[1] + y_value * y_speed * t
        y_vals.append(move_y)
    return(x_vals,y_vals)"""
        
#a = [4,4]
#b = [1,2]

#xs,ys = point_to_point(a,b,1,1)
#plt.plot(xs,ys)


#s = 4
#time = 1

#xs, ys = point_to_point(a,b,s,time)

#plt.plot(xs,ys)   

#time = 10

#start = [0,5]
#chase_start = [20,0]
#chase_x = AFF.vert_x(time,chase_start)
#chase_y = AFF.vert_y(time,6,chase_start,1)
#chase_array = [chase_x,chase_y]
"""   
def point_to_chase(start,chase_arrays,chaser_speed,chase_time):
    t_sta = 0
    t_fin = chase_time + 0.001
    full_time = []
    for t in numpy.arange(t_sta,t_fin,0.001):
        full_time.append(t)
    length = len(full_time)
    chasing_x = [start[0]]
    chasing_y = [start[1]]
    for i in range(1,length):
        x_disp = chase_arrays[0][i] - chasing_x[(i - 1)]
        y_disp = chase_arrays[1][i] - chasing_y[(i - 1)]
        
        if x_disp > 0:
            x_value = 1
        if x_disp < 0:
            x_value = -1
        if y_disp > 0:
            y_value = 1
        if y_disp < 0:
            y_value = -1
        
        if x_disp == 0:
            x_speed = 0
            y_speed = chaser_speed
        elif y_disp == 0:#don't strictly need, but whatever.
            x_speed = chaser_speed
            y_speed = 0
        elif x_disp == 0 and y_disp == 0:
            x_speed = 0
            y_speed = 0
        else:
            angle = atan(y_disp/x_disp)
            x_speed = chaser_speed * cos(angle)
            y_speed = chaser_speed * sin(angle)
        move_x = chasing_x[(i - 1)] + x_value * x_speed * 0.001
        chasing_x.append(move_x)
        move_y = chasing_y[(i - 1)] + y_value * y_speed * 0.001
        chasing_y.append(move_y)
    return(chasing_x,chasing_y)
   """ 
#x_s,y_s = point_to_chase(start,chase_array,6,4)

#plt.plot(chase_x,chase_y)
#plt.plot(xs,ys)
#plt.show()
    
#x_vals,y_vals = point_to_point([1,1],[4,4],1,1)
#chases_x,chases_y = point_to_chase([1,4],[x_vals,y_vals],2,2)

#plt.plot(x_vals,y_vals)
#plt.plot(chases_x,chases_y)        
"""    
def p_to_p(start,objective,speed):
    
    x_disp = objective[0] - start[0]
    y_disp = objective[1] - start[1]
    
    distance = sqrt((x_disp ** 2) + (y_disp ** 2))
    
    if x_disp > 0:
        x_value = 1
    if x_disp < 0:
        x_value = -1
    if y_disp > 0:
        y_value = 1
    if y_disp < 0:
        y_value = -1
    
    if x_disp == 0:
        x_speed = 0
        x_value = 0
        y_speed = speed
    elif y_disp == 0:#don't strictly need, but whatever.
        x_speed = speed
        y_speed = 0
        y_value = 0
    elif x_disp == 0 and y_disp == 0:
        x_speed = 0
        x_value = 0
        y_speed = 0
        y_value = 0
    else:
        angle = atan(abs(y_disp)/abs(x_disp))
        x_speed = speed * cos(angle)
        y_speed = speed * sin(angle)
    
    x_vals = []
    y_vals = []
    
    time = round((distance/speed),3)
    
    t_sta = 0
    t_fin = time + 0.001
    for t in numpy.arange(t_sta,t_fin,0.001):
        move_x = start[0] + x_value * x_speed * t
        x_vals.append(move_x)
        move_y = start[1] + y_value * y_speed * t
        y_vals.append(move_y)
    return(x_vals,y_vals,time)

"""
#from math import sqrt, pi, tan
"""
def p_to_stop(start,objective,speed,time):
    
    x_disp = objective[0] - start[0]
    y_disp = objective[1] - start[1]
    
    
    if x_disp > 0:
        x_value = 1
    if x_disp < 0:
        x_value = -1
    if y_disp > 0:
        y_value = 1
    if y_disp < 0:
        y_value = -1
    
    if x_disp == 0:
        x_speed = 0
        x_value = 0
        y_speed = speed
    elif y_disp == 0:#don't strictly need, but whatever.
        x_speed = speed
        y_speed = 0
        y_value = 0
    elif x_disp == 0 and y_disp == 0:
        x_speed = 0
        x_value = 0
        y_speed = 0
        y_value = 0
    else:
        angle = atan(abs(y_disp)/abs(x_disp))
        x_speed = speed * cos(angle)
        y_speed = speed * sin(angle)
    
    x_vals = []
    y_vals = []
        
    t_sta = 0
    t_fin = time + 0.001
    for t in numpy.arange(t_sta,t_fin,0.001):
        move_x = x_value * x_speed * t
        new_x = start[0] + move_x
        if abs(move_x) <= abs(x_disp):
            x_vals.append(new_x)
        else:
            x_vals.append(objective[0])
        move_y = y_value * y_speed * t
        new_y = start[1] + move_y
        if abs(move_y) <= abs(y_disp):
            y_vals.append(new_y)
        else:
            y_vals.append(objective[1])
    return(x_vals,y_vals)    
    
start_a = [25,20]
finish_a = [10,20]
start_b = [25,10]
finish_b = [10,10]
speed = 5

x_as,y_as = p_to_stop(start_a, finish_a, 5, 2)
x_bs,y_bs = p_to_stop(start_b,finish_b, 5, 18)

print('x_as: ',x_as)
print('y_as: ',y_as)
print('x_bs: ',x_bs)
print('y_bs: ',y_bs)

plt.plot(x_as,y_as,color='orange')
plt.plot(x_bs,y_bs,color='blue')    
"""

#speed = 5

#x_runner = AFF.vert_x(5,[25,10])
#y_runner = AFF.vert_y(5,speed,[25,10],-1)
#runner = [x_runner,y_runner]

#x_chaser,y_chaser = AFF.point_to_chase([25,15],runner,5,5)

#plt.plot(x_runner,y_runner,color='red')
#plt.plot(x_chaser,y_chaser,color='blue')


#def static(start,height,time):
#    x_val = start[0]
#    y_val = start[1]
#    z_val = height * (2/3)
    
#    t_sta = 0
#    t_fin = time + 0.001
    
#    x_vals = []
#    y_vals = []
#    z_vals = []
    
#    for t in numpy.arange(t_sta,t_fin,0.001):
#        x_vals.append(x_val)
#        y_vals.append(y_val)
#        z_vals.append(z_val)
        
#    return(x_vals,y_vals,z_vals)
    
#start = [1,2]
#height = 3    
#xs,ys,zs = static(start,height,2)

#print(xs)
#print(ys)
#print(zs)

#a = [1,2,3]
#b = [1,2]
#a.append(b)
#print(a)

#import AmericanFootballFunctionsv5 as AFF
"""
def add_to_zeroth(a,b):
    new_zero = a[0] + b
    new_one = a[1]
    new = [new_zero,new_one]
    return(new)

def add_to_oneth(a,b):
    new_zero = a[0]
    new_one = a[1] + b
    new = [new_zero,new_one]
    return(new)
    
def add_to_both(a,b):
    new_zero = a[0] + b
    new_one = a[1] + b
    new = [new_zero,new_one]
    return(new)

target = [5,10]
obstacle = [5,5]
start = [5,0]
height = 3

distance = 1

speed = 1

target_a = add_to_zeroth(obstacle,distance)

p_one_x, p_one_y, p_one_z, p_one_t = AFF.p_to_p(start,target_a,speed,height)

p_two_x, p_two_y, p_two_z, p_two_t = AFF.p_to_p(target_a,target,speed,height)

xs = AFF.join_two(p_one_x, p_two_x)
ys = AFF.join_two(p_one_y, p_two_y)
zs = AFF.join_two(p_one_z, p_two_z)

total_time = p_one_t + p_two_t - 0.001

#plt.plot(xs,ys)

def chop_first(a):
    new = []
    for i in range(1,len(a)-1):
        val = a[i]
        new.append(val)
    return(new)
"""
"""
def off_runner_speed_calc(offensive_speed,offensive_position,defender_position,pitch_width,direction):#offense is relative to the ball (i.e. whoever holds the ball)
    x_disp = offensive_position[0] - defender_position[0]
    if x_disp < 0:
        x_val = -1
    if x_disp > 0:
        x_val = 1
    y_disp = offensive_position[1] - defender_position[1]
    
    if x_disp == 0:
        if y_disp * direction >= 0:    
            x_speed = 0
            y_speed = direction * offensive_speed
        if y_disp * direction < 0:
            if offensive_position[0] < pitch_width/2:
                temp_val = -1
            if offensive_position[0] > pitch_width/2:
                temp_val = 1
            x_speed = temp_val * offensive_speed * cos(30 * pi/180)
            y_speed = direction * offensive_speed * sin(30 * pi/180)
        ratio = 0
    else:
        ratio = abs(y_disp / x_disp)
        if ratio >= 1:
            if y_disp * direction >= 0:
                x_speed = 0
                y_speed = direction * offensive_speed
            if y_disp * direction < 0:
                x_speed = x_val * offensive_speed * cos(30 * pi/180)
                y_speed = direction * offensive_speed * sin(30 * pi/180)
        if ratio < 1:
            x_speed = x_val * offensive_speed * cos(45 * pi/180)
            y_speed = direction * offensive_speed * sin(45 * pi/180)
    
    if offensive_position[0] < 0.5 or offensive_position[0] > pitch_width - 0.5:
        x_speed = 0
        y_speed = direction * offensive_speed
    
    #x_speeds = chop_first(x_speed)
    #y_speeds = chop_first(y_speed)
    
    return(x_speed,y_speed)

x_vals = [24]
y_vals = [0]

for t in numpy.arange(0,10.1,0.1):
    speed = 5
    start = [AFF.last_val(x_vals),AFF.last_val(y_vals)]
    defender = [24,5]
    xspeed,yspeed = off_runner_speed_calc(speed,start,defender,50,1)
    new_x = start[0] + xspeed * 0.1
    x_vals.append(new_x)
    new_y = start[1] + yspeed * 0.1
    y_vals.append(new_y)

#plt.show()
plt.plot(x_vals,y_vals) 
plt.scatter(25,5)
plt.xlim([0,50])
plt.show()

def def_runner_speed_calc(defensive_speed,defender_position,offensive_position,pitch_width,direction):#offense is relative to the ball (i.e. whoever holds the ball)#direction means the direction the linemen on the man's side would be facing
    x_disp = defender_position[0] - offensive_position[0]
    if x_disp < 0:
        x_val = 1
    if x_disp > 0:
        x_val = -1
    y_disp = defender_position[1] - offensive_position[1]
    #if y_disp >= 0:
    #    y_val = -1
    #if y_disp < 0:
    #    y_val = 1
    
    #separation = sqrt((x_disp**2) + (y_disp**2))
    
    if x_disp == 0:
        x_speed = 0
        if y_disp == 0:
            y_speed = 0
        else:
            if y_disp >= 0:
                y_speed = defensive_speed * direction
            else:
                y_speed = defensive_speed * direction * (-1)
    else:
        ratio = abs(y_disp/x_disp)
        if ratio >= 1:
            angle = atan(ratio)
            x_speed = defensive_speed * cos(angle) * x_val
            y_speed = defensive_speed * sin(angle) * direction * (-1)
        else:
            if y_disp * direction < 0:
                x_speed = defensive_speed * x_val
                y_speed = 0
            if y_disp * direction >= 0:
                x_speed = defensive_speed * cos(45 * pi/180) * x_val
                y_speed = defensive_speed * sin(45 * pi/180) * direction * (-1)
     
    #if separation < 1.5:
          
    #x_speeds = chop_first(x_speed)
    #y_speeds = chop_first(y_speed)
    
    return(x_speed,y_speed)
       
x_vals = [3]
y_vals = [0]

for t in numpy.arange(0,10.1,0.001):
    speed = 5
    start = [AFF.last_val(x_vals),AFF.last_val(y_vals)]
    attacker = [24,5]
    xspeed,yspeed = def_runner_speed_calc(speed,start,attacker,50,1)
    new_x = start[0] + xspeed * 0.001
    x_vals.append(new_x)
    new_y = start[1] + yspeed * 0.001
    y_vals.append(new_y)

#plt.show()
plt.plot(x_vals,y_vals) 
plt.scatter(25,5)
plt.xlim([0,50])
plt.show()

def_xs = [40]
def_ys = [80]
def_speed = 4

off_xs = [20]
off_ys = [10]
off_speed = 6

for t in numpy.arange(0,20,0.001):
    def_pos = [AFF.last_val(def_xs),AFF.last_val(def_ys)]
    off_pos = [AFF.last_val(off_xs),AFF.last_val(off_ys)]
    
    def_x_speed,def_y_speed = def_runner_speed_calc(def_speed,def_pos,off_pos,50,-1)
    off_x_speed,off_y_speed = off_runner_speed_calc(off_speed,off_pos,def_pos,50,1)
    
    new_def_x = def_pos[0] + def_x_speed * 0.001
    new_def_y = def_pos[1] + def_y_speed * 0.001
    new_off_x = off_pos[0] + off_x_speed * 0.001
    new_off_y = off_pos[1] + off_y_speed * 0.001
    
    def_xs.append(new_def_x)
    def_ys.append(new_def_y)
    off_xs.append(new_off_x)
    off_ys.append(new_off_y)
    
plt.plot(off_xs,off_ys,color='blue')
plt.plot(def_xs,def_ys,color='red')
plt.xlim([0,50])
plt.ylim([0,100])
  
"""
"""
def def_to_man(def_speed,def_pos,off_pos):
    
    x_disp = def_pos[0] - off_pos[0]
    y_disp = def_pos[1] - off_pos[1]
        
    if x_disp > 0:
        x_val = -1
    if x_disp < 0:
        x_val = 1
    if y_disp > 0:
        y_val = -1
    if y_disp < 0:
        y_val = 1
        
    if x_disp == 0:
        x_speed = 0
        y_speed = def_speed * y_val
    elif y_disp == 0:#don't strictly need, but whatever.
        x_speed = def_speed * x_val
        y_speed = 0
    elif x_disp == 0 and y_disp == 0:
        x_speed = 0
        y_speed = 0
    else:
        ratio = abs(y_disp/x_disp)
        angle = atan(ratio)
        x_speed = def_speed * cos(angle) * x_val
        y_speed = def_speed * sin(angle) * y_val
        
    return(x_speed,y_speed)

def def_speed_cal(def_speed,def_pos,off_pos,endzone,pitch_width):
    x_disp = def_pos[0] - off_pos[0]
    y_disp = def_pos[1] - off_pos[1]
    
    if x_disp > 0:
        x_val = -1
    if x_disp < 0:
        x_val = 1
    
    if def_pos[1] < endzone:
        y_val = 1
    if def_pos[1] > endzone:
        y_val = -1
    
    if x_disp == 0:
        x_speed, y_speed = def_to_man(def_speed,def_pos,off_pos)
    else:
        ratio = y_disp/x_disp
        if abs(endzone - def_pos[1]) < abs(endzone - off_pos[1]):
            if ratio > tan(60 * pi/180):
                x_speed, y_speed = def_to_man(def_speed,def_pos,off_pos)
            elif ratio < tan(30 * pi/180):
                x_speed = def_speed * cos(30 * pi/180) * x_val
                y_speed = def_speed * sin(30 * pi/180) * y_val
            else:
                x_speed = def_speed * x_val
                y_speed = 0
        if abs(endzone - def_pos[1]) >= abs(endzone - off_pos[1]):
            if ratio > tan(60 * pi/180):
                x_speed, y_speed = def_to_man(def_speed,def_pos,off_pos)
            elif ratio < tan(30 * pi/180):
                x_speed = def_speed * cos(45 * pi/180) * x_val
                y_speed = def_speed * sin(45 * pi/180) * y_val
            else:
                x_speed = def_speed * cos(60 * pi/180) * x_val
                y_speed = def_speed * sin(60 * pi/180) * y_val
    
    if abs(endzone - def_pos[1]) < 0.5:
        x_speed, y_speed = def_to_man(def_speed,def_pos,off_pos)
    
    if  pitch_width - def_pos[0] < 0.5 or def_pos[0] < 0.5:
        x_speed = 0
        y_speed = off_speed * y_val * (-1)
    
    separation = sqrt((x_disp**2) + (y_disp**2))
    if separation < 5 or separation > 20:
        x_speed, y_speed = def_to_man(def_speed,def_pos,off_pos)
    
    return(x_speed, y_speed)    
        

def off_speed_cal(off_speed,off_pos,def_pos,endzone,pitch_width):
    x_disp = off_pos[0] - def_pos[0]
    y_disp = off_pos[1] - def_pos[1]
    
    if x_disp > 0:
        x_val = 1
    if x_disp < 0:
        x_val = -1
    if x_disp == 0:
        if off_pos[0] < pitch_width/2:
            x_val = -1
        if off_pos[0] > pitch_width/2:
            x_val = 1
    
    if off_pos[1] < endzone:
        y_val = 1
    if off_pos[1] > endzone:
        y_val = -1
    
    if pitch_width - off_pos[0] < 0.5 or off_pos[0] < 0.5:
        if abs(x_disp) < 1.25:
            x_speed = 0
            y_speed = off_speed * y_val
        else:
            if off_pos[0] < 0.5:
                x_val = 1
            else:
                x_val = -1
            
    if abs(endzone - off_pos[1]) > abs(endzone - def_pos[1]): 
        if x_disp == 0:
            x_speed = off_speed * cos(30 * pi/180) * x_val
            y_speed = off_speed * sin(30 * pi/180) * y_val
        else:
            ratio = y_disp/x_disp
            if ratio > tan(60 * pi/180):
                x_speed = off_speed * cos(30 * pi/180) * x_val
                y_speed = off_speed * sin(30 * pi/180) * y_val
            elif ratio < tan(30 * pi/180):
                x_speed = off_speed * cos(60 * pi/180) * x_val
                y_speed = off_speed * sin(60 * pi/180) * y_val
            else:
                x_speed = off_speed * cos(45 * pi/180) * x_val
                y_speed = off_speed * sin(45 * pi/180) * y_val
    
    if abs(endzone - off_pos[1]) <= abs(endzone - def_pos[1]):
        if x_disp == 0:
            x_speed = 0
            y_speed = off_speed * y_val
        else:
            ratio = y_disp/x_disp
            if ratio > tan(60 * pi/180):
                x_speed = 0
                y_speed = off_speed * sin(30 * pi/180) * y_val
            elif ratio < tan(30 * pi/180):
                x_speed = off_speed * cos(45 * pi/180) * x_val
                y_speed = off_speed * sin(45 * pi/180) * y_val
            else:
                x_speed = off_speed * cos(60 * pi/180) * x_val
                y_speed = off_speed * sin(60 * pi/180) * y_val
    
    separation = sqrt((x_disp**2) + (y_disp**2))
    if separation > 20:
        x_speed = 0
        y_speed = off_speed * y_val
    
    return(x_speed,y_speed)
"""
"""    
def_xs = [40]
def_ys = [80]
def_speed = 2

#a = [AFF.last_val(def_xs),AFF.last_val(def_ys)]
#print(a[0])
#print(a[1])

off_xs = [20]
off_ys = [10]
off_speed = 3

for t in numpy.arange(0,40,0.001):
    def_pos = [AFF.last_val(def_xs),AFF.last_val(def_ys)]
    off_pos = [AFF.last_val(off_xs),AFF.last_val(off_ys)]
    
    def_x_speed,def_y_speed = def_speed_cal(def_speed,def_pos,off_pos,100,50)
    #def_x_speed,def_y_speed = def_to_man(def_speed,def_pos,off_pos)
    off_x_speed,off_y_speed = off_speed_cal(off_speed,off_pos,def_pos,100,50)
    
    
    new_def_x = def_pos[0] + def_x_speed * 0.001
    new_def_y = def_pos[1] + def_y_speed * 0.001
    new_off_x = off_pos[0] + off_x_speed * 0.001
    new_off_y = off_pos[1] + off_y_speed * 0.001
    
    def_xs.append(new_def_x)
    def_ys.append(new_def_y)
    off_xs.append(new_off_x)
    off_ys.append(new_off_y)
    
plt.plot(off_xs,off_ys,color='blue')
plt.plot(def_xs,def_ys,color='red')
plt.xlim([0,50])
plt.ylim([0,100])
plt.show()
"""
"""
def def_chase(def_speed,off_speed,def_start,def_arm,off_start,endzone,pitch_width):
    
    def_xs = [def_start[0]]
    def_ys = [def_start[1]]
    
    off_xs = [off_start[0]]
    off_ys = [off_start[1]]
    
    del_x = AFF.last_val(def_xs) - AFF.last_val(off_xs)
    del_y = AFF.last_val(def_ys) - AFF.last_val(off_ys)
    init_sep = sqrt((del_x**2) + (del_y**2))
    
    separations = [init_sep]
    
    t = 0
    while -1 < AFF.last_val(off_ys) and AFF.last_val(off_ys) < (endzone + 1) and AFF.last_val(separations) > def_arm:
        
        def_x = AFF.last_val(def_xs)
        def_y = AFF.last_val(def_ys)
        def_pos = [def_x,def_y]
        
        off_x = AFF.last_val(off_xs)
        off_y = AFF.last_val(off_ys)
        off_pos = [off_x,off_y]
        
        def_x_speed,def_y_speed = def_speed_cal(def_speed,def_pos,off_pos,100,50)
        off_x_speed,off_y_speed = off_speed_cal(off_speed,off_pos,def_pos,100,50)
        
        def_x_val = AFF.last_val(def_xs) + def_x_speed * 0.001
        def_y_val = AFF.last_val(def_ys) + def_y_speed * 0.001
        off_x_val = AFF.last_val(off_xs) + off_x_speed * 0.001
        off_y_val = AFF.last_val(off_ys) + off_y_speed * 0.001
        
        def_xs.append(def_x_val)
        def_ys.append(def_y_val)
        off_xs.append(off_x_val)
        off_ys.append(off_y_val)
        
        x_sep = def_x - off_x
        y_sep = def_y - off_y
        sep =  sqrt((x_sep**2) + (y_sep**2))
        separations.append(sep)

        t += 0.001
        
    time = round(t,3)
    
    def_vals = [def_xs,def_ys]
    off_vals = [off_xs,off_ys]
    
    return(def_vals,off_vals,time)

off_sta = [20,10]
def_sta = [40,80]

off_speed = 8
def_speed = 7
def_cra = 0.9
    
def_vals,off_vals,time =  def_chase(def_speed,off_speed,def_sta,def_cra,off_sta,100,50)

print(time)
plt.plot(off_vals[0],off_vals[1],color='blue')
plt.plot(def_vals[0],def_vals[1],color='red')
plt.xlim([0,50])
plt.ylim([0,100])
plt.show()
    
    
#print(def_xs) 
#print(off_xs)
    
      
"""
""" 
    ratio = y_disp/x_disp
    
    if y_dis = 0
        
    if x_disp > 0:
        x_value = 1
    if x_disp < 0:
        x_value = -1
    if y_disp > 0:
        y_value = 1
    if y_disp < 0:
        y_value = -1
        
    if x_disp == 0:
        x_speed = 0
        x_value = 0
        y_speed = chaser_speed
    elif y_disp == 0:#don't strictly need, but whatever.
        x_speed = chaser_speed
        y_speed = 0
        y_value = 0
    elif x_disp == 0 and y_disp == 0:
        x_speed = 0
        x_value = 0
        y_speed = 0
        y_value = 0
    else:
        angle = atan(y_disp/x_disp)
        
        
        x_speed = abs(chaser_speed * cos(angle))
        y_speed = abs(chaser_speed * sin(angle))
    return(x_speed,y_speed)

def run_with_chase(runner_start,chaser_start,runner_speed,chaser_speed,reach):
    
    runner_x = runner_start[0]
    runner_xs = []
    runner_y = runner_start[1]
    runner_ys = []
    
    chaser_x = chaser_start[0]
    chaser_xs = []
    chaser_y = chaser_start[1]
    chaser_ys = []
    
    x_disp = chaser_x - runner_x
    y_disp = chaser_y - runner_y
    separation = sqrt((x_disp**2) + (y_disp**2))
    
    times = []
    t = 0
    while 0 < runner_x < 10 and 0 < runner_y < 10 and separation < reach:
        chaser_x = AFF.last_val(chaser_xs)
        chaser_y = AFF.last_val(chaser_ys)
        chaser_pos = [chaser_x,chaser_y]
        
        runner_x = AFF.last_val(runner_xs)
        runner_y = AFF.last_val(runner_ys)
        runner_post = [runner_x,runner_y]
        
        x_disp = AFF.last_val(chaser_xs) - AFF.last_val(runner_xs)
        y_disp = AFF.last_val(chaser_ys) - AFF.last_val(runner_ys)
        
        if x_disp > 0:
            x_value = 1
        if x_disp < 0:
            x_value = -1
        if y_disp > 0:
            y_value = 1
        if y_disp < 0:
            y_value = -1
        
        if x_disp == 0:
            x_speed = 0
            x_value = 0
            y_speed = chaser_speed
        elif y_disp == 0:#don't strictly need, but whatever.
            x_speed = chaser_speed
            y_speed = 0
            y_value = 0
        elif x_disp == 0 and y_disp == 0:
            x_speed = 0
            x_value = 0
            y_speed = 0
            y_value = 0
        else:
            angle = atan(y_disp/x_disp)
            x_speed = abs(chaser_speed * cos(angle))
            y_speed = abs(chaser_speed * sin(angle))
        move_x = chasing_x[(i - 1)] + x_value * x_speed * 0.001
        chasing_x.append(move_x)
        move_y = chasing_y[(i - 1)] + y_value * y_speed * 0.001
        chasing_y.append(move_y)
        
        
        x_val = runner_x + speed * t
        x_vals.append(x_val)
        times.append(t)
        t += 0.001
                
    time = AFF.last_val(times)
    
    
    
    
    
    
    cont_array = [0]
    cont = len(cont_array)
    
    for t in numpy.arange(0,cont,0.001):
        
        if n < 2
            cont_array.append(cont)
            cont = len(cont_array)
    
    t_sta = 0
    t_fin = chase_time + 0.001
    
    full_time = []
    
    for t in numpy.arange(t_sta,t_fin,0.001):
        full_time.append(t)
    length = len(full_time)
    chasing_x = [start[0]]
    chasing_y = [start[1]]
    chasing_z = [height * (2/3)]
    for i in range(1,length):
        x_disp = chase_arrays[0][i] - chasing_x[(i - 1)]
        y_disp = chase_arrays[1][i] - chasing_y[(i - 1)]
        
        if x_disp > 0:
            x_value = 1
        if x_disp < 0:
            x_value = -1
        if y_disp > 0:
            y_value = 1
        if y_disp < 0:
            y_value = -1
        
        if x_disp == 0:
            x_speed = 0
            x_value = 0
            y_speed = chaser_speed
        elif y_disp == 0:#don't strictly need, but whatever.
            x_speed = chaser_speed
            y_speed = 0
            y_value = 0
        elif x_disp == 0 and y_disp == 0:
            x_speed = 0
            x_value = 0
            y_speed = 0
            y_value = 0
        else:
            angle = atan(y_disp/x_disp)
            x_speed = abs(chaser_speed * cos(angle))
            y_speed = abs(chaser_speed * sin(angle))
        move_x = chasing_x[(i - 1)] + x_value * x_speed * 0.001
        chasing_x.append(move_x)
        move_y = chasing_y[(i - 1)] + y_value * y_speed * 0.001
        chasing_y.append(move_y)
        z_val = height * (2/3)
        chasing_z.append(z_val)
    return(chasing_x,chasing_y,chasing_z)
  
def continue_test(speed):
    start = 1
    
    x_val = start
    x_vals = []
    t = 0
    times = []
    while x_val < 3:
        x_val = start + speed * t
        x_vals.append(x_val)
        times.append(t)
        t += 0.001
                
    time = AFF.last_val(times)
    return(x_vals,time)

some_xs, trun = continue_test(1)

print(some_xs)
print(trun)        
"""

#a = [1,2,3]
#b = AFF.z_populating(3,a)
#print(b)

#t = AFF.quad_greater(-9.8,20,0)
#print(t)

#angle = AFF.throw_angle(23,[10,0],[0,-2.5])
#print(angle*180/pi)

#ball_x = [0,1,2,3,4,5]
#ball_y = [0,1,2,3,4,5]
"""
def int_coords(start,ball_array):

    init_x_disp = ball_array[0][0] - start[0]
    init_y_disp = ball_array[1][0] - start[1]
    
    distances = [sqrt((init_x_disp**2)+(init_y_disp**2))]

    xs = [ball_array[0][1]]
    ys = [ball_array[1][1]]
    
    for i in range(1,len(ball_array[0])):
        x_disp = ball_array[0][i] - start[0]
        y_disp = ball_array[1][i] - start[1]
        
        distance = sqrt((x_disp**2)+(y_disp**2))
        if distance < AFF.last_val(distances):
            distances.append(distance)
            xs.append(ball_array[0][i])
            ys.append(ball_array[1][i])
    
    x = AFF.last_val(xs)
    y = AFF.last_val(ys)    
    return(x,y)
    
"""
    
#int_x,int_y = int_coords([4,5],[ball_x,ball_y])    

#print(int_x,int_y)
"""    
d_one = 10
d_two = 20
d_thr = 40

t_one = 1.57
t_two = 2.58
t_thr = 4.43            
        
s_one = d_one/t_one
s_two = d_two/t_two
s_thr = d_thr/t_thr

a_one = sqrt((2*d_one)/t_one)
a_two = sqrt((2*d_two)/t_two)
a_thr = sqrt((2*d_thr)/t_thr)

print(s_one)
print(s_two)
print(s_thr)            

print(a_one)
print(a_two)
print(a_thr)

a_one_d = sqrt((2*d_one)/t_one)
a_two_d = sqrt((2*(d_two-d_one))/(t_two-t_one))
a_thr_d = sqrt((2*(d_thr-d_two))/(t_thr-t_two))

print(a_one_d)
print(a_two_d)
print(a_thr_d)

print(s)

"""
"""
#import playerdeets as deets

#safety,linebacker = deets.defense

#print(safety)
#print(linebacker)

#xs,ys,zs = AFF.p_to_stop([25, 4.459280158864356], [5, 4.459280158864356], 7.865806451612903, 2.091, 1.94)

#plt.plot(xs,ys)

#a = [1,2,3]
#b = [3,4,5,6]

#a = AFF.join_two(a,b)
#print(a)

#def speed_check(speed,new):
#    if new < speed[0]:
#        speed.append(new)
#    else:
#        speed.append(speed[0])
#i don't want to 

#speeds = [7,0]
#acc = 1
#new_speed = AFF.last_val(speeds) + acc * 5
#speed_check(speeds,new_speed)
#new_speed = AFF.last_val(speeds) + acc * 8
#speed_check(speeds,new_speed)
#print(speeds)

#runner = ['Runner',1.5,[5,0],1,[4,0]]

#xs,ys,zs = AFF.verts(3,runner,1)
#AFF.finalise_deets(runner,1,xs,ys)
#plt.plot(xs,ys)

#print(ys)

#print(runner)

#qb = ['qb',1.84,[25,-2]]

#time = AFF.time_to_ground(qb,38,7)

#xs,ys,zs = AFF.throws(time,38,qb,54,7,'L')

#print(time)

#print(AFF.last_val(xs))
#print(AFF.last_val(ys))
#time = 1.5
#linebacker = AFF.player_details('LB',1.5,5,2,4,0.75,0.75)
#lb_pos = [27,4]
#linebacker.append(lb_pos)

#xs, ys, zs = AFF.p_to_stop(time,linebacker,[5,AFF.last_val(linebacker)[1]])

#plt.plot(xs,ys)

#AFF.finalise_deets(linebacker,time,xs,ys)
#print(linebacker)

#xs, ys, zs = AFF.p_to_stop(time,linebacker,[AFF.last_val(linebacker)[0],8])

#plt.plot(xs,ys)

#AFF.finalise_deets(linebacker,time,xs,ys)
#print(linebacker)

#xs, ys, zs = AFF.p_to_stop(time,linebacker,[20,18])

#plt.plot(xs,ys)

#AFF.finalise_deets(linebacker,time,xs,ys)
#print(linebacker)

#gravity = 9.80665
#ballspeed = 38
#vangle = 7 * pi/180
#qb_height = 1.84

#a = -gravity/2
#b = ballspeed * sin(vangle)
#c = qb_height

#print(a)
#print(b)
#print(c)
#print(4 * a * c)

#print(AFF.quad_one(a,b,c))
#print(AFF.quad_two(a,b,c))
#print(AFF.quad_greater(a,b,c))

time_interval = 0.001

def slant_to_vert(time,runner,turn):
    x_disp = turn[0] - AFF.last_val(runner)[0]
    y_disp = turn[1] - AFF.last_val(runner)[1]
    
    if x_disp > 0:
        x_value = 1
    if x_disp < 0:
        x_value = -1
    if y_disp > 0:
        y_value = 1
    if y_disp < 0:
        y_value = -1
    
    if x_disp == 0:
        x_comp = 0
        x_value = 0
        y_comp = 1
    elif y_disp == 0:#don't strictly need, but whatever.
        x_comp = 1
        y_comp = 0
        y_value = 0
    elif x_disp == 0 and y_disp == 0:
        x_comp = 0
        x_value = 0
        y_comp = 0
        y_value = 0
    else:
        angle = atan(abs(y_disp)/abs(x_disp))
        x_comp = cos(angle)
        y_comp = sin(angle)
    
    x_vals = []
    y_vals = []
    z_vals = []
    
    slant_times = []
    
    t_sta = 0
    t_fin = time + time_interval
    for t in numpy.arange(t_sta,t_fin,time_interval):
        speed = AFF.speed_func(runner,t)
        move_x = x_value * x_comp * speed * t
        new_x = AFF.last_val(runner)[0] + move_x
        if abs(move_x) <= abs(x_disp):
            x_vals.append(new_x)
            slant_times.append(t)
        else:
            x_val = turn[0]
            x_vals.append(x_val)
            
        move_y = y_value * y_comp * speed * t
        new_y = AFF.last_val(runner)[1] + move_y
        if abs(move_y) <= abs(y_disp):
            y_vals.append(new_y)
        else:
            y_val = turn[1] + speed * (t - AFF.last_val(slant_times))
            y_vals.append(y_val)
            
        z_val = runner[1] * (2/3)
        z_vals.append(z_val)
    return(x_vals,y_vals,z_vals)
"""
"""
rb = ['Name', 1.5, [1], 0]
rb_position = [20,-4]
rb.append(rb_position)
turn_position = [18,-2]
xs,ys,zs = slant_to_vert(3,rb,turn_position)

plt.plot(xs,ys)
"""
"""

L = []
positions = [30,20]
L.append(tuple(positions))
new = tuple(L)

L = [1,2,3,4]
L.insert(0,(0,0))
#print(L)

prov_throws = [(0,0),(0,0),(1,1),(2,2)]

tupled_throws = tuple(prov_throws)
#print(tupled_throws)
#print(prov_throws[1:3])

#L = [1, 2, 3, 4, 5, 6]
# Create an iterator
#grouped_l = iter(L)

#print(grouped_l)
# zip the iterator with itself
#zip(it, it)
#[(1, 'term1'), (3, 'term2'), (4, 'term3'), (5, 'termN')]

#string = '12345'
#print(string[-2:])

#test_list = [0,1,2,3,4]
#test_list.reverse()
#print(test_list)

#print(str(2))

from time import time,ctime

t = time()
time = ctime(t)

#print(time)

import datetime as dt

d1 = dt.datetime.strptime('00:08:30','%H:%M:%S')
d2 = dt.datetime.strptime('00:04:30','%H:%M:%S')

dt1 = dt.timedelta(hours=d1.hour, minutes=d1.minute, seconds=d1.second)
dt2 = dt.timedelta(hours=d2.hour, minutes=d2.minute, seconds=d2.second)

#print(dt1+dt2)

t1 = '00:08:30'

t2 = '00:08:30'

#print(float(t1[6:8]))

n = 8.0
#print(round(n))

test = 'testing'
#print(len(test))

test_dates = [0,1,2,2,2,3,8,8,10,13]
test_vals = [0,1,3,2,8,4,8,4,12,4]
#print(test_dates)
#print(test_vals)
#print(len(test_dates))
#print(len(test_vals))
op_a = []
op_b = []
op_c = []
op_d = []
rang = 10
counts = []
val_vals = []
"""
"""
for i in range(0,rang):
    val = i + count - 1
    val_vals.append(val)
    if val + count - 1 != rang + count -1:
        if test_dates[val] == test_dates[-1]:
            test_dates.append(val+1)
            test_vals.append(test_vals[-1])
            op_a.append(i)
        elif test_dates[val] == test_dates[val+1]:
            count += 1
            op_b.append(i)
        elif test_dates[val+1] != val + 1:
            test_dates.insert(val+1,val+1)
            test_vals.insert(val+1,test_vals[val])
            op_c.append(i)
        else:
            op_d.append(i)
        counts.append(count)
"""
"""
count = 0  
rang = 15
i = 0      
while i < rang:
    if test_dates[i] == test_dates[-1] and test_dates[i] != rang:
        test_dates.append(i+1-count)
        test_vals.append(test_vals[-1])
        op_a.append(i)
    elif test_dates[i] == test_dates[i+1]:
        count += 1
        rang += 1
        op_b.append(i)
    elif test_dates[i + 1] != i + 1 - count:
        test_dates.insert(i + 1,i + 1 - count)
        test_vals.insert(i + 1,test_vals[i])  
        op_c.append(i)
    else:
        op_d.append(i)
    i += 1

#print(test_dates)
#print(test_vals)
#print(val_vals)
#print(len(test_dates))
#print(len(test_vals))
#print('last: ',op_a)
#print('skips: ',op_b)
#print('inserts next: ',op_c)
#print('nothing: ',op_d)
#print(counts)

month_1 = 2020 * 12 + 6
month_2 = 2020 * 12 + 3

def month_minus_one(m,yyyy):
    month_val = yyyy * 12 + m - 1
    new = divmod(month_val,12)
    new_year = new[0]
    new_month = new[1]
    if new_month == 0:
        new_year = yyyy - 1
        new_month = 12
    return(new_month,new_year)
    
def month_diff(m1,yyyy1,m2,yyyy2):
    mon1 = yyyy1 * 12 + m1
    mon2 = yyyy2 * 12 + m2
    diff = mon1 - mon2
    return(diff)
"""    
"""
run_vals = []    
for i in len(dates):
    if 'Running' in types[i]:
        run_vals.append(i)
val = run_vals[-1]
earliest_date = dates[val]
"""
"""
date = '2020-08'
print(round(float(date[:4])))
print(round(float(date[5:7])))

new_m, new_y = month_minus_one(1,2020)
print(new_m,new_y)    

dates = []
print(len(dates))

feb_dates = [0,5,7,7,9,10]
feb_vals = [0,2,4,6,5,6]

lim = 15
count = 0
i = 0      
while i < lim:
    prog = []
    if feb_dates[-1] == feb_dates[-2] and feb_dates[-1] != lim:
        feb_dates.append(feb_dates[-1]+1)
        feb_vals.append(feb_vals[-1])
    if feb_dates[i] == feb_dates[-1] and feb_dates[i] != lim:    
        feb_dates.insert(i + 1,i+1-count)
        feb_vals.insert(i + 1,feb_vals[-1])
    elif feb_dates[i] == feb_dates[i+1]:
        count += 1
        lim += 1
    elif feb_dates[i + 1] != i + 1 - count:
        feb_dates.insert(i + 1,i + 1 - count)
        feb_vals.insert(i + 1,feb_vals[i])
    prog.append(i)
    print(prog)
    print(feb_dates)
    i += 1

print(feb_dates)
print(feb_vals)
print(len(feb_dates))
print(len(feb_vals))

import pandas as pd

#data = []

new_df = pd.DataFrame(columns= ['Activity Type','Date','Distance','Time'])

row_one = ['Running','date',5,'10']
a_row = pd.Series(row_one,index=new_df.columns)
mod_df = new_df.append(a_row,ignore_index = True)
new_df = mod_df.sort_values(by='Date')

row_two = ['Running','date',12,'10']
a_row = pd.Series(row_two,index=new_df.columns)
mod_df = new_df.append(a_row,ignore_index = True)
new_df = mod_df.sort_values(by='Date')

print(new_df)

from datetime import datetime

today_string = '2020-06-05'

latest_date_strp = datetime.strptime(today_string,'%Y-%m-%d')
latest_date_object = datetime.timestamp(latest_date_strp)
yester_date_object = latest_date_object - 24 * 60 * 60
yester_dt = datetime.fromtimestamp(yester_date_object)
yester_date_strp = datetime.strftime(yester_dt,'%Y-%m-%d')

print(latest_date_object)
print(yester_date_strp)

time = 0.5
runner = ['Runner',1,[3,0],1,[5,5]]
objective = [1,5]

xs,ys,zs = AFF.p_to_stop(time,runner,objective)

plt.plot(xs,ys)
print(len(xs))

#data = pd.read_csv (r'Activities.csv')  
file_name = "Confirmation.csv"
data = pd.read_csv (r'{}'.format(file_name))
df = pd.DataFrame(data, columns= ['Test date'])
print(df)

string = 'Will Scott'
split_string = string.split()
initial = string[0]
print(split_string)
print(initial)
"""

import play_functions as pf

import numpy

from math import sin, cos, atan, sqrt

from players import odell

runner = odell

start = [5,15]
runner['track_x'].append(start[0])
runner['track_y'].append(start[1])

pf.sine_route(runner,3,'W')
    
import matplotlib.pyplot as plt

plt.plot(runner['track_x'],runner['track_y'])

print(runner)
#angle = acos(((len_a**2)+(len_b**2)-(len_c**2))/(2*len_a*len_b))