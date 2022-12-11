from aocd.models import Puzzle

def get_unique(data: str, size: int):
    for i in range(len(data) - size + 1):
        chars = set(data[i:i+size])
        if len(chars) == size:
            return i + size


def tuning_trouble():
    puzzle = Puzzle(year=2022, day=6)
    data = puzzle.input_data

    puzzle.answer_a = get_unique(data, 4)
    puzzle.answer_b = get_unique(data, 14)
