# NHL Prop Model

Pulls player stats from the NHL's public API (name, shots, goals, assists, games played) and loads them into a pandas dataframe. Includes a full SOG (shots-on-goal) prop betting model translated from a production spreadsheet, including:

- Weighted projection (recent shot rate, season average, and shot-attempt rate)
- Opponent-adjusted projection
- Edge calculation (projection vs. betting line)
- American odds to implied probability conversion
- Model probability of the Over, using a Poisson distribution (scipy)

Every formula is verified against real output from an existing production spreadsheet used for live betting decisions.

## How to run

1. Install the required packages:
pip3 install pandas requests scipy --break-system-packages

2. Run the script:
python3 prop_model.py
   
## Status

Core SOG model math is complete and verified. Currently uses hardcoded sample inputs for opponent factor, recent ice time, and other rate stats — next step is wiring these to a real data source instead of manual entry.

## Next steps

- Source live inputs (opponent factor, recent stats) instead of hardcoded sample values
- Extend the same pattern to Goals and Assists prop models
- Pull a full team or league roster instead of hardcoded player IDs
