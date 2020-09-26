#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:09:00 2020

@author: WS
"""

import urllib.request
from bs4 import BeautifulSoup

import pandas as pd

def wiki_details(WIKI_URL):
    
    player = {'name': [],
              'height':[],
              'arm':[],
              '40':[],
              'split_a':[],
              'split_b':[],
              'shuttle':[],
              'vert':[]}

    #WIKI_URL = 'https://en.wikipedia.org/wiki/Aaron_Donald'
    #'https://en.wikipedia.org/wiki/Jalen_Ramsey'
    #'https://en.wikipedia.org/wiki/Saquon_Barkley'
    #'https://en.wikipedia.org/wiki/Richard_Sherman_(American_football)'
    #"https://en.wikipedia.org/wiki/Gardner_Minshew"
    #"https://en.wikipedia.org/wiki/D._J._Chark"

    page = urllib.request.urlopen(WIKI_URL)

    soup = BeautifulSoup(page, "lxml")

    name_full = str(soup.find_all('h1'))

    name_sta = name_full.find('>')
    name_end = name_full.rfind('<')

    name = name_full[name_sta+1:name_end]

    if ' (' in name:
        bracket_pos = name.find(' (')
        name = name[:bracket_pos]

    player['name'] = name

    #table_classes = {"class": ["sortable", "plainrowheaders"]}
    wikitables = soup.findAll("table")

    string = str(wikitables)

    sta_pos = string.find('Pre-draft measurables')

    string = string[sta_pos:]

    fin_pos = string.find('</table>')
    #print(fin_pos)
    string = string[:fin_pos]

    height_pos = string.find('in<br/>(')

    height = float(string[height_pos+8:height_pos+4+8])
    player['height'] = height

    string = string[height_pos+8:]

    arm_pos = string.find('in<br/>(')

    arm = float(string[arm_pos+8:arm_pos+4+8])
    player['arm'] = (arm)

    string = string[arm_pos+8:]

    hand_pos = string.find('in<br/>(')

    string = string[hand_pos+8:]

    temp_end_pos = string.find('</td>')

    string = string[temp_end_pos+5:]

    temp_end_pos = string.find('</tr>')

    string = string[:temp_end_pos]

    secs = []
    i_vals = []
    rows = []

    for i in range(0,len(string)):
        if string[i:i+4] == '<td>':
            temp = string[i:]
            end = temp.find('</td>')
            section = temp[:end]
            secs.append(section)
            i_vals.append(i)
        
            if ' s</span' in section:
                point = section.find(' s</')
                val = float(section[point-4:point])
            elif 'in<br/>' in section:
                point = section.find('in<br/>')
                val = float(section[point+8:point+12])
            else:
                val = 'NOT FOUND'
        
            rows.append(val)

    player['40'] = rows[0]
    player['split_a'] = rows[1]
    player['split_b'] = rows[2]
    player['shuttle'] = rows[3]
    player['vert'] = rows[5]

    print(player)
    
    strip = f"{player['name']},side,{player['height']},{player['40']},{player['split_a']},{player['split_b']},{player['arm']},{player['vert']},{player['shuttle']}"
    #side,height,forty,firstsplit,secondsplit,arm_length,vert_jump,shuttle
    print(strip)
    
#wiki_details('https://en.wikipedia.org/wiki/A._J._Green')
