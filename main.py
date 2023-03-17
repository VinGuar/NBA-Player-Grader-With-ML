import GameSimulations
import PlayerRanking
import Scraping
import TeamRankings
import UserInput


#print(Scraping.scrapeActivePlayers())


choice = UserInput.inputNum()


if choice == 1:
    player = UserInput.inputChoice(choice)
    choice = 5
    season = UserInput.inputChoice(choice)

url = Scraping.scrapeURL(player, season)
print(url)

stats = Scraping.scrapeStats(url, season, "base")
print(stats)
