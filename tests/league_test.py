import unittest
from models.league import League


class TestLeague(unittest.TestCase):
    def setUp(self):
        self.league_1 = League("Test League")

    def test_league_name__Test_League(self):
        self.assertEqual("Test League", self.league_1.name)