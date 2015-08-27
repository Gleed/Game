#-------------------------------------------------------------------------------
# Name:        central.py
# Purpose:     To run the game and bring the files together.
#
# Author:      Hannah
#
# Created:     26/08/2015
# Copyright:   (c) Hannah 2015
# Licence:     GNU  GENERAL PUBLIC LICENSE Version 2, June 1991
#-------------------------------------------------------------------------------
import game
import highscore
import mainmenu
import rules
import win
import lose
import os

def main():
    os.system('color 0b')
    mainmenu.menu()
    file=open("menu.txt","r")
    option=file.read()
    if option=="1":
        os.system('cls')
        play()
    elif option=="2":
        os.system('cls')
        rule()
    elif option=="3":
        os.system('cls')
        score()
    elif option=="4":
        os.system('cls')
        print("Goodbye!")
        exit()
    else:
        print("Please enter a number.")
        main()

def play():
    print("Going to the Game...\n\n")
    game.start()
    file=open("gnav.txt")
    nav=file.read()
    file.close()
    if nav=="1":
        os.system('cls')
        win.win()
        score()
    elif nav=="2":
        os.system('cls')
        lose.lose()
        main()
    else:
        os.system('cls')
        main()


def rule():
    print("Going to Rules...\n\n")
    os.system('cls')
    rules.rules()
    file=open("rnav.txt", "r")
    option=file.read()
    if option=="1":
        os.system('cls')
        play()
    elif option=="2":
        os.system('cls')
        main()
    elif option=="3":
        os.system('cls')
        bye()

def score():
    print ("Going to Highscores...\n")
    highscore.createlist()
    file=open("hnav.txt", "r")
    option=file.read()
    if option=="1":
        os.system('cls')
        play()
    elif option=="2":
        os.system('cls')
        main()
    elif option=="3":
        os.system('cls')
        bye()

def bye():
    exit()

if __name__ == '__main__':
    main()
