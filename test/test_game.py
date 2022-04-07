from unittest import TestCase

from game import Game


class TestGame(TestCase):

    def test_a_vale_of_a_cell_when_game_start_is_died(self):
        game = Game(3)

        self.assertEqual(game.get_cell(1, 1), False)

    def test_set_a_vale_of_a_cell_and_get_the_value(self):
        game = Game(3)
        game.set_cell(1, 1, True)
        self.assertEqual(game.get_cell(1, 1), True)

    def test_initialize_game_manually_with_a_matrix(self):
        initial_matrix = [[True, True, True], [False, False, False], [False, False, False]]
        game = Game(size_x=3, initial_matrix=initial_matrix)
        self.assertTrue(game.get_cell(0, 0))

    def test_sizeX_and_sizeY_manually_set(self):
        game = Game(size_x=3, size_y=4)

        self.assertEqual(3, game.get_size_x())
        self.assertEqual(4, game.get_size_y())

    def test_only_sizeX_manually_set(self):
        game = Game(size_x=3)

        self.assertEqual(3, game.get_size_x())
        self.assertEqual(3, game.get_size_y())
