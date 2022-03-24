from unittest import TestCase

from game import Game


class TestGame(TestCase):

    def test_something(self):
        self.assertEqual(True, True)

    def test_check_environment_size_of_two(self):
        game = Game(2)

        self.assertEqual(game.get_size(), 2)

    def test_check_environment_size_of_three(self):
        game = Game(3)

        self.assertEqual(game.get_size(), 3)

    def test_a_vale_of_a_cell_when_game_start_is_died(self):
        game = Game(3)

        self.assertEqual(game.get_cell(1, 1), False)
