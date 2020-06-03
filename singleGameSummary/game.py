#! /usr/bin/env python

import pandas as pd
import CFBScrapy as cfb

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
        self.succ = "yar"
