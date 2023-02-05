class SudokuSolver:
    """The solver uses a list of Moves that wrap around empty tiles.
    Tiles are looped through [1-9] until a valid number is found that
    does not break the rules of the sudoku. This process begins at the
    first tile. If a tiles loops through all 9 numbers, and they are
    all invalid, then we go back a tile and increment it instead.

    If this process can continue until the end successfully, then a
    solution has been found. If the first tile loops through all 9
    values then a solution is not possible at all.
    """
    class Move:
        """The Move class handles the blank tiles. It cycles through the
        numbers [1-9] inside the tile.

        Raises:
            ValueError: If the tile hasn't got None for its number
        """
        def __init__(self, tile):
            if tile.get_number() is not None:
                raise ValueError("Moves can only be done to tiles with no number")

            self.tile = tile

        def get_tile(self):
            return self.tile
        
        def next_number(self):
            current_number = self.tile.get_number()

            if current_number is None:
                self.tile.set_number(1)
                return True
            
            current_number += 1
            if current_number > 9:
                self.tile.set_number(None)
                return False
            self.tile.set_number(current_number)
            return True
        
        def reset(self):
            self.tile.set_number(None)

    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.moves = []
        
        # The moves are premade and reset whenever not being used. This
        # approach does not use a Stack which is likely a popular
        # technique for other programmers solving this problem.
        for tile in sudoku:
            if tile.get_number() is None:
                self.moves.append(self.Move(tile))

    def solve(self):
        """Call solve to return the resultant finished Sudoku. This
        method returns None if no solution can be found. It also
        prints to the terminal an Error message.
        """
        if not self.sudoku.is_currently_correct():
            print("The Sudoku is not possible to solve from initial values")
            return None

        counter = 0
        while True:
            # Check if we found a solution, or can't find a solution
            if counter >= len(self.moves):
                return self.sudoku
            elif counter < 0:
                print("The Sudoku is not possible to solve")
                return None
            
            current_move = self.moves[counter]

            # Try the next number for the tile
            if current_move.next_number():
                row = current_move.get_tile().get_row()
                col = current_move.get_tile().get_col()
                square = (row // 3, col // 3)

                groups = [
                    self.sudoku.get_row(row),
                    self.sudoku.get_col(col),
                    self.sudoku.get_square(*square)
                ]

                # Is this move legit?
                results = [Sudoku.is_grouping_possible(group) for group in groups]

                # No. Try a new number
                if False in results:
                    continue

                # Yes. Try the next number
                counter += 1
            else:
                # This move is invalid with all numbers [1-9]
                counter -= 1


class Sudoku:
    @staticmethod
    def is_grouping_possible(group):
        """This static method checks to see whether the given group list has two 
        (non-None) numbers that are the same. If so, return False. Otherwise,
        return True.

        Args:
            group (list): The line to check (row, column, or, 3x3 square)
        """
        numbers = list(map(lambda tile: tile.get_number(), group))
        numbers_no_none = list(filter(lambda n: n is not None, numbers))
        numbers_no_dups = set(numbers_no_none)
        return len(numbers_no_none) == len(numbers_no_dups)

    class Tile:
        def __init__(self, row, col, number):
            """Represents a tile in the Sudoku

            Args:
                row (int): Row index in the sudoku
                col (int): Column index in the sudoku
                number (int): Number associated with this tile
            """
            self.row = row
            self.col = col
            if number == "0":
                self.number = None
            else:
                self.number = int(number)
            
        def __repr__(self):
            if self.number is None:
                return " "
            return str(self.number)
        
        def set_number(self, number):
            self.number = number
            return self

        def get_number(self):
            return self.number
        
        def get_row(self):
            return self.row
        
        def get_col(self):
            return self.col

    def __init__(self, tile_data):
        """Generates the tiles inside the Sudoku. Yes I used an inner class
        for tiles. Don't hate me.

        Args:
            tile_data (str): 
                See https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Sudoku_Puzzle_by_L2G-20050714_standardized_layout.svg/1200px-Sudoku_Puzzle_by_L2G-20050714_standardized_layout.svg.png)
                Reading each row left to right and write the number that appears. Write gaps as a 0.
                The above Sudoku is:
                "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
        """
        self.tiles = [[None for __ in range(9)] for _ in range(9)]

        for row in range(9):
            for col in range(9):
                number = tile_data[(row * 9) + col]
                self.tiles[row][col] = self.Tile(row, col, number)
    
    def __str__(self):
        """Shows the Sudoku board. Not very clean but gets the job done
        """
        horizontal_line = "-" * ((3 * 5) + 4) + "\n"
        output = ""
        for i, row in enumerate(self.tiles):
            if ((i+0) % 3 == 0):
                output += horizontal_line

            output += "|"
            for j in range(9):
                if ((j+1) % 3 == 0):
                    output += str(row[j]) + "|"
                else:
                    output += str(row[j]) + " "
            output += "\n"
        output += horizontal_line
        return output
    
    def __iter__(self):
        self.iter = 0
        return self

    def __next__(self):
        if (self.iter >= 9 * 9):
            raise StopIteration
        row = self.iter // 9
        col = self.iter % 9
        tile = self.tiles[row][col]
        self.iter += 1
        return tile
    
    def get_row(self, index):
        """Returns the row at the specified index.

        Args:
            index (int): Must be [0-9)

        Raises:
            IndexError: If the row goes out of bounds
        Returns:
            list: The group of numbers in the row
        """
        if (index < 0 or index >= 9):
            raise IndexError
        
        return self.tiles[index]
    
    def get_col(self, index):
        """Returns the column at the specified index.

        Args:
            index (int): Must be [0-9)

        Raises:
            IndexError: If the column goes out of bounds
        Returns:
            list: The group of numbers in the column
        """
        if (index < 0 or index >= 9):
            raise IndexError
        
        col = []
        for row in self.tiles:
            col.append(row[index])
        return col
    
    def get_square(self, row, col):
        """Returns the 3x3 square at the specified row and column indices.

        Args:
            row (int): Must be [0-3)
            col (int): Must be [0-3)

        Raises:
            IndexError: If the row or column goes out of bounds

        Returns:
            list: The group of numbers in the square
        """
        if (row < 0 or row >= 3):
            raise IndexError
        if (col < 0 or col >= 3):
            raise IndexError
        
        square = []
        for i in range(3 * row, 3 * row + 3):
            for j in range(3 * col, 3 * col + 3):
                square.append(self.tiles[i][j])
        return square
    
    def is_currently_correct(self):
        """Used to check if the current configuration of the board is valid.
        If checking that a move is valid, it is faster to not check the entire
        board, but only the groups that are affected by the move.

        A return of True does not mean that the Sudoku is solved. It also does
        not mean that a solution exists. It should only be used to check that
        the input Sudoku is legitimate.

        Returns:
            bool: True if the board is in a naively solvable configuration.
        """
        all_groups = []
        for i in range(9):
            all_groups.append(game.get_row(i))
            all_groups.append(game.get_col(i))

        for i in range(3):
            for j in range(3):
                all_groups.append(game.get_square(i, j))
        
        results = [Sudoku.is_grouping_possible(group) for group in all_groups]
        return False not in results
    

if __name__ == "__main__":
    board_data = [
        "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
        # "534070000627195000198000060800060003400803001700020006060000280000419005000080079",
        # "110000000000000000000000000000000000000000000000000000000000000000000000000000000",
        # "300000009000070102000009500070050000100400680006000000710090005000003800400000020",
        # "000092370800000000060800400700000832090000005000500100006001000030060050005007000",
        # "000000000000000000000000000000000000000000000000000000000000000000000000000000001"
    ]
    
    for i, data in enumerate(board_data):
        # print("Game #{}".format(i + 1))
        game = Sudoku(data)
        # print("Board:")
        # print(game)
        # print("Solution:")
        print(SudokuSolver(game).solve())
        # print("--------------------------------------------------------------------")