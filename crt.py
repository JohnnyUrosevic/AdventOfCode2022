from aocd.models import Puzzle

def crt():
    puzzle = Puzzle(year=2022, day=10)
    instructions = puzzle.input_data.split('\n')

    register_values = [1]

    x = 1

    for instruction in instructions:
        register_values.append(x)
        if instruction == 'noop':
            continue

        register_values.append(x)
        x += int(instruction.split(' ')[1])
    
    register_values.append(x)

    puzzle.answer_a = sum(register_values[i] * i for i in range(20, 221, 40))

    k = 1
    for i in range(6):
        for j in range(40):
            if j == register_values[k] or j == register_values[k] - 1 or j == register_values[k] + 1:
                print('# ', end='')
            else:
                print('. ', end='')
            k += 1
        print()

    puzzle.answer_b = 'RKAZAJBR'