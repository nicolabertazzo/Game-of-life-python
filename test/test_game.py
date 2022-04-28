from unittest import TestCase

from game import Game


class TestGame(TestCase):

    def test_a_value_of_a_cell_when_game_start_is_died(self):
        game = Game(3)

        self.assertEqual(game.get_cell(1, 1), False)

    def test_set_a_value_of_a_cell_and_get_the_value(self):
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

    def test_underpopulation_rule_no_neighbours_size_3(self):
        initial_matrix = [
            [False, False, False],
            [False, True, False],
            [False, False, False]
        ]
        game = Game(size_x=3, initial_matrix=initial_matrix)

        game.next_status()

        self.assertFalse(game.get_cell(1, 1))

    def test_underpopulation_rule_no_neighbours_size_4(self):
        initial_matrix = [
            [False, False, False, False],
            [False, False, True, False],
            [False, False, False, False],
            [False, False, False, False]
        ]
        game = Game(size_x=4, initial_matrix=initial_matrix)

        game.next_status()

        self.assertFalse(game.get_cell(1, 2))

    def test_underpopulation_rule_with_alive_on_corner_and_no_neighbours(self):
        initial_matrix = [
            [True, False, False],
            [False, False, False],
            [False, False, False]
        ]
        game = Game(size_x=3, initial_matrix=initial_matrix)

        game.next_status()

        self.assertFalse(game.get_cell(0, 0))

    def test_underpopulation_rule_with_alive_neighbours(self):
        initial_matrix = [
            [True, False, True],
            [False, True, False],
            [False, False, False]
        ]
        game = Game(size_x=3, initial_matrix=initial_matrix)

        game.next_status()

        self.assertTrue(game.get_cell(1, 1))

    def test_overcrowding_rule_four_neighbours_size_3(self):
        initial_matrix = [
            [True, False, True],
            [False, True, True],
            [False, True, False]
        ]
        game = Game(size_x=3, initial_matrix=initial_matrix)

        game.next_status()

        self.assertFalse(game.get_cell(1, 1))

    def test_continuing_to_live_rule_three_neighbours_size_3(self):
        initial_matrix = [
            [True, False, False],
            [False, True, True],
            [False, True, False]
        ]
        game = Game(size_x=3, initial_matrix=initial_matrix)

        game.next_status()

        self.assertTrue(game.get_cell(1, 1))

    def test_continuing_to_live_rule_three_neighbours_size_3_on_matrix_edge(self):
        initial_matrix = [
            [True, False, True],
            [False, True, True],
            [False, True, False]
        ]
        game = Game(size_x=3, initial_matrix=initial_matrix)

        game.next_status()

        self.assertTrue(game.get_cell(0, 2))

    def test_born_to_live(self):
        initial_matrix = [
            [True, False, True],
            [False, False, True],
            [False, False, False]
        ]
        game = Game(size_x=3, initial_matrix=initial_matrix)

        game.next_status()

        self.assertTrue(game.get_cell(1, 1))

    def test_born_to_live_on_matrix_edge(self):
        initial_matrix = [
            [True, False, True],
            [False, True, True],
            [False, True, False]
        ]
        game = Game(size_x=3, initial_matrix=initial_matrix)

        game.next_status()

        self.assertTrue(game.get_cell(2, 2))
