#! /usr/bin/env python

import pandas as pd
import CFBScrapy as CFB
import game

print("start")
thisGame = game.Game(year=2019, gameID=401112456, week=4, team='Clemson')
print("succ")
