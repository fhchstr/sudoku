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

    [None, 9,    7,       None, 1,    None,    None, None, 5   ],
    [None, 6,    None,    None, None, 2,       None, None, None],
    [None, None, None,    5,    6,    7,       9,    4,    None],
]

MEDIUM = [
    [2,    None, None,    None, None, 1,       None, None, 5   ],
    [None, None, None,    None, 9,    6,       None, 8,    None],
    [None, None, 5,       7,    2,    None,    None, None, 9   ],

    [None, 5,    None,    None, None, None,    None, 9,    None],
    [None, 8,    7,       None, None, None,    1,    4,    None],
    [None, 9,    None,    None, None, None,    None, 3,    None],

    [3,    None, None,    None, 6,    5,       4,    None, None],
    [None, 2,    None,    1,    3,    None,    None, None, None],
    [9,    None, None,    8,    None, None,    None, None, 3   ],
]

HARD = [
    [None, 7,    2,       9,    None, None,    3,    None, 8,  ],
    [None, 8,    None,    None, 5,    None,    1,    None, None],
    [None, None, None,    7,    None, None,    4,    None, None],

    [2,    None, None,    None, None, None,    None, 7,    None],
    [6,    None, None,    8,    None, 5,       None, None, 4   ],
    [None, 1,    None,    None, None, None,    None, None, 9   ],

    [None, None, 5,       None, None, 1,       None, None, None],
    [None, None, 1,       None, 6,    None,    None, 4,    None],
    [7,    None, 6,       None, None, 8,       9,    2,    None],
]

EVIL = [
    [None, None, None,    1,    None, None,    8,    None, 2   ],
    [None, None, 7,       8,    None, None,    9,    None, None],
    [None, 8,    1,       9,    None, 3,       None, None, None],

    [8,    None, None,    6,    None, None,    None, None, None],
    [None, 4,    None,    None, None, None,    None, 5,    None],
    [None, None, None,    None, None, 7,       None, None, 9   ],

    [None, None, None,    3,    None, 2,       6,    7,    None],
    [None, None, 6,       None, None, 9,       1,    None, None],
    [5,    None, 3,       None, None, 1,       None, None, None],
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


class TestSudoku(unittest.TestCase):

    def setUp(self):
        self.easy = Sudoku(EASY)
        self.medium = Sudoku(MEDIUM)
        self.hard = Sudoku(HARD)
        self.evil = Sudoku(EVIL)
        self.correct = Sudoku(CORRECT)
        self.incorrect = Sudoku(INCORRECT)

    # __init__
    # TODO

    # get
    def test_get_unset(self):
        self.assertIs(self.easy.get(0, 0), None)

    def test_get_value(self):
        self.assertEqual(self.easy.get(0, 1), 3)

    # set
    def test_set_valid(self):
        self.easy.set(1, 0, 0)
        self.assertEqual(self.easy.get(0, 0), 1)

    def test_set_invalid(self):
        with self.assertRaises(ValueError):
            self.easy.set(0, 0, 0)

    def test_set_on_unmodifiable(self):
        with self.assertRaises(sudoku.UnmodifiableCell):
            self.easy.set(1, 0, 1)

    # unset
    def test_unset_valid(self):
        self.easy.unset(0, 0)
        self.assertIs(self.easy.get(0, 0), None)

    def test_unset_on_unmodifiable(self):
        with self.assertRaises(sudoku.UnmodifiableCell):
            self.easy.unset(0, 1)

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
            list(self.easy.square_coordinates(2,1)),
            [
                (0, 0), (0, 1), (0, 2),
                (1, 0), (1, 1), (1, 2),
                (2, 0), (2, 1), (2, 2),
            ]
        )

    def test_9x9_11(self):
        self.assertEqual(
            list(self.easy.square_coordinates(3,3)),
            [
                (3, 3), (3, 4), (3, 5),
                (4, 3), (4, 4), (4, 5),
                (5, 3), (5, 4), (5, 5),
            ]
        )

    # solve
    def test_solve_easy(self):
        solved = self.easy.solve() 
        self.assertTrue(solved.correct())

    def test_solve_medium(self):
        solved = self.medium.solve() 
        self.assertTrue(solved.correct())

    def test_solve_hard(self):
        solved = self.hard.solve() 
        self.assertTrue(solved.correct())

    def test_solve_evil(self):
        solved = self.evil.solve() 
        self.assertTrue(solved.correct())

    # possibilities
    def test_single_possibility(self):
        self.assertEqual(self.correct.possibilities(0, 0), set([8]))

    def test_no_possibility(self):
        self.assertEqual(self.incorrect.possibilities(0, 2), set())

    def test_multiple_possibilities(self):
        self.assertEqual(self.easy.possibilities(0, 0), set([4, 6, 7, 8]))

    # __str__
    # TODO