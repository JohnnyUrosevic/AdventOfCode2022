from aocd.models import Puzzle
from ast import literal_eval
from functools import cmp_to_key

def compare(left, right):
    if type(left) == int and type(right) == int:
        return left - right
    
    if type(left) == int:
        return compare([left], right)

    if type(right) == int:
        return compare(left, [right])

    if not left and not right:
        return 0

    if not left:
        return -1
    
    if not right:
        return 1

    if (ret := compare(left[0], right[0])) != 0:
        return ret
    
    return compare(left[1:], right[1:])

def distress_signal():
    puzzle = Puzzle(year=2022, day=13)
    packets = puzzle.input_data.split('\n\n')

    correct_pairs = 0

    all_packets = []

    for i, pair in enumerate(packets):
        left, right = [literal_eval(x) for x in pair.split('\n')]
        all_packets += [left, right]

        if compare(left, right) < 0:
            correct_pairs += i + 1

    puzzle.answer_a = correct_pairs

    all_packets += [[[2]], [[6]]]
    all_packets.sort(key = cmp_to_key(compare))

    puzzle.answer_b = (all_packets.index([[2]]) + 1) * (all_packets.index([[6]]) + 1)
