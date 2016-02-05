# This is for the challenge Testing @ https://www.codeeval.com/open_challenges/225/

import sys


# B = Bug, N = Number, P = Priority.  Bug number, priority.
def bnp():
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            # Split one string into two with the divider of ' | '.
            test_split = line.split(' | ')
            test_code = test_split[0]
            dev_code = test_split[1]
            bug_num = 0
            # Compares each digit of a the strings, if not the same it is counted as a bug.
            for i in range(len(test_code)):
                if test_code[i] != dev_code[i]:
                    bug_num += 1
            # Uncomment the two lines below for testing results.
            # print(test_split)
            # print(bug_num)

            if bug_num == 0:
                print("Done")
            elif bug_num <= 2:
                print("Low")
            elif bug_num <= 4:
                print("Medium")
            elif bug_num <= 6:
                print("High")
            else:
                print("Critical")


bnp()
