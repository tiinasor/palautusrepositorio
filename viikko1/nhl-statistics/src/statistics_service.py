from enum import Enum
from src.player_reader import PlayerReader

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class StatisticsService:
    def __init__(self, player_reader):
        self._players = player_reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by=SortBy.POINTS):
        def sort_by_points(player):
            return player.points

        def sort_by_goals(player):
            return player.goals

        def sort_by_assists(player):
            return player.assists

        # Determine which sort function to use
        sort_function = {
            SortBy.POINTS: sort_by_points,
            SortBy.GOALS: sort_by_goals,
            SortBy.ASSISTS: sort_by_assists
        }[sort_by]

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_function
        )

        result = []
        i = 0
        while i < how_many + 1 and i < len(sorted_players):
            result.append(sorted_players[i])
            i += 1

        return result
