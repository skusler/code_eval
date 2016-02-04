# Allows for the use of system\console arguments.
import sys


def fizz_buzz():
    # This sets the first command line argument as a variable to read.
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            # Checks for integers in a line and returns them to a list.
            pull_digits = [int(num) for num in line.split() if num.isdigit()]
            x = pull_digits[0]
            y = pull_digits[1]
            z = pull_digits[2]
            count = 0
            while count < z:
                count += 1
                if count % x == 0 and count % y == 0:
                    print('FB', end="")
                elif count % x == 0:
                    print('F', end="")
                elif count % y == 0:
                    print('B', end="")
                else:
                    if count == z:
                        print(str(count), end="")
                    else:
                        print(str(count), end="")
            else:
                print()

fizz_buzz()
