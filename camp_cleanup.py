from aocd.models import Puzzle

def camp_cleanup():
    puzzle = Puzzle(year=2022, day=4)
    pairs = [pair.split(',') for pair in puzzle.input_data.split('\n')]

    contained = 0
    overlapped = 0
    for a, b in pairs:
        a_start, a_end = [int(x) for x in a.split('-')]
        b_start, b_end = [int(x) for x in b.split('-')]

        contained += int((a_start <= b_start and a_end >= b_end) or (b_start <= a_start and b_end >= a_end))
        overlapped += int((b_start <= a_start <= b_end) or (a_start <= b_start <= a_end) or (b_start <= a_end <= b_end) or (a_start <= b_end <= a_end))

    puzzle.answer_a = contained
    puzzle.answer_b = overlapped
