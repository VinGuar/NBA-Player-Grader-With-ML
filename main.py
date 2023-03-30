import GameSimulations
import PlayerRanking
import Scraping
import TeamRankings
import UserInput
import PlayerRanking

choice = UserInput.inputNum()

if choice == 1 or choice == 2 or choice == 3:
    player = UserInput.inputChoice(choice)
    choice = 5
    seasonFull = UserInput.inputChoice(choice)
    season = seasonFull[:5] + seasonFull[-2:] 

    panda = Scraping.scrapeURL(player, season)
    #print(url)

    stats = Scraping.scrapeStats(panda, season)
    seasonNum = seasonFull[-4:]

    statswmin = stats.copy()

    seasonNum = int(seasonNum)
    percentile = PlayerRanking.percentile(stats, seasonNum, player, False, True)
    print(percentile)
    pos = PlayerRanking.percentile(stats, seasonNum, player, True, False)
    grade = PlayerRanking.grader(percentile, pos, False)
    per36 = PlayerRanking.per36(statswmin, seasonNum, player)
    #print(percentile)
    if choice == 3:
        print(f"Regular grade: {grade} Per 36 grade: {per36}")
    elif choice == 2:
        print(f"Per 36 grade: {per36}")
    elif choice == 1:
        print(f"Regular grade: {grade}")
