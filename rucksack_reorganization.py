from aocd.models import Puzzle

def priority(item: str):
    result = ord(item.lower()) - ord('a') + 1
    if item.isupper():
        result += 26
    
    return result

def get_common(sack: str):
    n = len(sack)
    return (set(sack[:n // 2]) & set(sack[n // 2:])).pop()

def rucksack_reorganization():
    puzzle = Puzzle(year=2022, day=3)
    rucksacks = puzzle.input_data.split('\n')

    common_items = [get_common(sack) for sack in rucksacks]
    priorities = [priority(item) for item in common_items]

    puzzle.answer_a = sum(priorities)

    badges_sum = 0
    for i in range(0, len(rucksacks), 3):
        badge = (set(rucksacks[i]) & set(rucksacks[i+1]) & set(rucksacks[i+2])).pop()
        badges_sum += priority(badge)

    puzzle.answer_b = badges_sum
