#! /usr/bin/env python

import pandas as pd
import CFBScrapy as cfb 

from gameIDFinder import gameIDFinder

gameID, yearInput = gameIDFinder()
print("\nGame ID: {}".format(gameID))
print("\nYear: {}".format(yearInput))

dfGame = cfb.get_game_team_stats(year=yearInput,gameId=gameID)
