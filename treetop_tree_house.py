from aocd.models import Puzzle

def treetop_tree_house():
    puzzle = Puzzle(year=2022, day=8)

    trees = [[int(c) for c in row] for row in puzzle.input_data.split('\n')]

    n = len(trees)
    m = len(trees[0])

    visible = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        visible[i][0] = True
        max_so_far = trees[i][0]
        for j in range(1, m):
            if trees[i][j] > max_so_far:
                visible[i][j] = True
                max_so_far = trees[i][j]

        visible[i][-1] = True
        max_so_far = trees[i][-1]
        for j in range(m-2,-1,-1):
            if trees[i][j] > max_so_far:
                visible[i][j] = True
                max_so_far = trees[i][j]

    for j in range(m):
        visible[0][j] = True
        max_so_far = trees[0][j]
        for i in range(1, n):
            if trees[i][j] > max_so_far:
                visible[i][j] = True
                max_so_far = trees[i][j]

        visible[-1][j] = True
        max_so_far = trees[-1][j]
        for i in range(n-2,-1,-1):
            if trees[i][j] > max_so_far:
                visible[i][j] = True
                max_so_far = trees[i][j]

    puzzle.answer_a = sum(sum([int(x) for x in row]) for row in visible)

    max_scenic_score = 0
    for i in range(n):
        for j in range(m):
            up = 0
            for y in range(i-1, -1, -1):
                up += 1
                if trees[y][j] >= trees[i][j]:
                    break

            down = 0
            for y in range(i+1, n):
                down += 1
                if trees[y][j] >= trees[i][j]:
                    break

            left = 0
            for x in range(j-1, -1, -1):
                left += 1
                if trees[i][x] >= trees[i][j]:
                    break

            right = 0
            for x in range(j+1, m):
                right += 1
                if trees[i][x] >= trees[i][j]:
                    break

            max_scenic_score = max(max_scenic_score, up * down * left * right)

    puzzle.answer_b = max_scenic_score
