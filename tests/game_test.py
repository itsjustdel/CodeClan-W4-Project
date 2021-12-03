import unittest
from models.game import Game
from models.team import Team
from models.league import League
class TestGame(unittest.TestCase):

    def setUp(self):
        self.league = League("Test League 1")
        self.team_1 = Team("Test Team 1",)
        self.team_2 = Team("Test Team 2",)
        self.game_1 = Game(0,self.team_1, self.team_2)
        
