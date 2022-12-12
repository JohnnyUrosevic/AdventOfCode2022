from aocd.models import Puzzle
from typing import List

def simulation(n: int, instructions: List[str]):

    x_positions = [0] * n
    y_positions = [0] * n

    direction_map = {
        "D": (0, -1),
        "U": (0, 1),
        "L": (-1, 0),
        "R": (1, 0),
    }

    visited = set([(0, 0)])

    for instruction in instructions:
        dir, count = instruction.split(' ')
        dx = direction_map[dir]

        for _ in range(int(count)):
            x_positions[0] += dx[0]
            y_positions[0] += dx[1]
        
            head_x = x_positions[0]
            head_y = y_positions[0]

            for i in range(1, n):
                tail_x = x_positions[i]
                tail_y = y_positions[i]

                if abs(tail_x - head_x) > 1:
                    tail_x += (head_x - tail_x) / abs(head_x - tail_x)
                    if tail_y != head_y:
                        tail_y += (head_y - tail_y) / abs(head_y - tail_y)
                elif abs(tail_y - head_y) > 1:
                    tail_y += (head_y - tail_y) / abs(head_y - tail_y)
                    if tail_x != head_x:
                        tail_x += (head_x - tail_x) / abs(head_x - tail_x)

                x_positions[i] = tail_x
                y_positions[i] = tail_y
                
                head_x = tail_x
                head_y = tail_y

            visited.add((tail_x, tail_y))

    return len(visited)

def rope_bridge():
    puzzle = Puzzle(year=2022, day=9)
    instructions = puzzle.input_data.split('\n')

    puzzle.answer_a = simulation(2, instructions)
    puzzle.answer_b = simulation(10, instructions)
