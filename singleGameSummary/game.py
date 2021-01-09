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
        self.infoPairs = [("YEAR", str(self.year)),
                          ("WEEK", str(self.week)),
                          ("HOMETEAM", self.homeTeam),
                          ("AWAYTEAM", self.awayTeam),
                          ("WINNER", self.winner),
                          ("LOSER", self.loser),
                          ("WINNERSCORE", str(self.winnerScore)),
                          ("LOSERSCORE", str(self.loserScore)),
                          ("VENUE", self.venue)
                        ]
        self.genStats = get_game_team_stats(
            year=self.year, week=self.week, team=team)
        '''
        There is probably a way to loop over all of the rows
        and automate this process below
        '''
        self.genPairs = [("HOMETEAM", self.homeTeam),
                         ("AWAYTEAM", self.awayTeam),
                         ("HOMERUSHINGTDS", str(self.genStats['stat'].iloc[0])),
                         ("HOMEPUNTRETURNYARDS", str(self.genStats['stat'].iloc[1])),
                         ("HOMEPUNTRETURNTDS", str(self.genStats['stat'].iloc[2])),
                         ("HOMEPUNTRETURNS", str(self.genStats['stat'].iloc[3])),
                         ("HOMEPASSINGTDS", str(self.genStats['stat'].iloc[4])),
                         ("HOMEKICKRETURNYARDS", str(self.genStats['stat'].iloc[5])),
                         ("HOMEKICKRETURNTDS", str(self.genStats['stat'].iloc[6])),
                         ("HOMEKICKRETURNS", str(self.genStats['stat'].iloc[7])),
                         ("HOMEKICKINGPOINTS", str(self.genStats['stat'].iloc[8])),
                         ("HOMEINTERCEPTIONYARDS", str(self.genStats['stat'].iloc[9])),
                         ("HOMEINTERCEPTIONTDS", str(self.genStats['stat'].iloc[10])),
                         ("HOMEPASSESINTERCEPTED", str(self.genStats['stat'].iloc[11])),
                         ("HOMEFUMBLESRECOVERED", str(self.genStats['stat'].iloc[12])),
                         ("HOMETOTALFUMBLES", str(self.genStats['stat'].iloc[13])),
                         ("HOMETACKLESFORLOSS", str(self.genStats['stat'].iloc[14])),
                         ("HOMEDEFENSIVETDS", str(self.genStats['stat'].iloc[15])),
                         ("HOMETACKLES", str(self.genStats['stat'].iloc[16])),
                         ("HOMESACKS", str(self.genStats['stat'].iloc[17])),
                         ("HOMEQBHURRIES", str(self.genStats['stat'].iloc[18])),
                         ("HOMEPASSESDEFLECTED", str(self.genStats['stat'].iloc[19])),
                         ("HOMEFIRSTDOWNS", str(self.genStats['stat'].iloc[20])),
                         ("HOMETHIRDDOWNEFF", str(self.genStats['stat'].iloc[21])),
                         ("HOMEFOURTHDOWNEFF", str(self.genStats['stat'].iloc[22])),
                         ("HOMETOTALYARDS", str(self.genStats['stat'].iloc[23])),
                         ("HOMENETPASSINGYARDS", str(self.genStats['stat'].iloc[24])),
                         ("HOMECOMPLETIONATTEMPTS", str(self.genStats['stat'].iloc[25])), # Split
                         ("HOMEYARDSPERPASS", str(self.genStats['stat'].iloc[26])),
                         ("HOMERUSHINGYARDS", str(self.genStats['stat'].iloc[27])),
                         ("HOMERUSHINGATTEMPTS", str(self.genStats['stat'].iloc[28])),
                         ("HOMEYARDSPERRUSHATTEMPT", str(self.genStats['stat'].iloc[29])),
                         ("HOMETOTALPENALTIESYARDS", str(self.genStats['stat'].iloc[30])), # Split
                         ("HOMETURNOVERS", str(self.genStats['stat'].iloc[31])),
                         ("HOMEFUMBLESLOST", str(self.genStats['stat'].iloc[32])),
                         ("HOMEINTERCEPTIONS", str(self.genStats['stat'].iloc[33])),
                         ("HOMEPOSESSIONTIME", str(self.genStats['stat'].iloc[34])),
                         ("AWAYRUSHINGTDS", self.genStats['stat'].iloc[35]),
                         ("AWAYPASSINGTDS", str(self.genStats['stat'].iloc[36])),
                         ("AWAYKICKRETURNYARDS", str(self.genStats['stat'].iloc[37])),
                         ("AWAYKICKRETURNTDS", str(self.genStats['stat'].iloc[38])),
                         ("AWAYKICKRETURNS", str(self.genStats['stat'].iloc[39])),
                         ("AWAYKICKINGPOINTS", str(self.genStats['stat'].iloc[40])),
                         ("AWAYINTERCEPTIONYARDS", str(self.genStats['stat'].iloc[41])),
                         ("AWAYINTERCEPTIONTDS", str(self.genStats['stat'].iloc[42])),
                         ("AWAYPASSESINTERCEPTED", str(self.genStats['stat'].iloc[43])),
                         ("AWAYFUMBLESRECOVERED", str(self.genStats['stat'].iloc[44])),
                         ("AWAYTOTALFUMBLES", str(self.genStats['stat'].iloc[45])),
                         ("AWAYTACKLESFORLOSS", str(self.genStats['stat'].iloc[46])),
                         ("AWAYDEFENSIVETDS", str(self.genStats['stat'].iloc[47])),
                         ("AWAYTACKLES", str(self.genStats['stat'].iloc[48])),
                         ("AWAYSACKS", str(self.genStats['stat'].iloc[49])),
                         ("AWAYQBHURRIES", str(self.genStats['stat'].iloc[50])),
                         ("AWAYPASSESDEFLECTED", str(self.genStats['stat'].iloc[51])),
                         ("AWAYFIRSTDOWNS", str(self.genStats['stat'].iloc[52])),
                         ("AWAYTHIRDDOWNEFF", str(self.genStats['stat'].iloc[53])),
                         ("AWAYFOURTHDOWNEFF", str(self.genStats['stat'].iloc[54])),
                         ("AWAYTOTALYARDS", str(self.genStats['stat'].iloc[55])),
                         ("AWAYNETPASSINGYARDS", str(self.genStats['stat'].iloc[56])),
                         ("AWAYCOMPLETIONATTEMPTS", str(self.genStats['stat'].iloc[57])), # Split
                         ("AWAYYARDSPERPASS", str(self.genStats['stat'].iloc[58])),
                         ("AWAYRUSHINGYARDS", str(self.genStats['stat'].iloc[59])),
                         ("AWAYRUSHINGATTEMPTS", str(self.genStats['stat'].iloc[60])),
                         ("AWAYYARDSPERUSHATTEMPT", str(self.genStats['stat'].iloc[61])),
                         ("AWAYTOTALPENALTIESYARSD", str(self.genStats['stat'].iloc[62])), # Split
                         ("AWAYTURNOVERS", str(self.genStats['stat'].iloc[63])),
                         ("AWAYFUMBLESLOST", str(self.genStats['stat'].iloc[64])),
                         ("AWAYINTERCEPTIONS", str(self.genStats['stat'].iloc[65])),
                         ("AWAYPOSESSIONTIME", str(self.genStats['stat'].iloc[66])),
                        ]
        self.homeRushingTDs = self.genStats['stat'].iloc[0]
        self.homePuntReturnYards = self.genStats['stat'].iloc[1]
        self.homePuntReturnTDs = self.genStats['stat'].iloc[2]
        self.homePuntReturns = self.genStats['stat'].iloc[3]
        self.homePunt = self.genStats['stat'].iloc[4]
        self.homePuntReturns = self.genStats['stat'].iloc[3]
        self.bets = get_betting_lines(
            year=self.year, week=self.week, home=self.homeTeam)
        self.players = get_game_player_stats(
            year=self.year, gameId=self.gameID)

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
                    elif inFileList[i][:len(inFileList[i])-2] == variable:
                        inFileList[i] = value + inFileList[i][-2] + inFileList[i][-1]
            outFileList = " ".join(inFileList)
            outFile.write(outFileList+"\r\n")
        outFile.close()

    def singleGameFileName(self):
        badfileString = "{} {} at {} {}".format(
            self.year, self.awayTeam, self.homeTeam, self.week)
        fileList = badfileString.split()
        outFileString = "".join(fileList)
        return outFileString
