"""a sort of game
computer improves and then guessing a number by itself
then the result is being compared with a random guessing result
"""

import numpy as np

def random_guess(puzzle:int=42) -> int:
    """ Random guessing for using as a reference

    Args:
        puzzle (int, optional): The number to guess. Defaults to random number in range from one to 100

    Returns:
        int: number of tries needed to guess (including the succesful one)
    """
    try_count = 0
    
    while True:
        try_count += 1
        supposed = np.random.randint(1, 100)  # an anticipation
        if puzzle == supposed:
            break  # leaving the cicle when guessing
    return try_count


def alg_guess(puzzle:int=42) -> int:
    """ Guessing with a primitive algorithm

    Args:
        puzzle (int, optional): The number to guess. Defaults to random number in range from one to 100

    Returns:
        int: number of tries needed to guess (including the succesful one)
    """
    try_count, less_guess, more_guess = 0, 1, 100
    
    while True:
        try_count += 1
        supposed = np.random.randint(less_guess, more_guess)  # an anticipation
        if puzzle > supposed:
            less_guess = supposed
        elif puzzle < supposed:
            more_guess = supposed
        elif puzzle == supposed:            
            break  # leaving the circle when guessing
    return try_count


def score_game(guesser) -> int:
    """ Counting average number of attempts (out of 1000) to guess

    Args:
        guesser ([type]): guessing function to check efficiency

    Returns:
        int: average attempts
    """
    try_count_list = []
    np.random.seed(1)  # seed fixation for reproductability
    random_array = np.random.randint(1, 100, size=(1000))  # list of puzzles to guess
    
    for number in random_array:
        try_count_list.append(guesser(number))
        
    guess_score = int(np.mean(try_count_list))
    print(f'The score of {guesser.__name__} is {guess_score}')
    return guess_score


if __name__ == "__main__":
    # RUN
    score_game(random_guess)
    score_game(alg_guess)