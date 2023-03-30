def inputNum():
    #deciding which part of program to utilize
    print("Which of the following options do you want?")
    print("")
    print("1: A particular NBA player's REGULAR/NORMAL grade, based on factors that predict winning, for a given year")
    print("2: A particular NBA player's per36 grade, based on factors that predict winning, for a given year")
    print("3: Both 1 and 2")
    print("")

    choice = input("Please select a number 1-3 (no spaces) for these options: ")

    #making sure choice is a number 1-3
    while True:
        try:
            int(choice)
            if int(choice) in (1,2,3):
                break
            else:
                choice = input("Please enter a number digit 1-3 (no spaces): ")
        except:
            choice = input("Please enter a number digit 1-3 (no spaces): ")

    #making choice an int
    choice = int(choice)
    return choice

def inputChoice(choice):

    if (choice == 1 or choice ==2 or choice ==3):
        return input("Please enter a players exact first and last name: ")
    if choice == 5:
        return input("Please enter wanted season. Follow exact syntax: ####-####   (ex: 2022-2023): ")




    