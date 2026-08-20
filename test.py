sog_per_60 = 8.37
toi_avg = 25.80
season_sog = 260
games_played = 74
l10_icf_avg = 2.9

term1 = 0.65 * (sog_per_60 * toi_avg / 60)
print(term1)

term2 = 0.2 * (season_sog / games_played)
print(term2)

term3 = 0.15 * l10_icf_avg
print(term3)

proj_sog = max(0, min(8, term1 + term2 + term3))
print(proj_sog)

opp_factor = 1.000
line = 2.5

adj_proj_sog = proj_sog * opp_factor
edge = adj_proj_sog - line

print(adj_proj_sog)
print(edge)
