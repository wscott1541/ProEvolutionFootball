#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 18:58:32 2020

@author: WS
"""

#go through teams
#go through roster
#go through player
#write to pandas

import time

import urllib.request
from bs4 import BeautifulSoup

import pandas as pd

teams = [#'Arizona Cardinals',
#'Atlanta Falcons',
#'Baltimore Ravens',
#'Buffalo Bills',
#'Carolina Panthers',
#'Chicago Bears',
#'Cincinnati Bengals',
#'Cleveland Browns',
#'Dallas Cowboys',
#'Denver Broncos',
#'Detroit Lions',
#'Green Bay Packers',
#'Houston Texans',
#'Indianapolis Colts',
#'Jacksonville Jaguars',
#'Kansas City Chiefs',
#'Los Angeles Chargers',
#'Los Angeles Rams',
#'Miami Dolphins',
#'Minnesota Vikings',
#'New England Patriots',
#'New Orleans Saints',
#'New York Giants',
#'New York Jets',
#'Las Vegas Raiders',#21:39
#'Philadelphia Eagles',
#'Pittsburgh Steelers',
#'San Francisco 49ers',#21:44
'Seattle Seahawks',
'Tampa Bay Buccaneers',
'Tennessee Titans',#21:52
'Washington Football Team']

def gen_team_wiki(team):
    
    name = team.replace(' ','_')
    
    wiki = f'https://en.wikipedia.org/wiki/{name}'
    
    return(wiki)
    

"""
def roster_details(WIKI_URL):
    page = urllib.request.urlopen(WIKI_URL)

    soup = BeautifulSoup(page, "lxml")
    
    ros = {'class':'toccolours'}
    roster = str(soup.find_all('table',ros))
    
    #print(len(roster))
    
    ros_sta = roster.find('Quarterbacks')
    ros_end = roster.find('Special teams')
    
    roster = roster[ros_sta-4:ros_end]
    
    for i in range(0,len(roster)):
        if roster[i-3:i] == '<b>':
            sta = i
            end = roster[sta:].find('</b>')
            position = roster[i:sta+end]
            print(position)
            
        if roster[i-3:i] == '<a ':
            sta = i
            end = roster[sta:].find('</a>')
            section = roster[i:sta+end]
            #print(section)
            wiki_sta = section.find('wiki/')
            wiki_end = section[wiki_sta:].find('"')
            wiki = section[wiki_sta+5:wiki_sta+wiki_end]
            
            name_sta = section.find('>')
            name = section[name_sta+1:]
            
            print(name)        
