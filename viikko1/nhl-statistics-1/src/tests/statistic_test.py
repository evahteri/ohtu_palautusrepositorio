import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())
    
    def test_search(self):
        result = self.statistics.search("Yzerman")

        self.assertEqual(result.name, "Yzerman")
    
    def test_search_wrong_name(self):
        result = self.statistics.search("Stamkos")

        self.assertEqual(result, None)

    def test_team(self):
        result = self.statistics.team("EDM")

        self.assertEqual(result[0].name, "Semenko")
    
    def test_top(self):
        result = self.statistics.top(3)
        top3_names = [result[0].name, result[1].name, result[2].name]

        self.assertEqual(top3_names, ["Gretzky", "Lemieux", "Yzerman"])
    
    def test_top_goals(self):
        result = self.statistics.top(3, 2)
        top3_names = [result[0].name, result[1].name, result[2].name]

        self.assertEqual(top3_names, ["Lemieux", "Yzerman", "Kurri"])
    
    def test_top_assists(self):
        result = self.statistics.top(3, 3)
        top3_names = [result[0].name, result[1].name, result[2].name]

        self.assertEqual(top3_names, ["Gretzky", "Yzerman", "Lemieux"])
