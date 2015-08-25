#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Hannah
#
# Created:     25/08/2015
# Copyright:   (c) Hannah 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random

def main():
    print("Welcome to the game. Your aim is to get 30 points by picking a higher number than the computer.\n However the higher number you pick, the fewer points you get if you win.")
    ready=raw_input("Are you ready? Y/N")
    if ready=="Y" or ready =="y":
        print ("Let's play!")
        game()
    else:
        print ("Goodbye!")
        exit()

def game():
    x=0
    score=0
    while x<10:
        x=x+1
        num=random.randint(1, 100)
        guess=int(raw_input("Pick a number between 1 and 100."))

##        while type(guess)==str:
##            guess=raw_input("Pick a number between 1 and 100.\nPlease do not enter letters.")
##        int(guess)
##        print(type(guess))
        if guess>num and guess<=10:
            print ("Well done, you get 10 points!")
            points=10
        elif guess>num and guess>10 and guess<=20:
            print ("Well done, you get 9 points.")
            points=9
        elif guess>num and guess>20 and guess<=30:
            print ("Well done, you get 8 points.")
            points=8
        elif guess>num and guess>30 and guess<=40:
            print ("Well done, you get 7 points.")
            points=7
        elif guess>num and guess>40 and guess<=50:
            print ("Well done, you get 6 points.")
            points=6
        elif guess>num and guess>50 and guess<=60:
            print("Well done, you get 5 points.")
            points=5
        elif guess>num and guess>60 and guess<=70:
            print("Well done, you get 4 points")
            points=4
        elif guess>num and guess>70 and guess<=80:
            print("Well done, you get 3 points")
            points=3
        elif guess>num and guess>80 and guess<=90:
            print("Well done, you get 2 points")
            points=2
        elif guess>num and guess>90 and guess<=100:
            print("Well done, you get 1 point")
            points=1
        elif guess==num:
            print("Exact match! You get 10 bonus points!")
            points=10
        elif guess>100:
            print("That's cheating! -10 points")
            points=-10
        else:
            print("The computer beat you this time. Sorry, no points.")
            points=0
        score=score+points
        print(score)
    if score>=30:
        print ("You Win! Your final score was: "+str(score))
    else:
        print("The computer beat you this time, you lose. Your final score was: "+str(score))
if __name__ == '__main__':
    main()
