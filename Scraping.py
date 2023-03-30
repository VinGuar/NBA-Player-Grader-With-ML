import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from unidecode import unidecode

#make sure do not go over rate limit of 20 requests per minute. If over puts in "jail" for an hour
rate = 0
def checkRate(r):
    global rate
    if r > 16:
        rate = 0
        time.sleep(61)

#scrapes URL for the player
def scrapeURL(player1, season1):

    global rate

    #remove punctuation for full name
    def nopunct(word):

        punctuations = '''!()-[];:'"\,<>./?@#$%^&*_~'''

        no_punct = ""
        for char in word:
            if char not in punctuations:
                no_punct = no_punct + char

        return no_punct

    player1 = nopunct(player1)
    player1 = unidecode(player1)
    player1 = player1.lower()


    #creating first and last name variables for player
    names = player1.split()
    firstName = names[0]
    lastName = names[1]


    url = "https://www.basketball-reference.com/players/"


    #insert the player name part of the url
    url += (lastName[0].lower() + "/")
    if len(lastName)>=5:
        for num in range(5):
            url += lastName[num].lower()
    else:
        url += lastName.lower()
    
    if len(firstName)>=2:
        for num in range (2):
            url += firstName[num].lower()
    else:
        url += firstName.lower()

    codeNum1 = 0
    codeNum2 = 2


    url += "01.html"

    #Finding name of player to check validity
    checkRate(rate)
    page = requests.get(url)
    rate += 1

    soup = BeautifulSoup(page.content, 'html.parser')
    player_name = soup.find('h1').text
    player_name = player_name.strip()
    player_name = nopunct(player_name)
    player_name = unidecode(player_name)
    player_name = player_name.lower()


    index = url.index("01")
    


    #url construction with potential ability to have the same base code.
    while True:
        if player_name == player1:
            break
        else:
            url = url[:index]
            url = url + str(codeNum1) + str(codeNum2) + ".html"

            #redo player name with the new url
            checkRate(rate)
            page = requests.get(url)
            rate += 1

            soup = BeautifulSoup(page.content, 'html.parser')

            player_name = soup.find('h1').text
            player_name = player_name.strip()
            player_name = unidecode(player_name)
            player_name = player_name.lower()
            player_name = nopunct(player_name)

            codeNum2 += 1

            if codeNum2>8:
                break

            if (codeNum2 % 10)==0:
                codeNum1 += 1
                codeNum2 = codeNum2 - 10
    return soup



def scrapeStats(page, season1):
    global rate
    #Making table with soup and pandas
    dictionary = {}


    table = page.find_all("table")
    try:
        dfs1 = pd.read_html(str(table))[0]
    except:
        return dictionary
    

    dfs1 = dfs1.fillna(0)


    baseDFS = dfs1.to_dict('index')

    baseStats = ["MP", "FG", "FGA", "3P", "3PA", "2P", "2PA", "FT", "FTA", "TRB", "AST", "STL", "BLK", "TOV", "PF", "PTS"]
    

    listID = 0

    while True:
        while True:
            try:
                seas = baseDFS[listID]["Season"]
            except:
                listID += 1
            else:
                break
            
            if listID>100:
                return dictionary
        
        if seas == season1:
            break
        else:
            listID += 1
    


    for stat in baseStats:
        try:
            dictionary[stat] = baseDFS[listID][stat]
        except:
            pass



    return dictionary

    

