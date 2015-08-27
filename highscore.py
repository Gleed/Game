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
import os

global highscores
global leaderboard

def check():
    global leaderboard
    global highscores

    os.system('color 0a')

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
        leaderboard2=leaderboard2[:30]
    print "Leaderboard:"
    n=0
    for entry in leaderboard2:
        n=n+1
        print (str(n)+str(entry))
    print("\n\n\n(1) Play Game\n(2) Main Menu\n(3) Quit")
    choice=""
    while choice!="1" and choice !="2" and choice!="3":
        choice=raw_input("What do you want to do? 1,2 or 3")
    file=open("hnav.txt", "w")
    file.write(choice)
    file.close()

    file=open("gamescore.txt","w")
    file.write("name,0")
    file.close()
if __name__ == '__main__':
    createlist()