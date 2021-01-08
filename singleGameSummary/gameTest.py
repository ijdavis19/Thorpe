#! /usr/bin/env python

import pandas as pd
import requests
import json
from pandas.io.json import json_normalize
import sys
sys.path.insert(1, '/home/ian/sources/CFBScrapy/CFBScrapy/')
from cfbtools import *
import game

def gameTest():
        test = game.Game(year=2018, gameID=401013169, week=10, team='Clemson')
        print("\n\nGame test successfully retrieved")
        print("\n{} vs. {}".format(test.homeTeam, test.awayTeam))
        print("\n{}".format(test.year))
        print("\n{}".format(test.week))
        return test

'''
import game
from gameTest import *
x = gameTest()
print(x.gameInfo.head())
print(x.gameInfo.columns)
'''
