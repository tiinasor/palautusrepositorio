from player_reader import PlayerReader, PlayerStats
import argparse
from rich.prompt import Prompt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--season', type=str, default=None)
    parser.add_argument('--nationality', type=str, default=None)

    args = parser.parse_args()

    seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26"]
    nationalities = ["USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA", "GBR", "SVK", "DEN", "NED", "AUT", "BLR", "GER", "SUI", "NOR", "UZB", "LAT", "AUS"]

    season = args.season or Prompt.ask("Season", choices=seasons, default="2024-25")
    reader = PlayerReader(season)
    stats = PlayerStats(reader)

    first = True
    while True:
        if first and args.nationality:
            nat = args.nationality
        else:
            nat = Prompt.ask("Nationality", choices=nationalities, default="")
        first = False

        stats.print_stats(nat)

if __name__ == "__main__":
    main()
