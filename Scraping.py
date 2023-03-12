from sportsreference.nba.roster import Player
from sportsreference.nba.roster import Roster

houston = Roster('HOU')
for player in houston.players:
    # Prints the name of all players who played for Houston in the most
    # recent season.
    print(player.name)