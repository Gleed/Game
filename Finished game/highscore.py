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
    leaderboard.append(gamescore)
    name=gamescore[0]
    number=gamescore[1]
    if len(highscores)==0:
        file=open("scores.txt", "a")
        file.write(name+","+number)
        file.close()
    else:
        file=open("scores.txt", "a")
        file.write(","+name+","+number)
    listscores()

def createlist():
    global highscores
    global leaderboard

    file=open("scores.txt", "r")
    scores=file.read().split(",")
    i=0
    highscores=[]
    while i <len(scores):
        a=scores[i]
        b=scores[i+1]
        toadd=[a,b]
        highscores.append(toadd)
        i=i+2
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
        n=int(n)+1
        if n>=10:
            pass
        else:
            n= "%02d" % (n)
        print("------------------")
        name=str(entry[0])
        if int(len(entry[0]))>10:
##            print(name)
            name=name[:7]
            print("|"+str(n)+"|"+str(name)+"...|"+str(entry[1])+"|")
        elif int(len(name))==10:
            print("|"+str(n)+"|"+str(name)+"|"+str(entry[1]+"|"))
        elif int(len(name))==9:
            print("|"+str(n)+"|"+str(name)+" |"+str(entry[1]+"|"))
        elif int(len(name))==8:
            print("|"+str(n)+"|"+str(name)+"  |"+str(entry[1]+"|"))
        elif int(len(name))==7:
            print("|"+str(n)+"|"+str(name)+"   |"+str(entry[1]+"|"))
        elif int(len(name))==6:
            print("|"+str(n)+"|"+str(name)+"    |"+str(entry[1]+"|"))
        elif int(len(name))==5:
            print("|"+str(n)+"|"+str(name)+"     |"+str(entry[1]+"|"))
        elif int(len(name))==4:
            print("|"+str(n)+"|"+str(name)+"      |"+str(entry[1]+"|"))
        elif int(len(name))==3:
            print("|"+str(n)+"|"+str(name)+"       |"+str(entry[1]+"|"))
        elif int(len(name))==2:
            print("|"+str(n)+"|"+str(name)+"        |"+str(entry[1]+"|"))
        elif int(len(name))==1:
            print("|"+str(n)+"|"+str(name)+"         |"+str(entry[1]+"|"))
    print("------------------")
    print("\n(1) Play Game\n(2) Main Menu")
    choice=""
    while choice!="1" and choice !="2":
        choice=raw_input("What do you want to do? 1 or 2\n")
    file=open("hnav.txt", "w")
    file.write(choice)
    file.close()

    file=open("gamescore.txt","w")
    file.write(",")
    file.close()

if __name__ == '__main__':
    createlist()