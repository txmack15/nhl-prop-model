import requests
import pandas as pd
import json
from scipy.stats import poisson
import math

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



df["prop_line"] = [45.5, 30.5]
df["edge"] = df["goals"] - df["prop_line"]

def calculate_sog_projection(sog_per_60, toi_avg, season_sog, games_played, l10_icf_avg, opp_factor, line):
    term1 = 0.65 * (sog_per_60 * toi_avg / 60)
    term2 = 0.2 * (season_sog / games_played)
    term3 = 0.15 * l10_icf_avg

    proj_sog = max(0, min(8, term1 + term2 + term3))
    adj_proj_sog = proj_sog * opp_factor
    edge = adj_proj_sog - line

    return {
        "proj_sog": proj_sog,
        "adj_proj_sog": adj_proj_sog,
        "edge": edge
    }

eichel_projection = calculate_sog_projection(
    sog_per_60=8.37,
    toi_avg=25.80,
    season_sog=260,
    games_played=74,
    l10_icf_avg=2.9,
    opp_factor=1.000,
    line=2.5
)

def american_odds_to_implied_prob(odds):
    if odds > 0:
        return 100 / (odds + 100)
    else:
        return abs(odds) / (abs(odds) + 100)

print(american_odds_to_implied_prob(-110))

def calculate_model_prob_over(adj_proj_sog, line):
    return 1 - poisson.cdf(math.floor(line), adj_proj_sog)

print(calculate_model_prob_over(3.479, 2.5))
