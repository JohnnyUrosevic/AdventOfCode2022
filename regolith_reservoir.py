from aocd.models import Puzzle

def regolith_reservoir():
    puzzle = Puzzle(year=2022, day=14)
    lines = puzzle.input_data.split('\n')

    tiles = set()

    floor = 0
    for line in lines:
        points = [[int(p) for p in point.split(',')] for point in line.split(' -> ')]
        prev_x, prev_y = points[0]

        for x, y in points[1:]:
            start_x = min(prev_x, x)
            start_y = min(prev_y, y)
            end_x = max(prev_x, x)
            end_y = max(prev_y, y)

            for i in range(start_x, end_x+1):
                for j in range(start_y, end_y+1):
                    tiles.add((i, j))
            
            floor = max(floor, y)

            prev_x = x
            prev_y = y

    tiles_backup = tiles.copy()
        
    rested = 0

    sand_x = 500
    sand_y = 0
    while True:
        if sand_y > floor:
            break

        if (sand_x, sand_y + 1) not in tiles:
            sand_y += 1
            continue 

        if (sand_x - 1, sand_y + 1) not in tiles:
            sand_x -= 1
            sand_y += 1
            continue 

        if (sand_x + 1, sand_y + 1) not in tiles:
            sand_x += 1
            sand_y += 1
            continue

        tiles.add((sand_x, sand_y))
        rested += 1
        sand_x = 500
        sand_y = 0 

    puzzle.answer_a = rested

    rested_2 = 0

    tiles = tiles_backup
    sand_x = 500
    sand_y = 0
    while True:
        if (500, 0) in tiles:
            break

        if sand_y != floor + 1:
            if (sand_x, sand_y + 1) not in tiles:
                sand_y += 1
                continue 

            if (sand_x - 1, sand_y + 1) not in tiles:
                sand_x -= 1
                sand_y += 1
                continue 

            if (sand_x + 1, sand_y + 1) not in tiles:
                sand_x += 1
                sand_y += 1
                continue

        tiles.add((sand_x, sand_y))
        rested_2 += 1
        sand_x = 500
        sand_y = 0 

    puzzle.answer_b = rested_2
