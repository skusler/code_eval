# This is for the challenge REAL FAKE @ https://www.codeeval.com/open_challenges/227/

import sys


def rof_test():
    # Takes file as input
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            result = []
            # Count total length is being used to iterate through whole line.
            count_len = 0
            # Count total num only goes up by when it detects a number and not a space.
            count_num = 0

            while count_len < 19:
                if line[count_len] == ' ':
                    pass
                # Used to double every other number starting with 1.
                elif (count_num + 1) % 2 != 0 or (count_num + 1) == 1:
                    result.append(int(line[count_len]) * 2)
                    count_num += 1
                else:
                    result.append(int(line[count_len]))
                    count_num += 1
                count_len += 1

            if sum(result) % 10 == 0:
                print("Real")
            else:
                print("Fake")

rof_test()
