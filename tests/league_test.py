import unittest
from controllers.game_controller import games
from models.game import Game, team_power
from models.team import Team
from models.league import League
from models.monster import Monster

class TestLeague(unittest.TestCase):
    def setUp(self):
        self.league_1 = League("Test League")

    def test_league_name__Test_League(self):
        self.assertEqual("Test League", self.league_1.name)