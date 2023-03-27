def inputNum():
    #deciding which part of program to utilize
    print("Which of the following options do you want?")
    print("")
    print("1: A particular NBA player's statistics and grade for a given year")
    print("2: A percentage predictor of a game between two particular teams")
    print("3: A list, up to a number of your choosing, of active NBA players currently on a team ranked in the current year")
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
    return choice

def inputChoice(choice):

    if (choice == 1):
        return input("Please enter a players exact first and last name: ")
    if choice == 5:
        return input("Please enter wanted season. Follow exact syntax: ####-####   (ex: 2022-2023): ")


def teamOne():
    return input("Please enter 3 letter abbreviation for team 1 (Home team): ")

def teamTwo():
    return input("Please enter 3 letter abbreviation for team 2 (Away Team): ")



    