#-------------------------------------------------------------------------------
# Name:        rules.py
# Purpose:
#
# Author:      Hannah
#
# Created:     25/08/2015
# Copyright:   (c) Hannah 2015
# Licence:     GNU GENERAL PUBLIC LICENSE Version 2, June 1991
#-------------------------------------------------------------------------------
import os
def rules():
    os.system('color 0f')
    print("\n\n\nThe Rules:\n\nThe aim of this game is to pick a higher number than the computer. \nThe computer will pick a number between 1 and 100 and so will you.\nBeware though, the higher the number you pick, the fewer points you will get if you win.\nYour target is 30 points. If you reach this or higher, you win.\nIf your score is one of the top ten, it will be displayed on the leaderboard.\n\n(1)Play Game\n(2)Main Menu\n(3)Quit")
    choice=""
    while choice!="1" and choice!="2"and choice!="3":
        choice=raw_input("What do you want to do? 1,2 or 3")
    file=open("rnav.txt", "w")
    file.write(choice)
    file.close()

