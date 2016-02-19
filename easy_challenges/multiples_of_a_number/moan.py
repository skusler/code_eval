# This is for the challenge Multiples of a Number @ https://www.codeeval.com/open_challenges/18/

import sys


def moan():
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            line_split = line.split(',')
            x = int(line_split[0])
            n = int(line_split[1])
            count = 1
            while n < x:
                # Reassign n to initial value if it's still lower than x.
                n = int(line_split[1])
                n *= count
                count += 1
            else:
                print(n)


moan()
