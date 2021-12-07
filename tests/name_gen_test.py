import unittest
from models.name_gen import random_name
class TestName_gen(unittest.TestCase):
    def test_name_is_not_None(self):
        gen_name = random_name()
        self.assertNotEqual(None, gen_name)

    def test_name_is_string__True(self):
        gen_name = random_name()
        # check if gen_name is a string
        is_string = isinstance(gen_name, str)

        self.assertEqual(True, is_string)

