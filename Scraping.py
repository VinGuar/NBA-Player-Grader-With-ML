import UserInput
import requests
from bs4 import BeautifulSoup


#player name from User
player1 = UserInput.player



#creating first and last name variables for player
names = player1.split()
firstName = names[0]
lastName = names[1]

punctuations = '''!()-[];:'"\,<>./?@#$%^&*_~'''

none = ""

for char in firstName:
    if char not in punctuations:
        none = none + char

firstName = no_punct

no_punct = ""
for char in lastName:
    if char not in punctuations:
        no_punct = no_punct + char

lastName = no_punct



url = "https://www.basketball-reference.com/players/"



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



 

