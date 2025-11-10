import argparse
from rich.prompt import Prompt
from player_reader import PlayerReader, PlayerStats

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--season', type=str, default=None)
    parser.add_argument('--nationality', type=str, default=None)
    return parser.parse_args()

def seasons_list() -> list[str]:
    return [
        "2018-19",
        "2019-20",
        "2020-21",
        "2021-22",
        "2022-23",
        "2023-24",
        "2024-25",
        "2025-26",
    ]

def nationalities_list() -> list[str]:
    return [
        "USA",
        "FIN",
        "CAN",
        "SWE",
        "CZE",
        "RUS",
        "SLO",
        "FRA",
        "GBR",
        "SVK",
        "DEN",
        "NED",
        "AUT",
        "BLR",
        "GER",
        "SUI",
        "NOR",
        "UZB",
        "LAT",
        "AUS",
    ]

def choose_season(args: argparse.Namespace) -> str:
    seasons = seasons_list()
    return args.season or Prompt.ask("Season", choices=seasons, default="2024-25")

def interactive_loop(stats: PlayerStats, initial_nationality: str | None) -> None:
    nationalities = nationalities_list()
    first = True
    while True:
        if first and initial_nationality:
            nat = initial_nationality
        else:
            nat = Prompt.ask("Nationality", choices=nationalities, default="")
        first = False

        stats.print_stats(nat)

def main() -> None:
    args = parse_args()
    season = choose_season(args)
    reader = PlayerReader(season)
    stats = PlayerStats(reader)
    interactive_loop(stats, args.nationality)

if __name__ == "__main__":
    main()
