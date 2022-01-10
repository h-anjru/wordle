import mmap
import os
import random as r

# emoji match indicators
no_match = '❌'
in_word = '🟨'
exact_match = '🟩'

# the possible solutions!
abs_path = os.path.dirname(os.path.abspath(__file__))
wordfile_name = 'five-letter-words_scores.txt'
wordfile_path = os.path.join(abs_path, wordfile_name)


def choose_solution():
    """Choose a random five-letter word from the plaintext file.

    The possible words are of the format 'wwwww12' which is a five-letter word and its score in US Scrabble as either a
    one- or two-digit number. The alphanumeric string is parsed and returned as the solution and the Scrabble score.
    
    Approach used: https://stackoverflow.com/a/35579149"""

    line_num = 0
    selected_line = ''

    with open(wordfile_path) as f:
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


def input_checker(user_guess):
    """Check if the user's input is actually a word.
    
    Method for checking if input is in text file: https://stackoverflow.com/a/4944929"""

    if len(user_guess) != 5:
        print('Your guess is not of the correct length (5).')
        valid = False
    else:
        with open(wordfile_path) as f, mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as s:
            if s.find(str.encode(user_guess)) != -1:
                valid = True
            else:
                print('That is not recognized as a word.')
                valid = False

    return valid


def match_checker(user_guess, solution):
    """Check user input against solution"""

    user_matches = [no_match] * 5  # start fresh
    in_solution = ''

    for idx_in, letter_in in enumerate(user_guess):
        for idx_sol, letter_sol in enumerate(solution):
            if letter_in == letter_sol:
                # exact match
                if idx_in == idx_sol:
                    user_matches[idx_in] = exact_match
                    in_solution += letter_in
                # match in word
                else:
                    user_matches[idx_in] = in_word
                    in_solution += letter_in

                # replace letter in guess & solution with non-letter to exclude from further checking
                temp_list = list(user_guess)
                temp_list[idx_sol] = '*'
                user_guess = ''.join(temp_list)

                temp_list = list(solution)
                temp_list[idx_sol] = '&'
                solution = ''.join(temp_list)

    # get a string of letters not in solution
    not_in_solution = user_guess

    for letter in in_solution:
        not_in_solution = not_in_solution.replace(letter, '')

    return user_matches, in_solution, not_in_solution


def remaining_letters(right_guesses, wrong_guesses):
    """Return a list of letters that are still available."""

    alphabet = 'abcdefghi\njklmnopqr\nstuvwxyz'

    remaining_alphabet = []  # list of strings to be represented as emojis

    for letter in alphabet:
        if letter in right_guesses:
            char_to_append = f'[{letter}]'
        elif letter in wrong_guesses:
            char_to_append = ' · '
        elif letter == '\n':
            char_to_append = letter
        else:
            char_to_append = f' {letter} '

        remaining_alphabet.append(char_to_append)

    return remaining_alphabet


def main():
    """Main gameplay"""

    # tracking variables
    matches_history = []  # list of strings of emojis for graphing guesses
    matched_letters = ''
    missed_letters = ''

    solution, difficulty = choose_solution()

    # welcome message
    print('Try to guess the five-letter word!')
    print(f'Scrabble (US) score: {difficulty}')
    print('To see eliminated letters, type "letters"')
    print('To end the game, type "I give up"\n')

    # user input loop
    solved = False

    while not solved:
        input_valid = False
        while input_valid is False:
            user_input = input('Your guess: ').lower().strip()
            if user_input == 'i give up':
                print(f'The word was "{solution}"!')
                return True
            if user_input == 'letters':
                remaining = remaining_letters(matched_letters, missed_letters)
                print(''.join(remaining))
                continue  # return to beginning of loop

            input_valid = input_checker(user_input)

        match_emojis, matches, misses = match_checker(user_input, solution)

        # make the emoji string to graph guesses
        match_emoji_str = ''.join(match_emojis)

        # check if solved
        solved = user_input == solution

        # add results to tracking variables
        matches_history.append(match_emoji_str)
        matched_letters += matches
        missed_letters += misses

        if not solved:
            print(match_emoji_str)


    # print results on solve
    print('Congratulations!')
    for line in matches_history:
        print(line)

    return True


if __name__ == "__main__":
    main()
