#-------------------------------------------------------------------------------
# Name:        highscore.py
# Purpose:     To display the top ten highscores.
#
# Author:      Hannah
#
# Created:     25/08/2015
# Copyright:   (c) Hannah 2015
# Licence:     GNU  GENERAL PUBLIC LICENSE Version 2, June 1991
#-------------------------------------------------------------------------------
from operator import itemgetter

global highscores
global leaderboard

def check():
    global leaderboard
    global highscores

    gamescore=[]
    file=open("gamescore.txt", "r+")
    gamescore=file.read().split(",")
    file.close()
##    print (gamescore)
# I want to compare gamescore[1] with the other scores in leaderboard.and return for each one whether it is higher or lower.
# If one returns higher then I want to loop to stop and the score to be added into the place it stopped.
    i=0
    tf=False
    while tf==False and i<len(leaderboard):
        if leaderboard [i][1]>gamescore[1]:
            tf=False
        else:
            tf=True
        if tf==True:
            leaderboard.append(gamescore)
            name=gamescore[0]
##            print (name)
            number=gamescore[1]
##            print(number)
            if len(highscores)==0:
                file=open("scores.txt", "a")
                file.write(name+","+number)
                file.close()
            else:
                file=open("scores.txt", "a")
                file.write(","+name+","+number)
        i=i+1
    listscores()

def createlist():
    global highscores
    global leaderboard

    file=open("scores.txt", "r")
    scores=file.read().split(",")
##    print(scores)
    i=0
    highscores=[]
    while i <len(scores):
        a=scores[i]
##        print a
        b=scores[i+1]
##        print b
        toadd=[a,b]
##        print toadd
        highscores.append(toadd)
##        print highscores
        i=i+2
##    print(highscores)
    leaderboard=sorted(highscores, key=itemgetter(1), reverse=True)
    check()

def listscores():
    global leaderboard

    leaderboard2=sorted(leaderboard, key=itemgetter(1), reverse=True)
    if len(leaderboard2)>10:
        leaderboard2=leaderboard2[:10]
    print "Leaderboard:"
    for entry in leaderboard2:
        print entry

if __name__ == '__main__':
    createlist()