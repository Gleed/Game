#-------------------------------------------------------------------------------
# Name:        win.py
# Purpose:
#
# Author:      Hannah
#
# Created:     25/08/2015
# Copyright:   (c) Hannah 2015
# Licence:     GNU GENERAL PUBLIC LICENSE Version 2, June 1991
#--------------------------------------------------------------------------
def win():
    file=open("gamescore.txt")
    data=file.read().split(",")
    file.close()
    score=data[1]
    print("Well Done, you win! Your score was: "+score+".")



