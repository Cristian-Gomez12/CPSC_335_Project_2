def soccer_exhaustive(G):
    r = len(G)
    c = len(G[0])
    n = r + c - 2  # the length of path
    counter = 0

    # search all possible path
    for bits in range(2**n):
        candidate = []

        # generate move sequences by generating bit strings
        for k in range(n):
            bit = (bits >> k) & 1
            if bit == 1:
                candidate.append("→")  # move right
            else:
                candidate.append("↓")  # move down

        # check if the candidate path is valid
        x, y = 0, 0
        valid = True

        for move in candidate:
            if move == "→":
                y += 1
            else:
                x += 1

            # check if candidate stays inside the grid and not crossing an 'X'
            if not (0 <= x < r and 0 <= y < c) or G[x][y] == 'X':
                valid = False
                break

        # check if the path ends at the bottom-right corner
        if valid and (x, y) == (r-1, c-1):
            counter += 1

    return counter

# opponent filed
grid = [
    ['.', '.', '.', '.', '.', '.', 'X', '.', 'X'],
    ['X', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'X', '.', '.', '.', 'X', '.'],
    ['.', '.', 'X', '.', '.', '.', '.', 'X', '.'],
    ['.', 'X', '.', '.', '.', '.', 'X', '.', '.'],
    ['.', '.', '.', '.', 'X', '.', '.', '.', '.'],
    ['.', '.', 'X', '.', '.', '.', '.', '.', 'X'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.']
]

result = soccer_exhaustive(grid)
print("The number of valid paths is:", result)
