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

print("Editing PDF...")

outFileString = thisGame.singleGameFileName()

with open('output/singleGameSummary.tex', 'r') as file:
    inFile = file.readlines()



if os.path.isfile("{}.tex".format(outFileString)):
    os.remove("{}.tex".format(outFileString))

outFile = open("{}.tex".format(outFileString), 'w')

thisGame.writeToLatex(inFile=inFile, outFile=outFile, varlist=thisGame.pairs)


if os.path.isfile("{}.tex".format(outFileString)):
    print("File built successfully")

os.system("pdflatex {}.tex".format(outFileString))
os.system("pdflatex {}.tex".format(outFileString))
os.system("rm {}.out".format(outFileString))
os.system("rm {}.log".format(outFileString))
os.system("rm {}.aux".format(outFileString))
os.system("rm {}.toc".format(outFileString))
os.system("rm {}.tex".format(outFileString))
os.system("mv {}.pdf output/".format(outFileString))
os.system("xdg-open output/{}.pdf".format(outFileString))