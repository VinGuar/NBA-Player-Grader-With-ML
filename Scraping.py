from sportsipy.nba.roster import Player

james_harden = Player('hardeja01')
print(james_harden.name)  # Prints 'James Harden'
print(james_harden.points)  # Prints Harden's career points total
# Prints a Pandas DataFrame of all relevant Harden stats per season
print(james_harden.dataframe)
print(james_harden.salary)  # Prints Harden's career earnings
print(james_harden.contract)  # Prints Harden's contract by yearly wages