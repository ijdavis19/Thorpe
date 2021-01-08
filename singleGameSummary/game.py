#! /usr/bin/env python

import pandas as pd
import requests
import json
from pandas.io.json import json_normalize
import sys
sys.path.insert(1, '/home/ian/sources/CFBScrapy/CFBScrapy/')
from cfbtools import *
import io


# 401237492


class Game(object):

    def __init__(self, year, gameID, week, team):
        self.year = year
        self.gameID = gameID
        self.week = week
        self.gameInfo = get_game_info(
            year=self.year, week=self.week, team=team)
        self.awayTeam = self.gameInfo['away_team'].iloc[0]
        self.awayScore = self.gameInfo['away_points'][0]
        self.homeTeam = self.gameInfo['home_team'].iloc[0]
        self.homeScore = self.gameInfo['home_points'][0]
        self.venue = self.gameInfo['venue'].iloc[0]
        self.genStats = get_game_team_stats(
            year=self.year, week=self.week, team=team)
        self.bets = get_betting_lines(
            year=self.year, week=self.week, home=self.homeTeam)
        self.players = get_game_player_stats(
            year=self.year, gameId=self.gameID)
        if self.homeScore > self.awayScore:
            self.winner = self.homeTeam
            self.loser = self.awayTeam
            self.winnerScore = self.homeScore
            self.loserScore = self.awayScore

        else:
            self.winner = self.awayTeam
            self.loser = self.homeTeam
            self.winnerScore = self.awayScore
            self.loserScore = self.homeScore

        self.pairs = [("YEAR", str(self.year)),
                      ("WEEK", str(self.week)),
                      ("HOMETEAM", self.homeTeam),
                      ("AWAYTEAM", self.awayTeam),
                      ("WINNER", self.winner),
                      ("LOSER", self.loser),
                      ("WINNERSCORE", str(self.winnerScore)),
                      ("LOSERSCORE", str(self.loserScore)),
                      ("VENUE", self.venue)
                      ]

    # with open('output/singleGameSummary.tex', 'r') as file:
    #        inFile = file.readlines()

    # outFile = open('output/something.tex', 'w')
    def writeToLatex(self, inFile, outFile, varlist):
        for l in range(0, len(inFile)):
            inFileList = str(inFile[l]).split()
            for i in range(0, len(inFileList)):
                for variable, value in varlist:
                    if inFileList[i] == variable:
                        inFileList[i] = value
                    elif inFileList[i][:len(inFileList[i])-1] == variable:
                        inFileList[i] = value + inFileList[i][-1]
            outFileList = " ".join(inFileList)
            outFile.write(outFileList+"\r\n")
        outFile.close()

    def singleGameFileName(self):
        badfileString = "{} {} at {} {}".format(
            self.year, self.awayTeam, self.homeTeam, self.week)
        fileList = badfileString.split()
        outFileString = "".join(fileList)
        return outFileString

    def gameTest(self):
        test = game.Game(year=2018, gameID=401013169, week=10, team='Clemson')
        print("\n\nGame test successfully retrieved")
        #print("\n{} vs. {}".format(sef))
