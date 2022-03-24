import unittest

from game import Game


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_check_environment_size_of_two(self):
        game = Game(2)

        self.assertEqual(game.get_size(), 2)

    def test_check_environment_size_of_three(self):
        game = Game(3)

        self.assertEqual(game.get_size(), 3)


if __name__ == '__main__':
    unittest.main()
