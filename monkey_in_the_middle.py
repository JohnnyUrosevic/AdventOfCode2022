from aocd.models import Puzzle
from math import prod

class Monkey():
    def __init__(self, monkey_string):
        self.inspections = 0
        
        monkey_lines = monkey_string.split('\n')

        self.inventory = [int(x[1:]) for x in monkey_lines[1].split(":")[-1].split(',')]
        operation_string = monkey_lines[2].split('= ')[-1]

        self.operation = (lambda old: eval(operation_string))

        self.divisor = int(monkey_lines[3].split(' ')[-1])
        self.test = lambda x: x % self.divisor == 0

        self.true_dest = int(monkey_lines[4].split(' ')[-1])
        self.false_dest = int(monkey_lines[5].split(' ')[-1])

    def round(self, relief=True):
        throws = []
        for item in self.inventory:
            self.inspections += 1

            new_item = self.operation(item)

            if relief:
                new_item //= 3

            if self.test(new_item):
                throws.append((self.true_dest, new_item))
            else:
                throws.append((self.false_dest, new_item))

        self.inventory = []
        return throws


def monkey_in_the_middle():
    puzzle = Puzzle(year=2022, day=11)
    monkey_strings = puzzle.input_data.split('\n\n')
    
    monkeys = [Monkey(monkey_string) for monkey_string in monkey_strings]

    for _ in range(20):
        for monkey in monkeys:
            throws = monkey.round()

            for dest, item in throws:
                monkeys[dest].inventory.append(item)

    active = sorted([m.inspections for m in monkeys])
    puzzle.answer_a = active[-1] * active[-2]

    monkeys = [Monkey(monkey_string) for monkey_string in monkey_strings]

    reducer = prod([m.divisor for m in monkeys])
    for _ in range(10000):
        for monkey in monkeys:
            throws = monkey.round(relief=False)

            for dest, item in throws:
                monkeys[dest].inventory.append(item % reducer)
    
    active = sorted([m.inspections for m in monkeys])
    puzzle.answer_b = active[-1] * active[-2]
