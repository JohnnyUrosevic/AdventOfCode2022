from aocd.models import Puzzle

def calculate_score(round: str):
    opponent, us = round.split(' ')
    opponent_num = ord(opponent) - ord('A')
    us_num = ord(us) - ord('X')
    
    return calculate_score_helper(opponent_num, us_num)

def calculate_score_helper(opponent_num, us_num):
    if opponent_num == us_num:
        result = 3
    elif us_num == ((opponent_num + 1) % 3):
        result = 6
    else:
        result = 0

    return us_num + result + 1

def calculate_correct_score(round: str):
    opponent, us = round.split(' ')
    opponent_num = ord(opponent) - ord('A')

    if us == 'X':
        return calculate_score_helper(opponent_num, (opponent_num - 1) % 3)
    elif us == 'Y':
        return calculate_score_helper(opponent_num, opponent_num)
    else:
        return calculate_score_helper(opponent_num, (opponent_num + 1) % 3)


def rock_paper_scissors():
    puzzle = Puzzle(year=2022, day=2)
    rounds = puzzle.input_data.split('\n')

    scores = [calculate_score(round) for round in rounds]

    puzzle.answer_a = sum(scores)

    corrected_scores = [calculate_correct_score(round) for round in rounds]

    puzzle.answer_b = sum(corrected_scores)
