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
        if len(stats)<8:
            continue
        else:
            dict[name] = stats
    return dict

def giveGrade(rosterDict):
    sortedDict = dict(sorted(rosterDict.items(), key=lambda item: item[1]['MP'], reverse=True))
    for key in sortedDict:
        totalMin = 0
        stats = sortedDict[key]
        mp = stats["MP"]

        percentile = PlayerRanking.percentile(stats, "2023", key, False, False)

        pos = PlayerRanking.percentile(stats, "2023", key, True, False)

        grade = PlayerRanking.grader(percentile, pos, True)

        if (totalMin + mp)>243:
            teamGrade = (243-totalMin)*grade
            break
        else:
            teamGrade = mp*grade

    teamGrade = teamGrade/243
    return teamGrade

            





choice = UserInput.inputNum()

if choice == 1:
    player = UserInput.inputChoice(choice)
    choice = 5
    seasonFull = UserInput.inputChoice(choice)
    season = seasonFull[:5] + seasonFull[-2:] 

    panda = Scraping.scrapeURL(player, season)
    #print(url)

    stats = Scraping.scrapeStats(panda, season)
    print(stats)
    seasonNum = seasonFull[-4:]

    seasonNum = int(seasonNum)
    percentile = PlayerRanking.percentile(stats, seasonNum, player, False, True)
    print(percentile)
    pos = PlayerRanking.percentile(stats, seasonNum, player, True, False)
    grade = PlayerRanking.grader(percentile, pos, False)
    #print(percentile)
    print("Grade: ", grade)

elif choice == 2:
    teamOne = UserInput.teamOne()
    teamTwo = UserInput.teamTwo()
    status = True

    rosterTeamOne = Scraping.scrapePlayers(status, teamOne)
    #rosterTeamTwo = Scraping.scrapePlayers(status, teamTwo)

    #print(rosterTeamOne)
    #print(rosterTeamTwo)
    one = makeTeamDict(rosterTeamOne)
    #two = makeTeamDict(rosterTeamTwo)

    oneGrade = giveGrade(one)

    print(one)
    print(oneGrade)
    #print(two)




            






