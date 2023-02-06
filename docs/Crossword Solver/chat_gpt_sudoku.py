def solve_sudoku(grid):
    # Loop through the sudoku
    for row in range(9):
        for col in range(9):
            # When we find an empty square, try to change it's
            # value.
            if grid[row][col] == 0:
                # Try changing the value 1 through to 10,
                for num in range(1, 10):
                    # And if it's a valid board then recursively continue
                    # to the solve the next value.
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                    # If the board is not valid then try the next number
                return False
    return True

def is_valid(grid, row, col, num):
    # check row
    for i in range(9):
        if grid[row][i] == num:
            return False

    # check column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # check 3x3 grid
    row_start = row // 3 * 3
    col_start = col // 3 * 3
    for i in range(3):
        for j in range(3):
            if grid[row_start + i][col_start + j] == num:
                return False

    return True

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

if solve_sudoku(grid):
    for row in grid:
        print(row)
else:
    print("No solution exists")