#-------------------------------------------------------------------------------
# Name:        central.py
# Purpose:     To run the game and bring the files together
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

def main():
    mainmenu.menu()
    file=open("mnav.txt","r")
    option=file.read()
    if option=="1":
        play()
    elif option=="2":
        rule()
    elif option=="3":
        score()
    elif option=="4":
        print("Goodbye!")
        exit()
    else:
        print("Please enter a number.")
        main()

def play():
    print("Play Game selected. Going to the Game...\n\n")
    game.start()
    file=open("gnav.txt")
    nav=file.read()
    file.close()
    if nav=="1":
        win.win()
        score()
    elif nav=="2":
        lose.lose()
        main()
    else:
        main()


def rule():
    print("Rules selected. Going to Rules...\n\n")
    rules.rules()
    file=open("rnav.txt", "r")
    option=file.read()
    if option=="1":
        play()
    elif option=="2":
        main()
    elif option=="3":
        bye()

def score():
    print ("Highscores selected. Going to Highscores...\n\n")
    highscore.createlist()
    file=open("hnav.txt", "r")
    option=file.read()
    if option=="1":
        play()
    elif option=="2":
        main()
    elif option=="3":
        bye()

def bye():
    print("Goodbye!")
    exit()

if __name__ == '__main__':
    main()
