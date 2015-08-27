#-------------------------------------------------------------------------------
# Name:        game2.py
# Purpose:     Game against the computer, aim to get 30 points by choosing a
#              higher number than the computer does.
# Author:      Hannah
#
# Created:     25/08/2015
# Copyright:   (c) Hannah 2015
# Licence:     GNU GENERAL PUBLIC LICENSE Version 2, June 1991
#-------------------------------------------------------------------------------
import random
import os

global score

def start():
    os.system('color 0e')
    print("Welcome to the game. Your target is 30 points.")
    game()

def game():
    global score
    score=0
    x=0
    name=""
    while name=="":
        name=raw_input("What is your name?")
    usepnt=["Points:    "]
    usescr=["Score:     "]
    usenum=["Your guess:"]
    comnum=["Computer:  "]
    attempt=["Attempt:   ",'01','02','03','04','05','06','07','08','09','10']
    while x<10:
        x=x+1
        num=random.randint(1, 85)
        guess=""
        try:
            guess=int(raw_input("\nPick a number between 1 and 100."))
        except ValueError:
            print("\n Please enter a number or your guess will lose 5 points")
            try:
                guess=int(raw_input("\nPick a number between 1 and 100."))
            except ValueError:
                guess="00"

        if guess>num and guess<=10:
            fb="\nWell done, you get 10 points!\n"
            points=10
        elif guess>num and guess>10 and guess<=20:
            fb="\nWell done, you get 9 points.\n"
            points=9
        elif guess>num and guess>20 and guess<=30:
            fb="\nWell done, you get 8 points.\n"
            points=8
        elif guess>num and guess>30 and guess<=40:
            fb="\nWell done, you get 7 points.\n"
            points=7
        elif guess>num and guess>40 and guess<=50:
            fb="\nWell done, you get 6 points.\n"
            points=6
        elif guess>num and guess>50 and guess<=60:
            print("\nWell done, you get 5 points.\n")
            points=5
        elif guess>num and guess>60 and guess<=70:
            fb="\nWell done, you get 4 points\n"
            points=4
        elif guess>num and guess>70 and guess<=80:
            fb="\nWell done, you get 3 points\n"
            points=3
        elif guess>num and guess>80 and guess<=90:
            fb="\nWell done, you get 2 points\n"
            points=2
        elif guess>num and guess>90 and guess<=100:
            fb="\nWell done, you get 1 point\n"
            points=1
        elif guess==num:
            fb="\nExact match! You get 10 points!\n"
            points=10
        elif guess>100:
            fb="\nThat's cheating! -5 points\n"
            points=-5
        else:
            fb="\nThe computer beat you this time. Sorry, no points.\n"
            points=0
        score=int(score)+int(points)
        if len(str(score))>=2:
            pass
        else:
            score= "%02d" % (score)
        if len(str(points))>=2:
            pass
        else:
            points= "%02d" % (points)
##        print("score: "+str(score))
        usepnt.append(str(points))
##        print(usepnt)
        usescr.append(str(score))
##        print(usescr)
        os.system('cls')
#This one for use in linux
##      os.system('clear')
        print(attempt)
        if num>=10:
            pass
        else:
            num= "%02d" % (num)
        comnum.append(str(num))
        if guess>=10:
            pass
        else:
            guess= "%02d" % (guess)
        usenum.append(str(guess))
        print(comnum)
        print(usenum)
        print(usepnt)
        print(usescr)
        print(fb)
        score=str(score)
        if score[0]=='0':
            score=score[1]
            score=int(score)
        else:
            pass
        if score>='30':
            status="1"
        else:
            status="2"
        file=open("gnav.txt","w")
        file.write(status)
        file.close
        file=open("gamescore.txt", "w")
        file.write(name + ","+str(score))
        file.close()

if __name__ == '__main__':
    start()
