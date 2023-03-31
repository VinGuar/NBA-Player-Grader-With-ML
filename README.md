# NBA_PlayerGradingSystem

This repository is a system to grade NBA players based on stats that correlate to winning, obtained from machine learning. 

It goes back to when the 3 point line was invented in 1980. It gives both regular grades and grades based on per36 stats, whichever you may prefer.

### How it works
-Uses ridge regression machine learning to find how much each stat correlates to a win per position. Uses 6 years of every single games data to find information.
-It then takes a player and makes it's stats into percentiles based on other players in their year and position and above 18 minutes a game. Also has option to make it per 36 minutes.
-Then, it multiplies the percentile with the machine learning numbers to create the grade. Gives half as much importance to the negatives and twice to the points to help even it out.

### Other tips/information

-Uses sportsreference for the information, and they only allow 20 requests per minute. If you ever go above 20, it will put you in "jail" for one hour and not let you use website, which makes the code not work.
-If there is an error or it does not work, there are normally 3 common reasons. 1: Sportsreference is down or not working.  2: Player name or season were incorrectly entered.   3: You got rate limited from the website.

### Summary

All in all this is a great way to grade players and see how much they can actually correlate towards a win. Some players are said to "put up empty stats", and this program is made to help see when players do that. Let me know if there is any questions or if you need help.



if error may basketball reference or issue with player name
x
