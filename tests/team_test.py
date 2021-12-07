import unittest
from models.team import Team
from models.league import League
class TestTeam(unittest.TestCase):
    def setUp(self):
        self.league_1 = League("Test League")
        self.team_1 = Team("Test Team",self.league_1)

    def test_team_name__Test_Team(self):
        self.assertEqual("Test Team" , self.team_1.name)

    def test_team_league__league_1(self):
        self.assertEqual(self.team_1.league, self.league_1)