import unittest
from controllers.game_controller import games
from models.game import Game, team_power
from models.team import Team
from models.league import League
from models.monster import Monster
class TestGame(unittest.TestCase):

    def setUp(self):
        self.league = League("Test League 1")
        self.team_1 = Team("Test Team 1",self.league)
        self.team_2 = Team("Test Team 2",self.league)
        self.game_1 = Game(self.league,self.team_1, self.team_2)
        self.monster_1 = Monster("John",8,"Blizzard",self.team_1)
        self.monster_2 = Monster("John",4,"Blizzard",self.team_1)
        self.monster_3 = Monster("John",4,"Blizzard",self.team_1)
        self.monster_4 = Monster("John",4,"Blizzard",self.team_2)
        self.monster_5 = Monster("John",4,"Blizzard",self.team_2)
        self.monster_6 = Monster("John",4,"Blizzard",self.team_2)
        
    def test_monster_name__John(self):
        self.assertEqual("John", self.monster_1.name)
    
    def test_monster_limbs__8(self):
        self.assertEqual(8,self.monster_1.limbs)
        
    def test_team_power__weather_match_result_16(self):
         # Act
        monsters = [self.monster_1]
        expected = team_power("Blizzard",monsters)
        actual = 16
        # Assert
        self.assertEqual(actual, expected) 

    def test_team_power__weather_mismatch_result_8(self):
        # Act
        monsters = [self.monster_1]
        expected = team_power("Hail",monsters)
        actual = 8
        # Assert
        self.assertEqual(actual, expected) 

    def test_play__result_home_team_win(self):
         # Act
        monsters_1 = [self.monster_1,self.monster_2,self.monster_3]
        monsters_2 = [self.monster_4,self.monster_5,self.monster_6]     
        #play game asigns a team to winning_team attribute on Game instance
        self.game_1.play(monsters_1,monsters_2)

        actual = self.game_1.winning_team
        expected = self.team_1
        
        # Assert
        self.assertEqual(actual, expected) 

    def test_play__result_away_team_win(self):
         # Act
        monsters_2 = [self.monster_1,self.monster_2,self.monster_3]
        monsters_1 = [self.monster_4,self.monster_5,self.monster_6]     
        #play game asigns a team to winning_team attribute on Game instance
        self.game_1.play(monsters_1,monsters_2)

        actual = self.game_1.winning_team
        expected = self.team_2
        
        # Assert
        self.assertEqual(actual, expected) 

    def test_play__result_home_team_win_if_draw(self):
         # Act
         #first monster was only monster that had more limbs, equal all agents
        self.monster_1.limbs = 4
        monsters_1 = [self.monster_1,self.monster_2,self.monster_3]
        monsters_2 = [self.monster_4,self.monster_5,self.monster_6]     
        #play game asigns a team to winning_team attribute on Game instance
        self.game_1.play(monsters_1,monsters_2)

        actual = self.game_1.winning_team
        expected = self.team_1
        
        # Assert
        self.assertEqual(actual, expected) 