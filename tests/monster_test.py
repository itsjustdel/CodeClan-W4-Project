import unittest
from models.monster import Monster

class TestMonster(unittest.TestCase):
    def setUp(self):
        self.monster_1 = Monster("Test Monster",4,"Hail")

    def test_monster_name__Test_Monster(self):
        self.assertEqual("Test Monster", self.monster_1.name)

    def test_monster_limbs__4(self):
        self.assertEqual(4, self.monster_1.limbs)

    def test_monster_weather__Hail(self):
        self.assertEqual("Hail", self.monster_1.fav_weather)