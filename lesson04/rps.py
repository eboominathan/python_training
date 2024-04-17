import sys
print("")
playerchoice = input(
    "Enter ... \n1. for Rock \n2. for Paper or \n3.for Scissors:\n\n")
player = int(playerchoice)
if player < 1 | player > 3:
    sys.exit("you must enter between 1 to 3")
