import math

class Sudoku(object):

    def __init__(self, board):
        self.board_size = len(board)
        if not math.sqrt(self.board_size).is_integer():
            raise MalformedBoard('The square root of the board\'s size must be an integer')

        self.unmodifiable_cells = set()
        self.board = [[None] * self.board_size for _ in xrange(self.board_size)]

        for row in xrange(self.board_size):
            if not len(board[row]) == self.board_size:
                raise MalformedBoard('The board must be a square ({0}x{0})'.format(self.board_size))
            for column in xrange(self.board_size):
                value = board[row][column]
                self.set(value, row, column)
                if value:
                    self.unmodifiable_cells.add((row, column))

    def get(self, row, column):
        """Get the value at the given coordinates."""
        return self.board[row][column]

    def set(self, value, row, column):
        """Set the given value at the given coordinates."""
        if not self.modifiable(row, column):
            raise UnmodifiableCell('The cell {}:{} is not modifiable'.format(row, column))

        cell_value = None
        if value is not None:
            cell_value = int(value)
            if not 1 <= cell_value <= self.board_size:
                raise ValueError('The board values must be from 1 to {}'.format(self.board_size))

        self.board[row][column] = cell_value

    def unset(self, row, column):
        """Set the value to None at the given coordinates."""
        self.set(None, row, column)

    def modifiable(self, row, column):
        """Return True if the cell at the given coordinates is modifiable."""
        return (row, column) not in self.unmodifiable_cells

    # FIXME huge improvement potential
    # instead of checking each cell, we should check each row, column and square. that's it.
    # This also eliminates the need for the _coordinates() method
    def correct(self):
        """Return True if the Sudoku is correct."""
        # Check first if all the rows are filled
        for row, column in self._coordinates():
            if not self.get(row, column):
                return False

        for row, column in self._coordinates():
            value = self.get(row, column)

            # Check the values on the same row/column
            for i in xrange(self.board_size):
                if i != column and self.get(row, i) == value:
                    return False
                if i != row and self.get(i, column) == value:
                    return False

        # Check the values in the same square
        for r, c in self.square_coordinates(row, column):
            if r != row and c != column and self.get(r, c) == value:
                return False

        return True

    def square_coordinates(self, row, column):
        """Return the coordinates of the cells in the square in which the given coordinates are."""
        square_size = int(math.sqrt(self.board_size))
        r = row // square_size * square_size
        c = column // square_size * square_size

        for square_row in xrange(r, r + square_size):
             for square_column in xrange(c, c + square_size):
                 yield square_row, square_column

    def next_coordinates(self, row, column):
        if column < self.board_size - 1:
            return row, column + 1
        elif row < self.board_size - 1:
            return row + 1, 0

        return None, None

    def solve(self):
        """Return a new solved Sudoku instance."""
        return Sudoku._solve_recursive(Sudoku(self.board))

    @staticmethod
    def _solve_recursive(sudoku, row=0, column=0):
        if sudoku.correct():
            return sudoku

        next_row, next_column = sudoku.next_coordinates(row, column)

        if not sudoku.modifiable(row, column):
            # This cell is not modifiable, go to the next one
            return Sudoku._solve_recursive(sudoku, next_row, next_column)

        for possibility in sudoku.possibilities(row, column):
            # Try each possibility and go to the next cell
            sudoku.set(possibility, row, column)

            finished = Sudoku._solve_recursive(sudoku, next_row, next_column)
            if finished:
                # Return the solution if we found it
                return finished
            else:
                # Discard this possibility
                sudoku.unset(row, column)

    def possibilities(self, row, column):
        """Return the valid possibilities for a given coordinate."""
        p = {x for x in xrange(1, self.board_size + 1)}

        for i in xrange(self.board_size):
            if i != column:
                p.discard(self.get(row, i))
            if i != row:
                p.discard(self.get(i, column))
        for r, c in self.square_coordinates(row, column):
            if r != row and c != column:
                p.discard(self.get(r, c))
        return p

    def _coordinates(self):
        """Generator over the coordinates of the Sudoku board."""
        for row in xrange(self.board_size):
            for column in xrange(self.board_size):
                yield row, column

    def __str__(self):
        square_size = int(math.sqrt(self.board_size))
        lines = []
        horizontal_line = '+' + '+'.join(['-' * (2 * square_size + 1)] * square_size) + '+'
        for row_index, row in enumerate(self.board):
            if row_index % square_size == 0:
                lines.append(horizontal_line)

            values = []
            for column_index, cell in enumerate(row):
                if column_index % square_size == 0:
                    values.append('|')
                values.append(str(cell) if cell else ' ')

            values.append('|')
            lines.append(' '.join(values))

        lines.append(horizontal_line)
        return '\n'.join(lines)


class MalformedBoard(Exception):
    pass

class UnmodifiableCell(Exception):
    pass
