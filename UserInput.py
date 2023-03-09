import PlayerRanking
import TeamRankings
import GameSimulations

#deciding which part of program to utilize
print("Which of the following options do you want?")
print("")
print("1: A particular NBA player's statistics and grade for a given year")
print("2: A list, up to a number of your choosing, of NBA players ranked in the current year")
print("3: A list, up to a number of your choosing, of NBA teams ranked in the current year")
print("4: A percentage predictor of a game between two particular teams")
print("")

choice = input("Please select a number 1-4 (no spaces) for these options: ")

#making sure choice is a number 1-4
while True:
    try:
        int(choice)
        if int(choice) in (1,2,3,4):
            break
        else:
            choice = input("Please enter a number digit 1-4 (no spaces): ")
    except:
        choice = input("Please enter a number digit 1-4 (no spaces): ")

#making choice an int
choice = int(choice)


if (choice == 1):
    player = input("Please enter a players exact first and last name: ")




    