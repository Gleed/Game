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

def main():
    game.main()
    highscore.createlist()

if __name__ == '__main__':
    main()
