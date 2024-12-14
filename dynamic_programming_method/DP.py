def soccer_dyn_prog(grid):
    # Get the number of rows and columns
    row, col = len(grid), len(grid[0])

    # Corner case: initial cell is impassible
    if grid[0][0] == 'X' or grid[row - 1][col - 1] == 'X':
        return 0

    # Initialize the DP grid with zeroes
    dp = [[0 for _ in range(col)] for _ in range(row)]

    # Base case
    dp[0][0] = 1
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 'X':  
                dp[i][j] = 0
                continue

            # From above
            if i > 0:
                dp[i][j] += dp[i - 1][j]

            # From the left
            if j > 0:
                dp[i][j] += dp[i][j - 1]

    return dp[row - 1][col - 1]


grid_example = [
    ['.', '.', '.', '.', '.', '.', 'X', '.', 'X'],
    ['X', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'X', '.', '.', '.', 'X', '.'],
    ['.', '.', 'X', '.', '.', '.', '.', 'X', '.'],
    ['.', 'X', '.', '.', '.', '.', 'X', '.', '.'],
    ['.', '.', '.', '.', 'X', '.', '.', '.', '.'],
    ['.', '.', 'X', '.', '.', '.', '.', '.', 'X'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.']
]

ans = soccer_dyn_prog(grid_example)
print(f"Number of different paths: {ans}")
