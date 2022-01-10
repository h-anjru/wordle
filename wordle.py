import mmap
import random as r

# emoji match indicators
no_match = '❌'
in_word = '🟨'
exact_match = '🟩'

# the possible solutions!
wordfile = 'five-letter-words_scores.txt'


def choose_solution():
    """Choose a random five-letter word from the plaintext file.

    The possible words are of the format 'wwwww12' which is a five-letter word and its score in US Scrabble as either a
    one- or two-digit number. The alphanumeric string is parsed and returned as the solution and the Scrabble score.
    
    Approach used: https://stackoverflow.com/a/35579149"""

    line_num = 0
    selected_line = ''

    with open(wordfile) as f:
        while True:
            line = f.readline()
            if not line:
                break
            line_num += 1
            if r.uniform(0, line_num) < 1:
                selected_line = line

    word = selected_line[:5]
    score = selected_line.replace(word,'').strip()

    return word, score


def match_checker(solution, user_guess):
    """Check user input against solution"""

    user_matches = [no_match] * 5  # start fresh

    for idx_in, letter_in in enumerate(user_guess):
        for idx_sol, letter_sol in enumerate(solution):
            if letter_in == letter_sol:
                if idx_in == idx_sol:
                    user_matches[idx_in] = exact_match
                    break
                else:
                    user_matches[idx_in] = in_word

    return(user_matches)


def solve_checker(user_matches):
    """Check if solved!"""

    solved = all(match == exact_match for match in user_matches)

    if solved:
        print('Congratulations!')

    return solved


# TODO: def input_checker() to check length and if it's a word
def input_checker(user_guess):
    """Check if the user's input is actually a word."""

    with open(wordfile) as f, mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as s:
        if s.find(str.encode(user_guess)) != -1:
            valid = True
        else:
            print('That is not recognized as a word.')
            valid = False

    return valid


def play_game():
    """Main gameplay"""

    matches_history = []
    guess_history = []

    solution, difficulty = choose_solution()

    print(f'Scrabble (US) score: {difficulty}')
    print('To end the game, type "I give up"')

    solved = False
    # TODO: add a counter for maximum number of guesses?

    while not solved:
        input_valid = False
        while input_valid is False:
            user_input = input('Your guess: ').lower()
            if user_input == 'i give up':
                print(f'The word was "{solution}"!')
                return True

            input_valid = input_checker(user_input)

        matches = match_checker(solution, user_input)

        matches_str = ''.join(matches)
        matches_history.append(matches_str)
        print(matches_str)

        solved = solve_checker(matches)

    # print results
    for line in matches_history:
        print(line)

    return True


play_game()
