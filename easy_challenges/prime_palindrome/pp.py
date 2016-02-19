# This is for the challenge Prime Palindrome @ https://www.codeeval.com/open_challenges/3/


import sys


def pp():
    # Reversed range to find biggest first
    for x in reversed(range(2, 1000)):
        # Checks for palindrome first as that's easier than finding if prime.
        if str(x) == str(x)[::-1]:
            # Second for loop to check for prime
            for i in range(2, x):
                if x % i == 0:
                    break
            else:
                return str(x)


prime_palindrome = pp()


sys.stdout.write(prime_palindrome)
