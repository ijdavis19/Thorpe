#! /usr/bin/env python

import pandas as pd
import CFBScrapy as cfb 
import game
from gameIDFinder import gameIDFinder
import io
import os

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
print("\n")
print("Editing PDF...")

with open('output/singleGameSummary.tex', 'r') as file:
    inFile = file.readlines()



# NEED TO REDO STRINGS SO THE FIT COHERENT FILE FORMAT
if os.path.isfile('output/testSum.tex'):
    os.remove('output/testSum.tex')

outFile = open('output/testSum.tex', 'w')

thisGame.writeToLatex(inFile=inFile, outFile=outFile, varlist=thisGame.pairs)


if os.path.isfile('output/testSum.tex'):
    print("File built successfully")

os.system("pdflatex output/testSum.tex")
os.system("xdg-open testSum.pdf")