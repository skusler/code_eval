# This is for challenge Black Card @ https://www.codeeval.com/open_challenges/222/

import sys


def bc():
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            game_split = line.split(' | ')
            names = game_split[0].split()
            max_turns = int(game_split[1])
            count = 0
            print(names)
            print(max_turns)
            print(count)



bc()
