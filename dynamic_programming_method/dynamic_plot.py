# This program visualizes the runtime performance of solving the Opponent Avoidance Problem 
# using dynamic programming approach. The problem involves finding all possible paths from
# top-left to bottom-right corner of a grid while avoiding obstacles.

import time
import random
import matplotlib.pyplot as plt

def soccer_dyn_prog(grid):
    """
    Solves the Opponent Avoidance Problem using dynamic programming.
    Each cell [i][j] stores the number of possible paths to reach that cell.
    Time complexity: O(n²) where n is the grid size
    """
    row, col = len(grid), len(grid[0])
    # Check if start or end positions are blocked
    if grid[0][0] == 'X' or grid[row-1][col-1] == 'X':
        return 0
    
    # Initialize DP table with zeros
    dp = [[0 for _ in range(col)] for _ in range(row)]
    dp[0][0] = 1  # Base case: one way to reach start position
    
    # Fill DP table: each cell combines paths from above and left
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 'X':
                dp[i][j] = 0  # No paths through obstacles
                continue
            if i > 0:  # Add paths from cell above
                dp[i][j] += dp[i-1][j]
            if j > 0:  # Add paths from cell to the left
                dp[i][j] += dp[i][j-1]
    
    return dp[row-1][col-1]  # Return total paths to bottom-right

def generate_grid(n, blocked_ratio=0.2):
    """
    Generates a random nxn grid with approximately blocked_ratio percentage of cells blocked.
    Ensures start and end positions are always open.
    """
    grid = [['.' for _ in range(n)] for _ in range(n)]
    num_blocks = int(n * n * blocked_ratio)
    positions = [(i, j) for i in range(n) for j in range(n)]
    # Keep start and end positions open
    positions.remove((0, 0))
    positions.remove((n-1, n-1))
    blocked_positions = random.sample(positions, num_blocks)
    for x, y in blocked_positions:
        grid[x][y] = 'X'
    return grid

def measure_runtime(grid_sizes):
    """
    Measures runtime for different grid sizes and returns data for plotting.
    """
    instance_sizes = []
    elapsed_times = []
    
    for size in grid_sizes:
        grid = generate_grid(size)
        start_time = time.perf_counter()
        paths = soccer_dyn_prog(grid)
        end_time = time.perf_counter()
        
        n = size * size  # Instance size is area of grid
        elapsed_time = end_time - start_time
        instance_sizes.append(n)
        elapsed_times.append(elapsed_time)
        
        print(f"Grid size: {size}x{size}, Paths: {paths}, Elapsed time: {elapsed_time:.4f}s")
    
    return instance_sizes, elapsed_times

if __name__ == "__main__":
    # Test with larger grid sizes since DP is efficient enough to handle them
    grid_sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    # Collect runtime data
    dp_sizes, dp_times = measure_runtime(grid_sizes)
    
    # Create visualization
    plt.figure(figsize=(10, 6))
    plt.scatter(dp_sizes, dp_times, marker='o', s=100, edgecolor='k', label="Dynamic Programming")
    
    # Add quadratic fit line to demonstrate O(n²) complexity
    import numpy as np
    x = np.array(dp_sizes)
    z = np.polyfit(x, dp_times, 2)
    p = np.poly1d(z)
    x_line = np.linspace(min(x), max(x), 100)
    plt.plot(x_line, p(x_line), '--', color='r', alpha=0.8, label="Quadratic Fit")
    
    # Configure plot appearance
    plt.title("Runtime of Dynamic Programming Algorithm")
    plt.xlabel("Instance Size (n = r × c)")
    plt.ylabel("Elapsed Time (seconds)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    
    plt.show()