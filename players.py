
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:49:48 2020

@author: WS
"""

"""Per Wiki, Pro Football Reference, nflcombineresults.com
https://matplotlib.org/3.1.0/gallery/color/named_colors.html
20-yard shuttle record: 3.81s, avg 4.25
(https://www.reddit.com/r/NFL_Draft/comments/81snap/looking_at_this_years_rbs_3cone_and_20yard/)"""

avg_s = 4.28
#track = {'x':[],
#         'y':[],
#         'z':[]}

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
    
def player_details(name,side,height,forty,firstsplit,secondsplit,arm_length,vert_jump,shuttle):
    speed = forty_speed(forty)
    acc = acc_calc(firstsplit,secondsplit)
    player = {'name': name,
              'side': side,
              'height': height,
              'speed': speed,
              'acc': acc,
              'arm': arm_length,
              'vert': vert_jump,
              'shuttle': shuttle,
              'current speed': [0],
              'position': [],
              'status': [],
              'track_x': [],
              'track_y': [],
              'track_z': []}
    return(player)
    
def qb_details(name, height):
    qb = {'name': name,
          'side': 'O',
          'height': height,
          'speed': 0.5,
          'acc': 2,
          'current speed': [0],
          'position':[],
          'status': [],
          'track_x': [],
          'track_y': [],
          'track_z': []}
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

def cb_details(name,height,forty,firstsplit,secondsplit,arm_length,vert_jump,cmp_pct,shuttle):
    speed = forty_speed(forty)
    acc = acc_calc(firstsplit,secondsplit)
    cb = {'name': name,
              'side': 'D',
              'height': height,
              'speed': speed,
              'acc': acc,
              'arm': arm_length,
              'vert': vert_jump,
              'shuttle': shuttle,
              'current speed': [0],
              'position': [],
              '%age': cmp_pct,
              'status': [],
              'track_x': [],
              'track_y': [],
              'track_z': []}
    return(cb)    
    
def defense_details(name,colour_a,colour_b,rusher,mlb,safety,cb_one,cb_two):
    defense = {'name': name,
               'colour A': colour_a,
               'colour B': colour_b,
               'rusher': rusher,
               'LB': mlb,
               'S': safety,
               'CB1': cb_one,
               'CB2': cb_two
               }
    return(defense)
    
"""Cleveland Browns"""

odell = player_details('Odell Beckham','O',1.81,4.43,1.57,2.58,0.83,0.98,3.94)
jarvis = player_details('Jarvis Landry','O',1.82,4.77,1.57,2.58,0.81,0.72,avg_s)
chubb = player_details('Nick Chubb','O',1.8,4.52,1.62,2.67,0.81,0.98,4.25)
hooper = player_details('Austin Hooper','O',1.92,4.72,1.63,2.75,0.86,0.84,4.32)
baker = qb_details('Baker Mayfield',1.84)

browns_offense = offense_details('Cleveland Browns','red','black',baker,odell,jarvis,chubb,hooper)

"""San Francisco 49ers"""

n_bosa = player_details('Nick Bosa','D',1.92,4.79,4.79,4.79,0.84,0.85,4.14)
warner = player_details('Fred Warner','D',1.91,4.64,1.55,2.65,0.81,0.98,4.28)
ward = player_details('Jimmie Ward','D',1.79,4.47,1.56,2.54,0.79,0.97,4.24)
sherman = cb_details('Richard Sherman',1.9,4.56,1.61,2.65,0.81,0.97,62.3,4.33)
ahkello = cb_details('Ahkello Witherspoon',1.9,4.45,1.53,2.57,0.84,1.03,56.6,4.13)

niners_defense = defense_details('San Francisco 49ers','red','white',n_bosa,warner,ward,sherman,ahkello)

"""Jacksonville Jaguars"""

minshew = qb_details('Gardner Minshew',1.85)
chark = player_details('DJ Chark','O',1.9,4.34,1.51,2.54,0.82,1.02,4.1)
westbrook = player_details('Dede Westbrook','O',1.83,4.39,1.54,2.54,0.78,0.86,4.34)
eifert = player_details('Tyler Eifert','O',1.97,4.68,1.65,2.69,0.84,0.9,4.34)
robinson = player_details('James Robinson','O',1.75,4.64,1.61,2.71,0.75,1.02,4.19)

jags_offense = offense_details('Jacksonville Jaguars','teal','black',minshew,chark,westbrook,eifert,robinson)

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
    
off_list = [browns_offense,jags_offense]
def_list = [niners_defense]

def teams_list(side,teams_list):
    
    text = f'{side}s available:'
    
    for i in range(0,len(teams_list)):
        name = teams_list[i]['name']
        
        chunk = f"""
- {name}"""
        
        text = text + chunk
    
    print(text)
    
teams_list('Offense',off_list)
teams_list('Defense',def_list)
