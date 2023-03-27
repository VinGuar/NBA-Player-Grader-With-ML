import GameSimulations
import PlayerRanking
import Scraping
import TeamRankings
import UserInput
import PlayerRanking

def makeTeamDict(rosterArr):
    dict = {}
    for n in range(len(rosterArr)):
        name = rosterArr[n]

        url = Scraping.scrapeURL(name, "2022-23")
        stats = Scraping.scrapeStats(url, "2022-23")

        dict[name] = stats
    return dict


choice = UserInput.inputNum()

if choice == 1:
    player = UserInput.inputChoice(choice)
    choice = 5
    seasonFull = UserInput.inputChoice(choice)
    season = seasonFull[:5] + seasonFull[-2:] 

    url = Scraping.scrapeURL(player, season)
    #print(url)

    stats = Scraping.scrapeStats(url, season)
    print(stats)
    seasonNum = seasonFull[-4:]

    seasonNum = int(seasonNum)
    percentile = PlayerRanking.percentile(stats, seasonNum, player, False)

    pos = PlayerRanking.percentile(stats, seasonNum, player, True)
    grade = PlayerRanking.grader(percentile, pos)
    #print(percentile)
    print("Grade: " + grade)

elif choice == 2:
    teamOne = UserInput.teamOne()
    teamTwo = UserInput.teamTwo()
    status = True

    rosterTeamOne = Scraping.scrapePlayers(status, teamOne)
    rosterTeamTwo = Scraping.scrapePlayers(status, teamTwo)

    #print(rosterTeamOne)
    #print(rosterTeamTwo)
    one = makeTeamDict(rosterTeamOne)
    two = makeTeamDict(rosterTeamTwo)

    print(one)
    print(two)




            






