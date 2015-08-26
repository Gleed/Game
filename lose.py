#-------------------------------"------------------------------------------------
# Name:        lose.py
# Purpose:
#
# Author:      Hannah
#
# Created:     25/08/2015
# Copyright:   (c) Hannah 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def lose():
  file=open("gamescore.txt")
  data=file.read().split(",")
  file.close()
  score=data[1]
  print("\n\n\nThe computer beat you this time. Your final score was: "+score+".\n\n\n")

