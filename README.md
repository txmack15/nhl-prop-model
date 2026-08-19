# NHL Prop Model

Pulls player stats from the NHL's public API (name, shots, goals, assists, games played) and loads them into a pandas dataframe as the foundation for an NHL player prop betting model.

## How to run

1. Install the required packages:


2. Run the script:



## Status

Currently fetches live stats for a hardcoded list of player IDs and displays them in a table. Still missing: prop line comparison and edge calculation (comparing projected stats against a betting line, as built out in earlier versions of this project using sample data).

## Next steps

- Add prop line and edge calculation columns
- Pull a full team or league roster instead of hardcoded player IDs
- Handle missing/incomplete player data