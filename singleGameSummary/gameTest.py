#! /usr/bin/env python

import pandas as pd
import CFBScrapy as cfb
import game


thisGame = game.Game(year=2018, gameID=401013169, week=10, team='Clemson')

print("Game Retrieved")
