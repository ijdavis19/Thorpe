#! /usr/bin/env python

import pandas as pd
import CFBScrapy as cfb 


def gameIDFinder():
    yearInput = input("Enter year of interest: ")
    yearInput = int(yearInput)

    if yearInput >= 2000 & yearInput < 2020:
        print(yearInput)
    else:
        print("Let's keep it between 2000 and 2019 for now.")
    
    team1 = input('Team One: ')

    dfTeam1Season = cfb.get_game_info(year=yearInput,team=team1)
    dfTeam1Season.set_index('week', inplace=True)

    print('Games played by {} in {}:'.format(yearInput,team1))
    print(dfTeam1Season[['away_team','home_team','id']])

    week = input('Input Game Week: ')
    intWeek = int(week)
    gameID = dfTeam1Season['id'].iloc[intWeek - 1]

    return gameID, yearInput, week, team1
    
#gameIDFinder()
