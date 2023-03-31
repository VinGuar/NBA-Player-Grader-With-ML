# NBA_PlayerGradingSystem  
This repository is a system to grade NBA players based on stats that correlate to winning, obtained from machine learning. 

It goes back to when the 3 point line was invented in 1980. It gives both regular grades and grades based on per36 stats, whichever you may prefer.

It is a great way to grade players and see how much they can actually correlate towards a win. Some players are said to "put up empty stats", and this program is made to help see when players do that. 


### How it works
-Uses ridge regression machine learning to find how much each stat correlates to a win per position. Uses 6 years of every single games data to find information.

-It then takes a player and makes it's stats into percentiles based on other players in their year and position and above 18 minutes a game. Also has option to make it per 36 minutes.

-Then, it multiplies the percentile with the machine learning numbers to create the grade. Gives half as much importance to the negatives and twice to the points to help even it out.


### File breakdown

AllPlayer.csv: list of all players stats dating back to 1980, used to get position for each player

Book2.csv: list of all players from 1980 that have at least 18 minutes, used to get percentiles for grading.

MachineLearningWithGoogleColab.ipynb: This is where I did the machine learning to get the information on what correlates to winning, and used this to make grade.

main.py: Code runs from here

Player161718.csv and player12131415.csv: These are the data I used for my machine learning. Has every game in these years.

PlayerRanking.py: This is where the grading is done.

Scraping.py: This is where the URL is made and the stats is scraped from sportsreference

UserInput.py: This is the file where the user input is obtained.


### Other tips/information

-Uses sportsreference for the information, and they only allow 20 requests per minute. If you ever go above 20, it will put you in "jail" for one hour and not let you use website, which makes the code not work.

-If there is an error or it does not work, there are normally 3 common reasons. 1: Sportsreference is down or not working.  2: Player name or season were incorrectly entered.   3: You got rate limited from the website.
 <br>
 
 <br>
### Let me know if there is any questions or if you need help.

![NBA LOGO](https://andscape.com/wp-content/uploads/2017/06/nbalogo.jpg?w=700)


