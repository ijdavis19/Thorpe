#! /usr/bin/env python

import pandas as pd
import CFBScrapy as cfb


def gameIDFinder():
    yearInput = int(input("Enter year of interest: "))

    team1 = input('Team One: ')

    dfTeam1Season = cfb.get_game_info(year=yearInput, team=team1)
    weeks = dfTeam1Season['week'].tolist()
    dfTeam1Season.set_index('week', inplace=True)

    print('Games played by {} in {}:'.format(team1, yearInput))
    print(dfTeam1Season[['away_team', 'home_team', 'id']])

    week = int(input('Input Game Week: '))
    if weeks[0] == 1:
        diff = 1
    if weeks[0] == 2:
        diff = 2
    if weeks[0] == 0:
        diff = 0
    for w in range(0, len(weeks)):
        if weeks[w] < week:
            if weeks[w+1] - weeks[w] > 1:
                diff = diff + 1
    indWeek = week - diff

    gameID = dfTeam1Season['id'].iloc[indWeek]

    return gameID, yearInput, week, team1


# gameIDFinder()
