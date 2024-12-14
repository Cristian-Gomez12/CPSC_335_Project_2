import random

def soccer_dyn_prog(grid):
    row, col = len(grid), len(grid[0])
    if grid[0][0] == 'X' or grid[row-1][col-1] == 'X':
        return 0
    dp = [[0 for _ in range(col)] for _ in range(row)]
    dp[0][0] = 1
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 'X':
                dp[i][j] = 0
                continue
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    return dp[row-1][col-1]

def generate_grid(n, blocked_ratio=0.2): # 0.2 = 20% of the grid will be an X (blocked)
    grid = [['.' for _ in range(n)] for _ in range(n)] # grid of .'s
    num_blocks = int(n * n * blocked_ratio)
    for _ in range(num_blocks):
        x, y = random.randint(0, n-1), random.randint(0, n-1) #place a random block in the grid
        grid[x][y] = 'X'
    grid[0][0] = '.'  
    grid[n-1][n-1] = '.' #make sure start and finish are open
    return grid


