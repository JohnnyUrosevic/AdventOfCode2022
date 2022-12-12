from aocd.models import Puzzle
import re
from functools import lru_cache

class Directory():
    def __init__(self, parent=None):
        self.parent = parent
        self.filesize = 0
        self.subdirectories = {} 

def no_space():
    puzzle = Puzzle(year=2022, day=7)
    lines = puzzle.input_data.split('\n')

    root = Directory()
    working_directory = root

    for line in lines:
        if line[0] == '$':
            if (m := re.match(r'\$ cd (.*)', line)) is not None:
                target = m.group(1)
                if target == '/':
                    working_directory = root
                elif target == '..':
                    working_directory = working_directory.parent
                else:
                    working_directory = working_directory.subdirectories[target]
        else:
            if (m := re.match(r'dir (.*)', line)) is not None:
                working_directory.subdirectories[m.group(1)] = Directory(working_directory)
            else:
                size, _ = line.split(' ')
                working_directory.filesize += int(size)

    small_directory_sum = 0
    @lru_cache
    def get_directory_size(root):
        nonlocal small_directory_sum
        size = root.filesize

        for child in root.subdirectories.values():
            size += get_directory_size(child)

        if size <= 100000:
            small_directory_sum += size

        return size

    total_space_used = get_directory_size(root)
    puzzle.answer_a = small_directory_sum

    unused = 70000000 - total_space_used
    to_recover = 30000000 - unused

    @lru_cache
    def find_directory_to_delete(root):
        size = get_directory_size(root)

        result = size if size > to_recover else float('inf')

        for child in root.subdirectories.values():
            result = min(find_directory_to_delete(child), result)

        return result

    puzzle.answer_b = find_directory_to_delete(root)
