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
    sortedDict = dict(sorted(rosterDict.items(), key=lambda item: float(item[1]['MP']), reverse=True))
    x = 0
    totalMin = 0
    teamGrade = 0
    for key in sortedDict:
        if x > 9:
            break
        if key == "LaMelo Ball" or key == "Terry Rozier" or key == "Kelly Oubre Jr.":
            continue

        stats = sortedDict[key]
        mp = stats["MP"]
        mp = float(mp)
        totalMin = totalMin + mp

        statswmin2 = stats.copy()
        
        stats.pop("MP")

        percentile = PlayerRanking.percentile(stats, 2023, key, False, False)
        pos = PlayerRanking.percentile(stats, 2023, key, True, False)
        grade = PlayerRanking.grader(percentile, pos, False)

        #per36 = PlayerRanking.per36(statswmin2, 2023, key)
        #print(grade, teamGrade, mp, totalMin)

        if (totalMin + mp)>230:
            teamGrade = teamGrade + (230-totalMin)*grade
            totalMin = 230
            break
        else:
            teamGrade = teamGrade + mp*grade

        x+=1
    print(totalMin)
    teamGrade = teamGrade/totalMin
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
    seasonNum = seasonFull[-4:]

    statswmin = stats.copy()

    seasonNum = int(seasonNum)
    percentile = PlayerRanking.percentile(stats, seasonNum, player, False, True)
    print(percentile)
    pos = PlayerRanking.percentile(stats, seasonNum, player, True, False)
    grade = PlayerRanking.grader(percentile, pos, False)
    per36 = PlayerRanking.per36(statswmin, seasonNum, player)
    #print(percentile)
    print(f"Grade: {grade} Per 36 grade: {per36}")

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

    oneGrade = giveGrade(one)
    twoGrade = giveGrade(two)

    #print(one)
    print(f"{teamOne} grade is: {oneGrade}, and {teamTwo} grade is: {twoGrade}")
    #print(two)




            






