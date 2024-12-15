# This program visualizes the runtime performance of solving the Opponent Avoidance Problem 
# using exhaustive search. It generates all possible paths and checks which ones are valid,
# demonstrating the exponential complexity of this approach.

import time
import random
import matplotlib.pyplot as plt

def generate_grid(n, blocked_ratio=0.2):
    """
    Generates a random nxn grid with approximately blocked_ratio percentage of cells blocked.
    Ensures start and end positions are always open.
    """
    grid = [['.' for _ in range(n)] for _ in range(n)]
    num_blocks = int(n * n * blocked_ratio)
    positions = [(i, j) for i in range(n) for j in range(n)]
    positions.remove((0, 0))
    positions.remove((n-1, n-1))
    blocked_positions = random.sample(positions, num_blocks)
    for x, y in blocked_positions:
        grid[x][y] = 'X'
    return grid

def soccer_exhaustive(G):
    """
    Solves the Opponent Avoidance Problem using exhaustive search.
    Generates all possible paths and checks which ones are valid.
    Time complexity: O(2^(r+c-2)) where r,c are grid dimensions
    """
    r = len(G)
    c = len(G[0])
    n = r + c - 2  # Total moves needed to reach bottom-right
    counter = 0

    # Generate all possible combinations of right/down moves
    for bits in range(2**n):
        candidate = []
        
        # Convert binary number to sequence of moves
        # 1 represents right move, 0 represents down move
        for k in range(n):
            bit = (bits >> k) & 1
            if bit == 1:
                candidate.append("→")
            else:
                candidate.append("↓")

        # Validate the candidate path
        x, y = 0, 0  # Start at top-left
        valid = True

        # Follow the path and check for validity
        for move in candidate:
            if move == "→":
                y += 1
            else:
                x += 1

            # Path is invalid if it goes outside grid or hits obstacle
            if not (0 <= x < r and 0 <= y < c) or G[x][y] == 'X':
                valid = False
                break

        # Count path if it's valid and reaches the target
        if valid and (x, y) == (r-1, c-1):
            counter += 1

    return counter

def measure_runtime(grid_sizes):
    """
    Measures runtime for different grid sizes and returns data for plotting.
    Uses smaller grid sizes due to exponential complexity.
    """
    instance_sizes = []
    elapsed_times = []

    for size in grid_sizes:
        grid = generate_grid(size, blocked_ratio=0.2)
        start_time = time.perf_counter()
        paths = soccer_exhaustive(grid)
        end_time = time.perf_counter()

        n = size * size  # Instance size is area of grid
        elapsed_time = end_time - start_time
        instance_sizes.append(n)
        elapsed_times.append(elapsed_time)

        print(f"Grid size: {size}x{size}, Paths: {paths}, Elapsed time: {elapsed_time:.4f}s")
    
    return instance_sizes, elapsed_times

if __name__ == "__main__":
    # Use smaller grid sizes due to exponential complexity
    grid_sizes = [2,3,4,5,6,7,8,9,10,11,12]

    # Collect runtime data
    ex_sizes, ex_times = measure_runtime(grid_sizes)

    # Create visualization
    plt.figure(figsize=(10, 6))
    plt.scatter(ex_sizes, ex_times, marker='o', s=100, edgecolor='k', label="Exhaustive Search")
    plt.title("Runtime of Exhaustive Search")
    plt.xlabel("Instance Size (n = r × c)")
    plt.ylabel("Elapsed Time (seconds)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()