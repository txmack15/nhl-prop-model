eichel = {
    "name": "Jack Eichel",
    "team": "VGK",
    "season_sog": 260,
    "games_played": 74,
    "proj_sog": 3.48
}

dorofeyev = {
    "name": "Pavel Dorofeyev",
    "team": "VGK",
    "season_sog": 229,
    "games_played": 82,
    "proj_sog": 3.17
}

players = [eichel, dorofeyev]

print(players[1]["proj_sog"])

for player in players:
    if player["season_sog"] > 240:
        print(player["name"])

        def format_player(player):
            return player["name"] + " - " + str(player["proj_sog"])

print(format_player(eichel))