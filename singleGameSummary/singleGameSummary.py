#! /usr/bin/env python

import pandas as pd
import CFBScrapy as cfb 
import game
from gameIDFinder import gameIDFinder

# dfGame = cfb.get_game_info(year=2015,week=5,team='Clemson')
gameID, yearInput, week, team1 = gameIDFinder()
print("\nGame ID: {}".format(gameID))
print("\nYear: {}".format(yearInput))

thisGame = game.Game(year=yearInput, gameID=gameID, week=week, team=team1)

print("\n")
print("Home Team: {}".format(thisGame.homeTeam))
print("Home Coach: {}".format(thisGame.homeCoach))
print("Away Team: {}".format(thisGame.awayTeam))
print("Away Coach: {}".format(thisGame.awayCoach))
