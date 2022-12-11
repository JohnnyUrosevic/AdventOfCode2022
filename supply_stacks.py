from aocd.models import Puzzle
import re

def supply_stacks():
    puzzle = Puzzle(year=2022, day=5)
    stack_input, instructions = [x.split('\n') for x in puzzle.input_data.split('\n\n')]

    stacks = [[] for _ in range(9)]

    for line in stack_input[:-1]:
        j = 0
        for i in range(1, len(line), 4):
            if line[i] != ' ':
                stacks[j].append(line[i])
            j += 1

    [stack.reverse() for stack in stacks]
    updated_stacks = [stack.copy() for stack in stacks]

    for instruction in instructions:
        m = re.match(r'move (\d+) from (\d+) to (\d+)', instruction)
        count = int(m.group(1))
        source = int(m.group(2)) - 1
        dest = int(m.group(3)) - 1

        for _ in range(count):
            stacks[dest].append(stacks[source].pop())

        current_move = []
        for _ in range(count):
            current_move.append(updated_stacks[source].pop())
        
        current_move.reverse()
        updated_stacks[dest] += current_move
    
    tops = "".join([x[-1] for x in stacks])
    puzzle.answer_a = tops

    updated_tops = "".join([x[-1] for x in updated_stacks])
    puzzle.answer_b = updated_tops
