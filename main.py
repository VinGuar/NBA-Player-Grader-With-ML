import GameSimulations
import PlayerRanking
import Scraping
import TeamRankings
import UserInput

choice = UserInput.inputNum()

if choice == 1:
    player = UserInput.inputChoice(choice)
    choice = 5
    season = UserInput.inputChoice(choice)

url = Scraping.scrapeURL(player, season)
print(url)

stats = Scraping.scrapeStats(url, season)
print(url, stats)