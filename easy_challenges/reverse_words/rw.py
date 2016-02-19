# This is for challenge Reverse Words @ https://www.codeeval.com/open_challenges/8/

import sys


def rw():
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            # Strips any whitespace on the ends, eliminating blanks lines.
            line.strip()
            line_split = line.split()
            new_line = []
            ls_length = len(line_split) - 1
            while ls_length > -1:
                new_line.append(line_split[ls_length])
                ls_length -= 1
            else:
                # Removes trailing whitespace.
                new_line = (" ".join(new_line)).strip()
                print(new_line)


rw()
