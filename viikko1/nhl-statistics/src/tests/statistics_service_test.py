import unittest
from src.statistics_service import StatisticsService, SortBy
from src.player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_returns_player_if_name_exists(self):
        player = self.stats.search("Semenko")
        self.assertEqual(player.name, "Semenko")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 4)
        self.assertEqual(player.assists, 12)

    def test_search_returns_none_if_name_does_not_exist(self):
        player = self.stats.search("Non-existent")
        self.assertIsNone(player)

    def test_team_returns_players_of_given_team(self):
        edm_players = self.stats.team("EDM")
        self.assertEqual(len(edm_players), 3)
        self.assertEqual(edm_players[0].name, "Semenko")
        self.assertEqual(edm_players[1].name, "Kurri")
        self.assertEqual(edm_players[2].name, "Gretzky")
        
        for player in edm_players:
            self.assertEqual(player.team, "EDM")

    def test_team_returns_empty_list_if_team_does_not_exist(self):
        team_players = self.stats.team("NON")
        self.assertEqual(len(team_players), 0)

    def test_top_returns_players_sorted_by_points(self):
        top_players = self.stats.top(3)
        
        self.assertEqual(len(top_players), 4)  # Returns how_many + 1 players
        self.assertEqual(top_players[0].name, "Gretzky")  # 124 points
        self.assertEqual(top_players[1].name, "Lemieux")  # 99 points
        self.assertEqual(top_players[2].name, "Yzerman")  # 98 points
        self.assertEqual(top_players[3].name, "Kurri")    # 90 points

    def test_top_returns_all_players_if_how_many_exceeds_player_count(self):
        top_players = self.stats.top(10)
        self.assertEqual(len(top_players), 5)  # All players from stub

    def test_top_by_points_returns_players_in_correct_order(self):
        top_players = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(len(top_players), 4)
        self.assertEqual(top_players[0].name, "Gretzky")  # 124 points
        self.assertEqual(top_players[1].name, "Lemieux")  # 99 points
        self.assertEqual(top_players[2].name, "Yzerman")  # 98 points
        self.assertEqual(top_players[3].name, "Kurri")    # 90 points

    def test_top_by_goals_returns_players_in_correct_order(self):
        top_players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(len(top_players), 4)
        self.assertEqual(top_players[0].name, "Lemieux")  # 45 goals
        self.assertEqual(top_players[1].name, "Yzerman")  # 42 goals
        self.assertEqual(top_players[2].name, "Kurri")    # 37 goals
        self.assertEqual(top_players[3].name, "Gretzky")  # 35 goals

    def test_top_by_assists_returns_players_in_correct_order(self):
        top_players = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(len(top_players), 4)
        self.assertEqual(top_players[0].name, "Gretzky")  # 89 assists
        self.assertEqual(top_players[1].name, "Yzerman")  # 56 assists
        self.assertEqual(top_players[2].name, "Lemieux")  # 54 assists
        self.assertEqual(top_players[3].name, "Kurri")    # 53 assists
