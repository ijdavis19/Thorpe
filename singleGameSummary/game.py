#! /usr/bin/env python

import pandas as pd
import CFBScrapy as cfb
import io

class Game(object):

    def __init__(self, year, gameID, week, team):
        self.year = year
        self.gameID = gameID
        self.week = week
        self.gameInfo = cfb.get_game_info(year=self.year, week=self.week, team=team)
        self.awayTeam = self.gameInfo['away_team'].iloc[0]
        self.homeTeam = self.gameInfo['home_team'].iloc[0]
        self.venue = self.gameInfo['venue'].iloc[0]
        self.genStats = cfb.get_game_team_stats(year=self.year,gameId=self.gameID)
        self.bets = cfb.get_betting_lines(year=self.year, week=self.week, home=self.homeTeam)
        self.players = cfb.get_game_player_stats(year=self.year,gameId=self.gameID)
        self.homeCoach = cfb.get_coach_info(team=self.homeTeam, year=self.year)['first_name'].iloc[0] + " " + cfb.get_coach_info(team=self.homeTeam, year=self.year)['last_name'].iloc[0]
        self.awayCoach = cfb.get_coach_info(team=self.awayTeam, year=self.year)['first_name'].iloc[0] + " " + cfb.get_coach_info(team=self.awayTeam, year=self.year)['last_name'].iloc[0]

        self.pairs = [("YEAR",str(self.year)),
                      ("WEEK",str(self.week)),
                      ("HOMETEAM",self.homeTeam),
                      ("AWAYTEAM",self.awayTeam),
                      ("VENUE",self.venue)
                      ]

    # with open('output/singleGameSummary.tex', 'r') as file:
    #        inFile = file.readlines()

    # outFile = open('output/something.tex', 'w')
    def writeToLatex(self, inFile, outFile, varlist):
        for l in range(0,len(inFile)):
            inFileList = str(inFile[l]).split()
            for i in range(0,len(inFileList)):
                for variable, value in varlist:
                    if inFileList[i] == variable:
                        inFileList[i] = value
                    elif inFileList[i][:len(inFileList[i])-1] == variable:
                        inFileList[i] = value + inFileList[i][-1]
            outFileList = " ".join(inFileList)
            outFile.write(outFileList+"\r\n")
        outFile.close()
    
    def singleGameFileName(self):
        badfileString = "{} {} at {} {}".format(self.year, self.awayTeam, self.homeTeam, self.week)
        fileList = badfileString.split()
        outFileString = "".join(fileList)
        return outFileString


        

        

