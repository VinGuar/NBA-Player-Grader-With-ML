from sportsipy.nba.roster import Player
from sportsipy.nba.roster import Roster

houston = Roster('BRK')
for player in houston.players:
    # Prints the name of all players who played for Houston in the most
    # recent season.
    print(player.name)