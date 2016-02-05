# This is for the challenge EVEN NUMBER @ https://www.codeeval.com/open_challenges/100/

import sys


def even():
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            if int(line) % 2 == 0:
                print(1)
            else:
                print(0)

even()