"""    
    #print(name_full)
    
    #name_sta = name_full.find('href="#Current_roster"')
    #name_end = name_full.rfind('href="#Pro_Football_Hall_of_Famers"')
    
    #roster = name_full[name_sta:name_end]
    
    #print(roster)


def player_details(WIKI_URL):
    
    player = {'height':'NOT FOUND',
              'weight': 'NOT FOUND',
              'arm':'NOT FOUND',
              'hand': 'NOT FOUND',
              '40':'NOT FOUND',
              'split_a': 'NOT FOUND',
              'split_b': 'NOT FOUND',
              'shuttle': 'NOT FOUND',
              'cone': 'NOT FOUND',
              'vert': 'NOT FOUND',
              'broad': 'NOT FOUND',
              'bench': 'NOT FOUND',
              'wonderlic': 'NOT FOUND'}

    #WIKI_URL = 'https://en.wikipedia.org/wiki/Aaron_Donald'
    #'https://en.wikipedia.org/wiki/Jalen_Ramsey'
    #'https://en.wikipedia.org/wiki/Saquon_Barkley'
    #'https://en.wikipedia.org/wiki/Richard_Sherman_(American_football)'
    #"https://en.wikipedia.org/wiki/Gardner_Minshew"
    #"https://en.wikipedia.org/wiki/D._J._Chark"

    page = urllib.request.urlopen(WIKI_URL)

    soup = BeautifulSoup(page, "lxml")

    #name_full = str(soup.find_all('h1'))

    #name_sta = name_full.find('>')
    #name_end = name_full.rfind('<')

    #name = name_full[name_sta+1:name_end]

    #if ' (' in name:
    #    bracket_pos = name.find(' (')
    #    name = name[:bracket_pos]

    #player['name'] = name

    #table_classes = {"class": ["sortable", "plainrowheaders"]}
    wikitables = soup.findAll("table")

    string = str(wikitables)

    sta_pos = string.find('Pre-draft measurables')

    string = string[sta_pos:]

    fin_pos = string.find('</table>')
    #print(fin_pos)
    string = string[:fin_pos]
    
    #print(string)
    
    tr_find = string.find('</tr>')
    top_row_string = string[:tr_find]
    #th
    headers = []
    
    #print(top_row_string)
    
    string = string[tr_find+4:]
    
    tr_find = string.find('</tr>')
    mid_row_string = string[:tr_find]
    vals = []
    #td
    
    #print(mid_row_string)
    
    for i in range(0,len(top_row_string)-4):
        if top_row_string[i:i+3] == '<th':
            temp = top_row_string[i:]
            end = temp.find('</th>')
            section = temp[:end]
            headers.append(section)
            
    for i in range(0,len(mid_row_string)-4):
        if mid_row_string[i:i+4] == '<td>':
            temp = mid_row_string[i:]
            end = temp.find('</td>')
            section = temp[:end]
            vals.append(section)
    
    #print(headers)
    #print(headers[4])
    #print(vals[4])
    
    for i in range(0,len(headers)):
        if 'Height' in headers[i]:
            try:
                section = vals[i]
                pos = section.find('in<br/>(')
                val = float(section[pos+8:pos+12])
            except:
                val = 'NOT FOUND'
            player['height'] = val
            
        if 'Weight' in headers[i]:
            try:
                section = vals[i]
                sta_pos = section.find('lb<br/>(')
                end_pos = section.find(' kg')
                val = float(section[sta_pos+8:end_pos-4])
            except:
                val = 'NOT FOUND'
            player['weight'] = val
            
        if 'Arm' in headers[i]:
            try:
                section = vals[i]
                pos = section.find('in<br/>(')
                val = float(section[pos+8:pos+12])
            except:
                val = 'NOT FOUND'
            player['arm'] = val
            
        if 'Hand' in headers[i]:
            try:
                section = vals[i]
                pos = section.find('in<br/>(')
                val = float(section[pos+8:pos+12])
            except:
                val = 'NOT FOUND'
            player['hand'] = val
            
        if '40-yard' in headers[i]:
            try:
                section = vals[i]
                point = section.find(' s</')
                val = float(section[point-4:point])
            except:
                val = 'NOT FOUND'
            player['40'] = val
            
        if '10-yard' in headers[i]:
            try:
                section = vals[i]
                point = section.find(' s</')
                val = float(section[point-4:point])
            except:
                val = 'NOT FOUND'
            player['split_a'] = val
            
        if '20-yard split' in headers[i]:
            try:
                section = vals[i]
                point = section.find(' s</')
                val = float(section[point-4:point])
            except:
                val = 'NOT FOUND'
            player['split_b'] = val
            
        if 'shuttle' in headers[i]:
            try:
                section = vals[i]
                point = section.find(' s</')
                val = float(section[point-4:point])
            except:
                val = 'NOT FOUND'
            player['shuttle'] = val
            
        if 'cone' in headers[i]:
            try:
                section = vals[i]
                point = section.find(' s</')
                val = float(section[point-4:point])
            except:
                val = 'NOT FOUND'
            player['cone'] = val
            
        if 'Broad' in headers[i]:
            try:
                section = vals[i]
                pos = section.find('in<br/>(')
                val = float(section[pos+8:pos+12])
            except:
                val = 'NOT FOUND'
            player['broad'] = val
            
        if 'Vert' in headers[i]:
            try:
                section = vals[i]
                pos = section.find('in<br/>(')
                val = float(section[pos+8:pos+12])
            except:
                val = 'NOT FOUND'
            player['vert'] = val
            
        if 'Bench' in headers[i]:
            try:
                section = vals[i]
                pos = section.find(' reps')
                val = float(section[pos-2:pos])
            except:
                val = 'NOT FOUND'
            player['bench'] = val
            
        if 'Wonderlic' in headers[i]:
            try:
                section = vals[i]
                pos = section.find('</span')
                val = float(section[pos-2:pos])
            except:
                val = 'NOT FOUND'
            player['wonderlic'] = val
            
    return(player)
    
def roster_details(team):
    
    cols = ['Team','Name','Position','Height','Weight','Hand','Arm','40-yard','10-yard','20-yard split','shuttle','cone','Broad','Vert','Bench','Wonderlic']

    try:
        data = pd.read_csv (r'rosters2020-09-30.csv')
        df = pd.DataFrame(data,columns=cols)
    except:
        df = pd.DataFrame(columns=cols)
    
    
    WIKI_URL = gen_team_wiki(team)
    
    page = urllib.request.urlopen(WIKI_URL)

    soup = BeautifulSoup(page, "lxml")
    
    time.sleep(1)    
    
    ros = {'class':'toccolours'}
    roster = str(soup.find_all('table',ros))
    
    #print(roster)
    
    ros_sta = roster.find('Quarterbacks')
    ros_end = roster.find('Rookies in italics')
    
    roster = roster[ros_sta-4:ros_end]
    
    #print(roster)
    
    positions = ['Staff']
    
    for i in range(0,len(roster)):
        if roster[i-3:i] == '<b>':
            sta = i
            end = roster[sta:].find('</b>')
            position = roster[i:sta+end]
            positions.append(position)
            
        if roster[i-3:i] == '<a ':
            sta = i
            end = roster[sta:].find('</a>')
            section = roster[i:sta+end]
            #print(section)
            wiki_sta = section.find('wiki/')
            wiki_end = section[wiki_sta:].find('"')
            wiki = section[wiki_sta+5:wiki_sta+wiki_end]
            if 'page does not exist' in wiki:
                wiki = 'NONE'
            
            #pos_section = roster[sta+end:]
            #pos_end = pos_section.find('</li')
            #pos_section = pos_section[:pos_end]
            
            
            name_sta = section.find('>')
            name = section[name_sta+1:]
            
            if positions[-1] == 'Staff':
                pos = 'Staff'
            elif positions[-1] == 'Quarterbacks':
                pos = 'QB'
            elif positions[-1] == 'Running backs':
                pos = 'RB'
            elif positions[-1] == 'Wide receivers':
                pos = 'WR'
            elif positions[-1] == 'Tight ends':
                pos = 'TE'
            else:
                pos_section = roster[sta+end:]
                pos_end = pos_section.find('</li')
                pos_section = pos_section[:pos_end]
                
                if '<small>' in pos_section:
                    #print(name,'yep')
                    #print(name,pos_section)
                    pos_sta = pos_section.find('</a> ') + 5
                    pos_end = pos_section.find(' <sma')
                    pos = pos_section[pos_sta:pos_end]
                    if '</i>' in pos:
                        pos_sta = pos.find('</i> ') + 5
                        pos = pos[pos_sta:]
                else:
                    
                    #pos_end = pos_section.find('</li')
                
                    #pos_section = pos_section[:pos_end]
                    pos_sta = pos_section.rfind('>') + 2
                    pos = pos_section[pos_sta:pos_end]
                    
                
                #pos_temp = sta+end+5
                #pos_end = roster[pos_temp:].find('<')
                #pos_sta = roster[:pos_end].rfind('>')
                #pos = roster[pos_sta:pos_temp+pos_end]
            
            #print(name,wiki)
            
            
            if name[0] != '<':
                
                if pos == 'Staff':
                    print(f'{name} is on staff')
                elif name == "Cre'Von LeBlanc":
                    print(f'{name} skipped')
                    details = [team,name,pos,'FAILED','FAILED','FAILED','FAILED','FAILED','FAILED','FAILED','FAILED','FAILED','FAILED','FAILED','FAILED','FAILED']    
                    row = pd.Series(details,index=df.columns)
                    mod = df.append(row,ignore_index = True)
                    df = mod
                    df.to_csv(r'rosters2020-09-30.csv',index = False)
                elif wiki == 'NONE':
                    print(f'{name} does not have wikipedia')
                    details = [team,name,pos,'NW','NW','NW','NW','NW','NW','NW','NW','NW','NW','NW','NW','NW']    
                    row = pd.Series(details,index=df.columns)
                    mod = df.append(row,ignore_index = True)
                    df = mod
                    df.to_csv(r'rosters2020-09-30.csv',index = False)
                else:
                    #print(name,wiki)
                    url = f'https://en.wikipedia.org/wiki/{wiki}'
                    try:
                        p_vals = player_details(url)
                        
                        details = [team,name,pos,p_vals['height'],p_vals['weight'],p_vals['hand'],p_vals['arm'],p_vals['40'],p_vals['split_a'],p_vals['split_b'],p_vals['shuttle'],p_vals['cone'],p_vals['broad'],p_vals['vert'],p_vals['bench'],p_vals['wonderlic']]
                        row = pd.Series(details,index=df.columns)
                        mod = df.append(row,ignore_index = True)
                        df = mod
                        df.to_csv(r'rosters2020-09-30.csv',index = False)
                        print(f'{name} loaded')
                        time.sleep(1.25)
                    except:
                        print(f'{name} failed')
                        details = [team,name,pos,'FAILED','FAILED','FAILED','FAILED','FAILED','FAILED','FAILED','FAILED','FAILED','FAILED','FAILED','FAILED','FAILED']    
                        row = pd.Series(details,index=df.columns)
                        mod = df.append(row,ignore_index = True)
                        df = mod
                        df.to_csv(r'rosters2020-09-30.csv',index = False)
            
                    
    
    
#player_details('https://en.wikipedia.org/wiki/Ryan_Fitzpatrick')
#for i in range(0,len(teams)):
#    print(teams[i])                
#    cont = input('Continue? ')
#    if cont == 'Y':
#        roster_details(teams[i])

#print(teams[0])
#roster_details(teams[0])

#roster_details('Buffalo Bills')

#print(player_details('https://en.wikipedia.org/wiki/Cre%27Von_LeBlanc'))
 
downloads = ['rosters2020-09-29.csv','rosters2020-09-30.csv']

cols = ['Team','Name','Position','Height','Weight','Hand','Arm','40-yard','10-yard','20-yard split','shuttle','cone','Broad','Vert','Bench','Wonderlic']

data = pd.read_csv (r'rosters2020-09-29.csv')
df_one = pd.DataFrame(data,columns=cols)

data = pd.read_csv (r'rosters2020-09-30.csv')
df_two = pd.DataFrame(data,columns=cols)
    
frames = [df_one, df_two]

result = pd.concat(frames) 

result.to_csv(r'full_rosters.csv',index = False)                      