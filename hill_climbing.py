from aocd.models import Puzzle
from collections import deque

def bfs(grid, start, end):
    dirs = [
        (0, 1),
        (0, -1),
        (-1, 0),
        (1, 0),
    ]

    seen = set()

    queue = deque([(0,) + start])
    while queue:
        l, i, j = queue.popleft()

        if (i, j) in seen:
            continue

        seen.add((i, j))

        if (i, j) == end:
            return l
            break

        for dx, dy in dirs:
            di = dx + i
            dj = dy + j

            if di < 0 or di >= len(grid) or dj < 0 or dj >= len(grid[0]):
                continue

            if grid[di][dj] <= grid[i][j] + 1:
                queue.append((l+1, di, dj)) 
    
    return float('inf')

def hill_climbing():
    puzzle = Puzzle(year=2022, day=12)
    grid = [[c for c in row] for row in puzzle.input_data.split('\n')]

    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == 'S':
                start = (i, j)
            if c == 'E':
                end = (i, j)

    grid = [[ord(c) - ord('a') for c in row] for row in grid]

    grid[start[0]][start[1]] = 0 
    grid[end[0]][end[1]] = ord('z') - ord('a')

    puzzle.answer_a = bfs(grid, start, end)

    shortest = float('inf')
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == 0:
                shortest = min(shortest, bfs(grid, (i, j), end))

    puzzle.answer_b = shortest
