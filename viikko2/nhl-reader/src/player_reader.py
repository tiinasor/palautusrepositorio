import requests
from rich.console import Console
from rich.table import Table
from player import Player

BASE_URL = "https://studies.cs.helsinki.fi/nhlstats"

class PlayerReader:
    def __init__(self, season: str):
        self.season = season
        self.url = f"{BASE_URL}/{season}/players"

    def get_players(self):
        response = requests.get(self.url, timeout=10)
        response.raise_for_status()
        return [Player(d) for d in response.json()]

    def players(self):
        return self.get_players()

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality: str):
        players = self.reader.get_players()
        selected = list(filter(lambda p: p.nationality == nationality, players))
        return sorted(selected, key=lambda p: p.goals + p.assists, reverse=True)

    def print_stats(self, nationality: str):
        console = Console()
        header, table = self._build_tables(nationality)

        console.print(header)
        console.print(table)

    def _build_tables(self, nationality: str):
        table = Table(show_header=True, padding=(0, 2))
        columns = [
            ("Released", {"style": "cyan"}),
            ("teams", {"style": "magenta"}),
            ("goals", {"justify": "right", "style": "green"}),
            ("assists", {"justify": "right", "style": "green"}),
            ("points", {"justify": "right", "style": "green"}),
        ]

        for col_name, col_opts in columns:
            table.add_column(col_name, **col_opts)

        for player in self.top_scorers_by_nationality(nationality):
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(player.goals + player.assists),
            )

        header = Table(
            show_header=False,
            width=len(table.columns) * 12,
            padding=(0, 0),
            show_edge=False,
            show_lines=False,
        )
        header.add_column("header", justify="center")
        header.add_row(f"[italic]Season {self.reader.season} players from {nationality}[/italic]")

        return header, table
