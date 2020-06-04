#! /usr/bin/env python

import pandas as pd
import CFBScrapy as cfb
import io
import os

TEAM1 = "Clemson"
TEAM2 = "Florida State"
VENUE = "Memorial Stadium"
WEEK = 5
YEAR = 2015

varlist = [("TEAM1",TEAM1),
           ("TEAM2",TEAM2),
           ("VENUE", VENUE),
           ("WEEK", str(WEEK)),
           ("YEAR", str(YEAR))
           ]

with open('output/singleGameSummary.tex', 'r') as file:
    inFile = file.readlines()


if os.path.isfile('output/docTest.tex'):
    os.remove('output/docTest.tex')

outFile = open('output/docTest.tex', 'w')


print(len(inFile))
print(inFile[96])
for l in range(0,len(inFile)):
    inFileList = str(inFile[l]).split()
    for i in range(0,len(inFileList)):
        for variable, value in varlist:
            if inFileList[i] == variable:
                inFileList[i] = value
            if inFileList[i][:len(inFileList[i])-1] == variable:
                inFileList[i] = value + inFileList[i][-1]
    outFileList = " ".join(inFileList)
    outFile.write(outFileList+"\r\n")
outFile.close()

with open('output/docTest.tex', 'r') as file:
    outFile = file.readlines()
print(len(outFile))
print(outFile[96])
