class Player:
    def __init__(self, data: dict):
        self.name = data.get('name', '')
        self.nationality = data.get('nationality', '')
        self.assists = data.get('assists', 0)
        self.goals = data.get('goals', 0)
        self.team = data.get('team', '')
        self.games = data.get('games', 0)
        self.id = data.get('id', None)

    def __str__(self):
        points = self.goals + self.assists
        return f"{self.name:<20} {self.team:<15} {self.goals} + {self.assists} = {points}"
