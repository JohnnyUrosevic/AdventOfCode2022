from aocd.models import Puzzle

def calorie_counting():
    puzzle = Puzzle(year=2022, day=1)
    elves = puzzle.input_data.split('\n\n')

    nums = [[int(x) for x in elf.split('\n')] for elf in elves]
    totals = [sum(elf) for elf in nums]

    puzzle.answer_a = max(totals)
    puzzle.answer_b = sum(sorted(totals)[-3:])
