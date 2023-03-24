import GameSimulations
import PlayerRanking
import Scraping
import TeamRankings
import UserInput
import PlayerRanking


#print(Scraping.scrapeActivePlayers())


choice = UserInput.inputNum()


if choice == 1:
    player = UserInput.inputChoice(choice)
    choice = 5
    seasonFull = UserInput.inputChoice(choice)

season = seasonFull[:5] + seasonFull[-2:] 

url = Scraping.scrapeURL(player, season)
print(url)

stats = Scraping.scrapeStats(url, season, "base")
print(stats)

seasonNum = seasonFull[-4:]
seasonNum = int(seasonNum)

percentile = PlayerRanking.percentile(stats, seasonNum, player)
print(percentile)