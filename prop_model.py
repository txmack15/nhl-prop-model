import requests
import pandas as pd
import json

def get_player_stats(player_id):
    url = f"https://api-web.nhle.com/v1/player/{player_id}/landing"
    response = requests.get(url)
    data = response.json()

    player_stats = {
        "name": data["firstName"]["default"] + " " + data["lastName"]["default"],
        "shots": data["featuredStats"]["regularSeason"]["subSeason"]["shots"],
        "goals": data["featuredStats"]["regularSeason"]["subSeason"]["goals"],
        "assists": data["featuredStats"]["regularSeason"]["subSeason"]["assists"],
        "games_played": data["featuredStats"]["regularSeason"]["subSeason"]["gamesPlayed"]
    }

    return player_stats

players = [get_player_stats(8478402), get_player_stats(8477934)]
df = pd.DataFrame(players)


for index, row in df.iterrows():
    print(f"{row['name']} - Shots: {row['shots']}, Goals: {row['goals']}, Assists: {row['assists']}, Games Played: {row['games_played']}")

raw = '```json\n[{"caption": "What a win for the Oilers tonight!", "hashtags": "#LetsGoOilers #NHL"}]\n```'

clean = raw.replace("```json", "").replace("```", "").strip()
print(clean) 

posts = json.loads(clean)
print(posts)
print(type(posts))
print(posts[0] ["caption"])