import UserInput

#player name from User
player1 = UserInput.player

#creating first and last name variables for player
names = player1.split()
firstName = names[0]
lastName = names[1]

url = "https://www.basketball-reference.com/players/"


index = url.find("players/") + 8

url += (lastName[0] + "/")
for num in range(5):
    url += lastName[num]
for num in range (2):
    url += firstName[num]

url += "01.html"

print(url)





