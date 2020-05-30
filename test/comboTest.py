#! /usr/bin/env python

import os
import pandas as pd
import CFBScrapy as cfb 

dfSeason = pd.read_csv('storage/season2018Clemson.csv')
dfSeason.set_index('id', inplace=True)

dfLines = pd.read_csv('storage/lines2018Clemson.csv')
dfLines.set_index('id', inplace=True)

dfCombo = dfSeason.append(dfLines[['spread','formattedSpread','overUnder']], sort=False)

print(dfCombo.head())

for col in dfLines.columns:
    print(col)

print('\nCombination:')
for col in dfCombo.columns:
    print(col)