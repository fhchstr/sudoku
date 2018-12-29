import unittest

import sudoku
from sudoku import Sudoku

EASY = [
    [None, 3,    2,       1,    5,    9,       None, None, None],
    [None, None, None,    2,    None, None,    None, 9,    None],
    [9,    None, None,    None, 4,    None,    5,    8,    None],

    [None, 8,    3,       6,    9,    None,    7,    None, None],
    [None, 5,    9,       None, None, None,    6,    3,    None],
    [None, None, 4,       None, 8,    3,       1,    5,    None],

    [None, 9,    7,       None, 1,    None,    None, None, 5],
    [None, 6,    None,    None, None, 2,       None, None, None],
    [None, None, None,    5,    6,    7,       9,    4,    None],
]

MEDIUM = [
    [2,    None, None,    None, None, 1,       None, None, 5],
    [None, None, None,    None, 9,    6,       None, 8,    None],
    [None, None, 5,       7,    2,    None,    None, None, 9],

    [None, 5,    None,    None, None, None,    None, 9,    None],
    [None, 8,    7,       None, None, None,    1,    4,    None],
    [None, 9,    None,    None, None, None,    None, 3,    None],

    [3,    None, None,    None, 6,    5,       4,    None, None],
    [None, 2,    None,    1,    3,    None,    None, None, None],
    [9,    None, None,    8,    None, None,    None, None, 3],
]

HARD = [
    [None, 7,    2,       9,    None, None,    3,    None, 8],
    [None, 8,    None,    None, 5,    None,    1,    None, None],
    [None, None, None,    7,    None, None,    4,    None, None],

    [2,    None, None,    None, None, None,    None, 7,    None],
    [6,    None, None,    8,    None, 5,       None, None, 4],
    [None, 1,    None,    None, None, None,    None, None, 9],

    [None, None, 5,       None, None, 1,       None, None, None],
    [None, None, 1,       None, 6,    None,    None, 4,    None],
    [7,    None, 6,       None, None, 8,       9,    2,    None],
]

EVIL = [
    [None, None, None,    1,    None, None,    8,    None, 2],
    [None, None, 7,       8,    None, None,    9,    None, None],
    [None, 8,    1,       9,    None, 3,       None, None, None],

    [8,    None, None,    6,    None, None,    None, None, None],
    [None, 4,    None,    None, None, None,    None, 5,    None],
    [None, None, None,    None, None, 7,       None, None, 9],

    [None, None, None,    3,    None, 2,       6,    7,    None],
    [None, None, 6,       None, None, 9,       1,    None, None],
    [5,    None, 3,       None, None, 1,       None, None, None],
]

HARDEST = [
    [8,    None, None,    None, None, None,    None, None, None],
    [None, None, 3,       6,    None, None,    None, None, None],
    [None, 7,    None,    None, 9,    None,    2,    None, None],

    [None, 5,    None,    None, None, 7,       None, None, None],
    [None, None, None,    None, 4,    5,       7,    None, None],
    [None, None, None,    1,    None, None,    None, 3,    None],

    [None, None, 1,       None, None, None,    None, 6,    8],
    [None, None, 8,       5,    None, None,    None, 1,    None],
    [None, 9,    None,    None, None, None,    4,    None, None],
]


CORRECT = [
    [8, 3, 2,   1, 5, 9,   4, 7, 6],
    [5, 4, 6,   2, 7, 8,   3, 9, 1],
    [9, 7, 1,   3, 4, 6,   5, 8, 2],

    [1, 8, 3,   6, 9, 5,   7, 2, 4],
    [7, 5, 9,   4, 2, 1,   6, 3, 8],
    [6, 2, 4,   7, 8, 3,   1, 5, 9],

    [3, 9, 7,   8, 1, 4,   2, 6, 5],
    [4, 6, 5,   9, 3, 2,   8, 1, 7],
    [2, 1, 8,   5, 6, 7,   9, 4, 3],
]

