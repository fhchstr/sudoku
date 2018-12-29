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

HARDEST = [
    [8,    None, None,    None, None, None,    None, None, None],
    [None, None, 3,       6,    None, None,    None, None, None],
    [None, 7,    None,    None, 9,    None,    2,    None, None],

    [None, 5,    None,    None, None, 7,       None, None, None],
    [None, None, None,    None, 4,    5,       7,    None, None],
    [None, None, None,    1,    None, None,    None, 3,    None],

    [None, None, 1,       None, None, None,    None, 6,    8   ],
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


EASY_16x16 = [
    [None, 3,    None, 13,     5,    None, None, 2,      4,    None, None, 12,     10,   None, 1,    None],
    [None, None, 10,   9,      None, 7,    13,   None,   None, 1,    11,   None,   14,   12,   None, None],
    [2,    None, None, None,   None, 12,   None, 1,      14,   None, 8,    None,   None, None, None, 11  ],
    [12,   1,    6,    7,      4,    None, 14,   9,      16,   3,    None, 10,     8,    2,    5,    13  ],

    [None, 12,   None, 2,      None, 8,    None, None,   None, None, 3,    None,   6,    None, 10,   None],
    [None, 5,    15,   None,   7,    2,    None, None,   None, None, 6,    9,      None, 8,    3,    None],
    [10,   None, 9,    None,   None, 6,    4,    3,      15,   8,    16,   None,   None, 7,    None, 12  ],
    [None, None, 3,    8,      13,   None, None, 10,     1,    None, None, 7,      5,    16,   None, None],

    [None, None, 12,   5,      None, 3,    6,    None,   None, 4,    7,    None,   9,    14,   None, None],
    [None, None, 13,   None,   16,   14,   None, None,   None, None, 12,   1,      None, 11,   None, None],
    [9,    6,    1,    None,   15,   None, None, 12,     8,    None, None, 14,     None, 10,   7,    3   ],
    [None, 7,    14,   None,   None, 1,    None, 4,      6,    None, 13,   None,   None, 5,    16,   None],

    [7,    None, 16,   None,   None, 10,   None, None,   None, None, 4,    None,   None, 13,   None, 8   ],
    [1,    13,   None, 11,     None, None, 15,   None,   None, 2,    None, None,   16,   None, 9,    10  ],
    [15,   None, 2,    None,   None, 4,    None, 7,      3,    None, 10,   None,   None, 6,    None, 5   ],
    [None, 10,   8,    None,   2,    9,    3,    None,   None, 16,   1,    11,     None, 4,    15,   None],
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
        self.easy_16x16 = Sudoku(EASY_16x16)

    # __init__
    # TODO

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

    # possibilities
    def test_single_possibility(self):
        self.assertEqual(self.correct.possibilities(0, 0), set([8]))

    def test_no_possibility(self):
        self.assertEqual(self.incorrect.possibilities(0, 2), set())

    def test_multiple_possibilities(self):
        self.assertEqual(self.easy.possibilities(0, 0), set([4, 6, 7, 8]))

    # __str__
    # TODO

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
