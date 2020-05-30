#! /usr/bin/env python

import pandas as pd
import CFBScrapy as cfb 

dfGame = cfb.get_game_team_stats(year=2018,gameId=401012787)

print(dfGame)