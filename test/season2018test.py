#! /usr/bin/env python

import os
import pandas as pd
import CFBScrapy as cfb 

dfSeason = cfb.get_game_info(year=2018,team='Clemson')
print(dfSeason.head())
for col in dfSeason.columns:
    print(dfSeason[col].describe())
dfSeason.to_csv('storage/season2018Clemson.csv')

dfLines = cfb.get_betting_lines(year=2018, team='Clemson')
print(dfLines.head())
for col in dfLines.columns:
    print(dfLines[col].describe())

dfLines.drop(dfLines[dfLines['provider'] != 'consensus'].index, inplace = True)
dfLines.to_csv('storage/lines2018Clemson.csv')

