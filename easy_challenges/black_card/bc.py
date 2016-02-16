# This is for challenge Black Card @ https://www.codeeval.com/open_challenges/222/

import sys


def bc():
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            game_split = line.split(' | ')
            names = game_split[0].split()
            max_turns = int(game_split[1])
            while len(names) > 1:
                # Used to cycle through all names successfully.  Minus 1 added because of arrays starting at 0.
                bye_bye = (max_turns - 1) % len(names)
                names.remove(names[bye_bye])
            else:
                print(names[0])


bc()
