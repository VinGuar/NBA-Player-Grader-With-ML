import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from unidecode import unidecode

#make sure do not go over rate limit
rate = 0
def checkRate(r):
    global rate
    if r > 17:
        rate = 0
        time.sleep(60)

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
    print(rate)
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
        print(player_name, player1)
        if player_name == player1:
            break
        else:
            url = url[:index]
            url = url + str(codeNum1) + str(codeNum2) + ".html"

            #redo player name with the new url
            checkRate(rate)
            print(rate)
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
    return url



def scrapeStats(url, season1):
    global rate
    #Making table with soup and pandas
    dictionary = {}

    checkRate(rate)
    print(rate)
    page = requests.get(url)
    rate += 1

    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find_all("table")
    try:
        dfs1 = pd.read_html(str(table))[0]
    except:
        print("could not find table for url: " + url)
        return dictionary
    
    #dfs2 = pd.read_html(str(table))[7]

    dfs1 = dfs1.fillna(0)

    #print(dfs.to_dict('index'))

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
                print("Error. listID too high. Will return blank dict. URL was: " + url)
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

    

#team array for url
teams = ["MIL", "BOS", "PHI", "CLE", "NYK", "BRK", "MIA", "ATL", "TOR", "WAS", "CHI", "IND", "ORL", "CHO", "DET", "DEN", "MEM", "SAC", "PHO", "GSW", "LAC", "MIN", "OKC", "DAL", "LAL", "UTA", "NOP", "POR", "SAS", "HOU"]
teams.sort()
   
#get the roster for teams
def scrapeRosterURL(status, teamNum):
    url = "https://www.basketball-reference.com/teams/"
    if status == False:
        url = url + teams[teamNum] + "/2023.html"
    else:
        url = url + teamNum + "/2023.html"

    return url

#get dictionary of active players
def scrapePlayers(status, teamAbbr):
    global rate
    players = []

    for n in range (30):

        #sportsreference limits 20 request per minute so need to wait a minute
        if status == True:
            url = scrapeRosterURL(status, teamAbbr)
        else:
            url = scrapeRosterURL(status, n)

        checkRate(rate)
        print(rate)
        page = requests.get(url)
        rate += 1

        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find_all("table")
        df1 = pd.read_html(str(table))[0]
        df1 = df1.fillna(0)

        df1 = df1.to_dict('index')


        for x in range(len(df1)):

            player = df1[x]["Player"]

            if " (TW)" in player:
                player = player.replace(' (TW)', '') 

            players.append(player)

        if status == True:
            break
        

            
    return players