INCORRECT = [
    [8, 3, 2,   1, 5, 9,   4, 7, 6],  # <- 0:2 is wrong (2)
    [5, 4, 6,   2, 7, 8,   3, 9, 1],  # <- 1:1 is wrong (4)
    [9, 7, 1,   3, 4, 6,   5, 8, 2],

    [1, 8, 3,   6, 9, 5,   7, 2, 4],
    [7, 5, 9,   4, 2, 1,   6, 3, 8],
    [6, 4, 2,   7, 8, 3,   1, 5, 9],  # <- 5:1 (4) and 5:2 (2) are wrong

    [3, 9, 7,   8, 1, 4,   2, 6, 5],
    [4, 6, 5,   9, 3, 2,   8, 1, 7],
    [2, 1, 8,   5, 6, 7,   9, 4, 3],
]

IMPOSSIBLE = [
    [8,    3,    None,    1,    5,    9,       4,    7,    6],
    [5,    4,    6,       2,    7,    8,       3,    9,    1],
    [9,    7,    1,       3,    4,    6,       5,    8,    2],

    [1,    8,    3,       6,    9,    5,       7,    2,    4],
    [7,    5,    9,       4,    2,    1,       6,    3,    8],
    [6,    None, 2,       7,    8,    3,       1,    5,    9],

    [3,    9,    7,       8,    1,    4,       2,    6,    5],
    [4,    6,    5,       9,    3,    2,       8,    1,    7],
    [2,    1,    8,       5,    6,    7,       9,    4,    3],
]

EASY_4x4 = [
    [3,    4,     1,    None],
    [None, 2,     None, None],

    [None, None,  2,    None],
    [None, 1,     4,    3],
]

EASY_16x16 = [
    [None, 3,    None, 13,     5,    None, None, 2,      4,    None, None, 12,     10,   None, 1,    None],
    [None, None, 10,   9,      None, 7,    13,   None,   None, 1,    11,   None,   14,   12,   None, None],
    [2,    None, None, None,   None, 12,   None, 1,      14,   None, 8,    None,   None, None, None, 11],
    [12,   1,    6,    7,      4,    None, 14,   9,      16,   3,    None, 10,     8,    2,    5,    13],

    [None, 12,   None, 2,      None, 8,    None, None,   None, None, 3,    None,   6,    None, 10,   None],
    [None, 5,    15,   None,   7,    2,    None, None,   None, None, 6,    9,      None, 8,    3,    None],
    [10,   None, 9,    None,   None, 6,    4,    3,      15,   8,    16,   None,   None, 7,    None, 12],
    [None, None, 3,    8,      13,   None, None, 10,     1,    None, None, 7,      5,    16,   None, None],

    [None, None, 12,   5,      None, 3,    6,    None,   None, 4,    7,    None,   9,    14,   None, None],
    [None, None, 13,   None,   16,   14,   None, None,   None, None, 12,   1,      None, 11,   None, None],
    [9,    6,    1,    None,   15,   None, None, 12,     8,    None, None, 14,     None, 10,   7,    3],
    [None, 7,    14,   None,   None, 1,    None, 4,      6,    None, 13,   None,   None, 5,    16,   None],

    [7,    None, 16,   None,   None, 10,   None, None,   None, None, 4,    None,   None, 13,   None, 8],
    [1,    13,   None, 11,     None, None, 15,   None,   None, 2,    None, None,   16,   None, 9,    10],
    [15,   None, 2,    None,   None, 4,    None, 7,      3,    None, 10,   None,   None, 6,    None, 5],
    [None, 10,   8,    None,   2,    9,    3,    None,   None, 16,   1,    11,     None, 4,    15,   None],
]

INVALID_BOARD_NOT_SQUARE_OF_INTEGER = [
    [None, 1,    None, 4,    5],
    [None, None, None, None, None],
    [2,    None, None, None, None],
    [None, None, 5,    None, 2],
    [None, None, None, 1,    None],
]

INVALID_BOARD_NOT_SQUARE_SHAPE = [
    [None, 1,    None, 4],
    [None, None, None, None],
    [2,    None, None, None, None],  # <- 5 elements instead of 4
    [4,    3,    None, None],
]

