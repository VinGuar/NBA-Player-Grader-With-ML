import UserInput
import requests
from bs4 import BeautifulSoup
import pandas as pd


#player name from User
player1 = UserInput.player
season1 = UserInput.season



#creating first and last name variables for player
names = player1.split()
firstName = names[0]
lastName = names[1]

punctuations = '''!()-[];:'"\,<>./?@#$%^&*_~'''

none = ""

for char in firstName:
    if char not in punctuations:
        none = none + char

firstName = none

#remove punctuation
no_punct = ""
for char in lastName:
    if char not in punctuations:
        no_punct = no_punct + char

lastName = no_punct



url = "https://www.basketball-reference.com/players/"


#insert the player name part of the url
url += (lastName[0].lower() + "/")
for num in range(5):
    url += lastName[num].lower()
for num in range (2):
    url += firstName[num].lower()

codeNum1 = 0
codeNum2 = 2


url += "01.html"

#Finding name of player to check validity
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
player_name = soup.find('h1').text
player_name = player_name.strip()

index = url.index("01")

#url construction with potential ability to have the same base code.
while True:
    if player_name.lower() == player1.lower():
        break
    else:
        url = url[:index]
        url = url + str(codeNum1) + str(codeNum2) + ".html"

        #redo player name with the new url
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        player_name = soup.find('h1').text
        player_name = player_name.strip()

        codeNum2 += 1


        if codeNum2>5:
            break

        if (codeNum2 % 10)==0:
            codeNum1 += 1
            codeNum2 = codeNum2 - 10


print(url)

#Making table with soup and pandas
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find_all("table")
dfs = pd.read_html(str(table))[0]
dfs = dfs.fillna(0)

#print(dfs.to_dict('index'))

newDFS = dfs.to_dict('index')

listThrees = ["MP", "FG", "FGA", "FG%", "3P", "3PA", "3P%", "2P", "2PA", "2P%", "eFG%", "FT", "FTA", "FT%", "ORB", "DRB", "TRB", "AST", "STL", "BLK", "TOV", "PF", "PTS"]

listID = 0

while True:
    while True:
        try:
            seas = newDFS[listID]["Season"]
        except:
            listID += 1
        else:
            break
        
        if listID>100:
            print("Error. listID too high.")
            exit()
    
    if seas == season1:
        break
    else:
        listID += 1
   
print(seas)
print(season1)
print(listID)



dictionary = {}

for stat in listThrees:
    dictionary[stat] = newDFS[listID][stat]


#newDFS = newDFS[0]["eFG%"]

print(dictionary)






 

