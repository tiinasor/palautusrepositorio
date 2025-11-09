import requests
from player import Player
from rich.console import Console
from rich.table import Table

BASE_URL = "https://studies.cs.helsinki.fi/nhlstats"

class PlayerReader:
    def __init__(self, season: str):
        self.season = season
        self.url = f"{BASE_URL}/{season}/players"

    def get_players(self):
        response = requests.get(self.url).json()
        return [Player(d) for d in response]

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality: str):
        players = self.reader.get_players()
        selected = list(filter(lambda p: p.nationality == nationality, players))
        return sorted(selected, key=lambda p: p.goals + p.assists, reverse=True)

    def print_stats(self, nationality: str):
        console = Console()

        table = Table(show_header=True, padding=(0, 2))
        table.add_column("Released", style="cyan")
        table.add_column("teams", style="magenta")
        table.add_column("goals", justify="right", style="green")
        table.add_column("assists", justify="right", style="green")
        table.add_column("points", justify="right", style="green")

        for player in self.top_scorers_by_nationality(nationality):
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(player.goals + player.assists),
            )

        header = Table(show_header=False, width=len(table.columns) * 12, padding=(0,0), show_edge=False, show_lines=False)
        header.add_column("header", justify="center")
        header.add_row(f"[italic]Season {self.reader.season} players from {nationality}[/italic]")

        console.print(header)
        console.print(table)
