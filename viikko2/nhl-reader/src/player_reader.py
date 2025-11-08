import requests
from player import Player

class PlayerReader:
    def __init__(self, url: str):
        self.url = url

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
