#-------------------------------------------------------------------------------
# Name:        mainmenu.py
# Purpose:
#
# Author:      Hannah
#
# Created:     25/08/2015
# Copyright:   (c) Hannah 2015
# Licence:     GNU GENERAL PUBLIC LICENSE Version 2, June 1991
#-------------------------------------------------------------------------------
def menu():

    print('  ------,                   ------,        -------------         -------------      ')
    print(' /      |                  /      |       /  ,--------,  \      /  ,--------,  \    ')
    print('/       |                 /       |      /  /          \  \    /  /          \  \   ')
    print('|       |                 |       |     |   |           |  |  |   |           |  |  ')
    print("'---,   |                 '---,   |     |   |           |  |  |   |           |  |  ")
    print('    |   |  ,----------,       |   |     |   |           |  |  |   |           |  |  ')
    print('    |   |  |          |       |   |     |   |           |  |  |   |           |  |  ')
    print('    |   |  |          |       |   |     |   |           |  |  |   |           |  |  ')
    print("    |   |  '----------'       |   |     |   |           |  |  |   |           |  |  ")
    print('    |   |                     |   |     |   |           |  |  |   |           |  |  ')
    print('    |   |                     |   |     |   |           |  |  |   |           |  |  ')
    print('    |   |                     |   |     |   |           |  |  |   |           |  |  ')
    print(",---'   '----,            ,---'   '----,\   \          /   /  \   \          /   /  ")
    print("|            |            |            | \   '--------'   /    \   '--------'   /   ")
    print("'------------'            '------------'  '--------------'      '--------------'    ")
    print("How low dare you go?\n\n")
    print("Main Menu\n\n\n\n(1)  Play Game\n(2)  Rules\n(3)  Highscores\n(4)  Quit\n")
    option=""
    while option!="1" and option!="2" and option!="3"and option!="4":
        option=raw_input("What do you want to do? 1,2,3 or 4\n")
    file=open("menu.txt", "w")
    file.write(option)
    file.close()

if __name__ == '__main__':
    menu()


