import math


class Sudoku(object):

    def __init__(self, board):
        if not math.sqrt(len(board)).is_integer():
            raise MalformedBoard('The square root of the board\'s size must be an integer')

        self.board_size = len(board)
        self.values_per_square = int(math.sqrt(self.board_size))
        self.board = [[None] * self.board_size for _ in xrange(self.board_size)]
        # Coordinates of the cells which contain a value during the object's instantiation
        self.unmodifiable_cells = set()

        # Make sure the board is valid and initialize the instance variables with its content
        for row in xrange(self.board_size):
            if not len(board[row]) == self.board_size:
                raise MalformedBoard('The board must be a square ({0}x{0})'.format(self.board_size))
            for column in xrange(self.board_size):
                value = board[row][column]
                if value:
                    if value not in self.valid_values():
                        raise MalformedBoard('{} is not a valid value'.format(value))
                    self.unmodifiable_cells.add((row, column))
                self.board[row][column] = value

        # Those coordinates are computed at object's initilization because the correct() method,
        # which is called thousands of times during the brute-force resolution of the sudoku, needs it
        self.top_left_corner_of_squares = set()
        square_steps = range(0, self.board_size, self.values_per_square)
        for square_top_row in square_steps:
            for square_left_column in square_steps:
                self.top_left_corner_of_squares.add((square_top_row, square_left_column))

    def valid_values(self):
        """Return the values allowed given the board size."""
        return {v for v in xrange(1, self.board_size + 1)}

    def modifiable(self, row, column):
        """Return True if the cell at the given coordinates is modifiable."""
        return (row, column) not in self.unmodifiable_cells

    def correct(self):
        """Return True if the Sudoku is correct."""
        # Return False if any row/column doesn't contain all the values
        for i in xrange(self.board_size):
            row_values = set(self.board[i])
            column_values = {self.board[row][i] for row in xrange(self.board_size)}
            if not row_values == column_values == self.valid_values():
                return False

        # Return False if any square doesn't contain all the values
        for top_left_corner in self.top_left_corner_of_squares:
            square_values = {self.board[r][c] for r, c in self.square_coordinates(*top_left_corner)}
            if square_values != self.valid_values():
                return False

        return True

    def square_coordinates(self, row, column):
        """Return the coordinates of the cells in the square in which the given coordinates are."""
        top_row = row // self.values_per_square * self.values_per_square
        left_column = column // self.values_per_square * self.values_per_square

        for row_in_square in xrange(top_row, top_row + self.values_per_square):
            for column_in_square in xrange(left_column, left_column + self.values_per_square):
                yield row_in_square, column_in_square

    def possibilities(self, row, column):
        """Return the valid possibilities for a given coordinate."""
        p = self.valid_values()

        for i in xrange(self.board_size):
            if i != column:
                p.discard(self.board[row][i])
            if i != row:
                p.discard(self.board[i][column])

        for r, c in self.square_coordinates(row, column):
            if r != row and c != column:
                p.discard(self.board[r][c])

        return p

    def __str__(self):
        # Find the largest width of the values's string representation
        value_width = max([len(str(v)) for v in self.valid_values()])
        # Space between the square border and the values (1 on each side) -----------------+
        # Space between the values ----------------------------------------+               |
        # Space to display the values --+                                  |               |
        #              +----------------+-----------------+   +------------+-----------+   |
        #              |                                  |   |                        |   |
        square_width = self.values_per_square * value_width + self.values_per_square - 1 + 2
        # A horizontal line is composed of lines made of dashes ('-') the same width as the squares
        # Between each square, the dash is replaced by a plus sign ('+')
        # The number of squares on a row is the same as the number of values in a square
        horizontal_line = '+' + '+'.join(['-' * square_width] * self.values_per_square) + '+'
        # Right alligned with fixed width
        fmt = '{:>%d}' % value_width

        lines = []
        for row_index, row in enumerate(self.board):
            if row_index % self.values_per_square == 0:
                lines.append(horizontal_line)

            values = []
            for column_index, cell in enumerate(row):
                if column_index % self.values_per_square == 0:
                    values.append('|')
                values.append(fmt.format(cell) if cell else ' ' * value_width)

            values.append('|')
            lines.append(' '.join(values))

        lines.append(horizontal_line)
        return '\n'.join(lines)


def solve(sudoku):
    """Return a new solved Sudoku instance. Return None if no solution exist."""
    def solve_recursive(sudoku, row=0, column=0):
        if sudoku.correct():
            return sudoku

        # We tried everything and couldn't solve the sudoku
        if row is None or column is None:
            return None

        # Compute the next coordinate
        next_row, next_column = row, column
        if column < sudoku.board_size - 1:
            next_column += 1
        elif row < sudoku.board_size - 1:
            next_row += 1
            next_column = 0

        if not sudoku.modifiable(row, column):
            # This cell is not modifiable, go to the next one
            return solve_recursive(sudoku, next_row, next_column)

        for possibility in sudoku.possibilities(row, column):
            # Try each possibility and go to the next cell
            sudoku.board[row][column] = possibility
            result = solve_recursive(sudoku, next_row, next_column)

            if result:
                # Return the solution if we found it
                return result
            else:
                # Clear the cell to make sure the next attempt doesn't take it into account
                sudoku.board[row][column] = None

    return solve_recursive(Sudoku(sudoku.board))


class MalformedBoard(Exception):
    pass
