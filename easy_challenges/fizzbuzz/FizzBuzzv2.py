# This is for the challenge Fizz Buzz @ https://www.codeeval.com/open_challenges/1/

import sys


def fizzbuzz():
    # This sets the first command line argument as a variable to read.
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            # Checks for integers in a line and returns them to a list.
            pull_digits = [int(num) for num in test.split() if num.isdigit()]
            x = pull_digits[0]
            y = pull_digits[1]
            n = pull_digits[2]
            count = 0
            result = []
            while count < n:
                count += 1
                if count % x == 0 and count % y == 0:
                    result.append(str("FB"))
                elif count % x == 0:
                    result.append(str("F"))
                elif count % y == 0:
                    result.append(str("B"))
                else:
                    result.append(str(count))
            print(" ".join(result))

fizzbuzz()
