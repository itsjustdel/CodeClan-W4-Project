import unittest
from models.league import League, sort_teams_by_wins
from models.team import Team
from models.game import Game
from models.monster import Monster

class TestLeague(unittest.TestCase):
    def setUp(self):
        self.league_1 = League("Test League")

    def test_league_name__Test_League(self):
        self.assertEqual("Test League", self.league_1.name)

    def test_sort_teams_by_wins(self):

        team_1 = Team("Test Team 1",self.league_1,0)
        team_2 = Team("Test Team 2",self.league_1,1)
            
        monster_1 = Monster("John",4,"Blizzard",team_1)
        monster_2 = Monster("John",4,"Blizzard",team_1)
        monster_3 = Monster("John",4,"Blizzard",team_1)
        monster_4 = Monster("John",4,"Blizzard",team_2)
        monster_5 = Monster("John",4,"Blizzard",team_2)
        monster_6 = Monster("John",20,"Blizzard",team_2)
        monsters_1 = [monster_1,monster_2,monster_3]
        monsters_2 = [monster_4,monster_5,monster_6]     
        
        game_1 = Game(self.league_1,team_1, team_2)    
        weather = "Blizzard"
        game_1.play(monsters_1,monsters_2, weather)
        
        teams = [team_1, team_2 ]
        games = [game_1]
        teams_and_wins = sort_teams_by_wins(teams,games)

        # team 2 will be first in list return because they won the match
        # the last John in team 2 wins all the time because he has more limbs
        expected = "Test Team 2"
        # first list is list of tuples, second is the team object
        actual = teams_and_wins[0][0].name
        self.assertEqual(actual, expected)

        expected = "Test Team 1"        
        actual = teams_and_wins[1][0].name
        self.assertEqual(actual, expected)