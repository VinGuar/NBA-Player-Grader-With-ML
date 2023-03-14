import requests
import os
from dotenv import load_dotenv

load_dotenv()

apiKey = os.environ.get("API_KEY")
# Get the current roster for the team
rosterUrl = f"https://api-nba-v1.p.rapidapi.com/teams/teamId/{4}"
rosterHeaders = {
    "X-RapidAPI-Key": apiKey,
    "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}
rosterResponse = requests.request("GET", rosterUrl, headers=rosterHeaders)
rosterData = rosterResponse.json()
currentRoster = [player["first_name"] + " " + player["last_name"] for player in rosterData["response"]]

print(currentRoster)