INVALID_BOARD_INVALID_VALUE = [
    [None, 3,    2,       1,    5,    9,       None, None, None],
    [None, None, None,    2,    None, None,    None, 9,    None],
    [9,    None, None,    None, 4,    None,    5,    8,    None],

    [None, 8,    3,       6,    9,    None,    7,    None, None],
    [None, 5,    9,       None, None, None,    6,    3,    None],
    [None, None, 4,       None, 8,    3,       1,    5,    None],

    [None, 9,    7,       None, 1,    None,    None, None, 5],
    [None, 6,    None,    None, None, 2,       None, None, None],
    [None, None, None,    12,   6,    7,       9,    4,    None],  # <- 12 is not a valid value
]


class TestSudoku(unittest.TestCase):

    def setUp(self):
        self.hardest = Sudoku(HARDEST)
        self.easy = Sudoku(EASY)
        self.medium = Sudoku(MEDIUM)
        self.hard = Sudoku(HARD)
        self.evil = Sudoku(EVIL)
        self.correct = Sudoku(CORRECT)
        self.incorrect = Sudoku(INCORRECT)
        self.impossible = Sudoku(IMPOSSIBLE)
        self.easy_4x4 = Sudoku(EASY_4x4)
        self.easy_16x16 = Sudoku(EASY_16x16)

    # __init__
    def test_init_board_not_square_of_integer(self):
        with self.assertRaises(sudoku.MalformedBoard):
            Sudoku(INVALID_BOARD_NOT_SQUARE_OF_INTEGER)

    def test_init_board_not_square_shape(self):
        with self.assertRaises(sudoku.MalformedBoard):
            Sudoku(INVALID_BOARD_NOT_SQUARE_SHAPE)

    def test_init_board_invalid_value(self):
        with self.assertRaises(sudoku.MalformedBoard):
            Sudoku(INVALID_BOARD_INVALID_VALUE)

    # valid_values
    def test_valid_values_4x4(self):
        self.assertEqual(self.easy_4x4.valid_values(), set([1, 2, 3, 4]))

    def test_valid_values_9x9(self):
        self.assertEqual(self.easy.valid_values(), set([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_valid_values_16x16(self):
        self.assertEqual(
            self.easy_16x16.valid_values(),
            set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        )

    # modifiable
    def test_modifiable_true(self):
        self.assertTrue(self.easy.modifiable(0, 0))

    def test_modifiable_false(self):
        self.assertFalse(self.easy.modifiable(0, 1))

    # correct
    def test_not_fully_filled(self):
        self.assertFalse(self.easy.correct())

    def test_incorrect(self):
        self.assertFalse(self.incorrect.correct())

    def test_correct(self):
        self.assertTrue(self.correct.correct())

    # square_coordinates
    def test_9x9_00(self):
        self.assertEqual(
            list(self.easy.square_coordinates(2, 1)),
            [
                (0, 0), (0, 1), (0, 2),
                (1, 0), (1, 1), (1, 2),
                (2, 0), (2, 1), (2, 2),
            ]
        )

    def test_9x9_11(self):
        self.assertEqual(
            list(self.easy.square_coordinates(3, 3)),
            [
                (3, 3), (3, 4), (3, 5),
                (4, 3), (4, 4), (4, 5),
                (5, 3), (5, 4), (5, 5),
            ]
        )

    def test_16x16_78(self):
        self.assertEqual(
            list(self.easy_16x16.square_coordinates(7, 8)),
            [
                (4, 8), (4, 9), (4, 10), (4, 11),
                (5, 8), (5, 9), (5, 10), (5, 11),
                (6, 8), (6, 9), (6, 10), (6, 11),
                (7, 8), (7, 9), (7, 10), (7, 11),
            ]
        )

    # possibilities
    def test_single_possibility(self):
        self.assertEqual(self.correct.possibilities(0, 0), set([8]))

    def test_no_possibility(self):
        self.assertEqual(self.incorrect.possibilities(0, 2), set())

    def test_multiple_possibilities(self):
        self.assertEqual(self.easy.possibilities(0, 0), set([4, 6, 7, 8]))

    # __str__
    def test_str_not_fully_filled(self):
        self.assertEqual(str(self.easy), '\n'.join([
            '+-------+-------+-------+',
            '|   3 2 | 1 5 9 |       |',
            '|       | 2     |   9   |',
            '| 9     |   4   | 5 8   |',
            '+-------+-------+-------+',
            '|   8 3 | 6 9   | 7     |',
            '|   5 9 |       | 6 3   |',
            '|     4 |   8 3 | 1 5   |',
            '+-------+-------+-------+',
            '|   9 7 |   1   |     5 |',
            '|   6   |     2 |       |',
            '|       | 5 6 7 | 9 4   |',
            '+-------+-------+-------+',
        ]))

    def test_str_fully_filled(self):
        self.assertEqual(str(self.correct), '\n'.join([
            '+-------+-------+-------+',
            '| 8 3 2 | 1 5 9 | 4 7 6 |',
            '| 5 4 6 | 2 7 8 | 3 9 1 |',
            '| 9 7 1 | 3 4 6 | 5 8 2 |',
            '+-------+-------+-------+',
            '| 1 8 3 | 6 9 5 | 7 2 4 |',
            '| 7 5 9 | 4 2 1 | 6 3 8 |',
            '| 6 2 4 | 7 8 3 | 1 5 9 |',
            '+-------+-------+-------+',
            '| 3 9 7 | 8 1 4 | 2 6 5 |',
            '| 4 6 5 | 9 3 2 | 8 1 7 |',
            '| 2 1 8 | 5 6 7 | 9 4 3 |',
            '+-------+-------+-------+',
        ]))

    def test_str_16x16_not_fully_filled(self):
        self.assertEqual(str(self.easy_16x16), '\n'.join([
            '+-------------+-------------+-------------+-------------+',
            '|     3    13 |  5        2 |  4       12 | 10     1    |',
            '|       10  9 |     7 13    |     1 11    | 14 12       |',
            '|  2          |    12     1 | 14     8    |          11 |',
            '| 12  1  6  7 |  4    14  9 | 16  3    10 |  8  2  5 13 |',
            '+-------------+-------------+-------------+-------------+',
            '|    12     2 |     8       |        3    |  6    10    |',
            '|     5 15    |  7  2       |        6  9 |     8  3    |',
            '| 10     9    |     6  4  3 | 15  8 16    |     7    12 |',
            '|        3  8 | 13       10 |  1        7 |  5 16       |',
            '+-------------+-------------+-------------+-------------+',
            '|       12  5 |     3  6    |     4  7    |  9 14       |',
            '|       13    | 16 14       |       12  1 |    11       |',
            '|  9  6  1    | 15       12 |  8       14 |    10  7  3 |',
            '|     7 14    |     1     4 |  6    13    |     5 16    |',
            '+-------------+-------------+-------------+-------------+',
            '|  7    16    |    10       |        4    |    13     8 |',
            '|  1 13    11 |       15    |     2       | 16     9 10 |',
            '| 15     2    |     4     7 |  3    10    |     6     5 |',
            '|    10  8    |  2  9  3    |    16  1 11 |     4 15    |',
            '+-------------+-------------+-------------+-------------+',
        ]))

    # solve
    def test_solve_easy(self):
        solved = sudoku.solve(self.easy)
        self.assertTrue(solved.correct())

    def test_solve_medium(self):
        solved = sudoku.solve(self.medium)
        self.assertTrue(solved.correct())

    def test_solve_hard(self):
        solved = sudoku.solve(self.hard)
        self.assertTrue(solved.correct())

    def test_solve_evil(self):
        solved = sudoku.solve(self.evil)
        self.assertTrue(solved.correct())

    def test_solve_hardest(self):
        solved = sudoku.solve(self.hardest)
        self.assertTrue(solved.correct())

    def test_solve_impossible(self):
        self.assertIsNone(sudoku.solve(self.impossible))

    def test_solve_easy_16x16(self):
        solved = sudoku.solve(self.easy_16x16)
        self.assertTrue(solved.correct())
