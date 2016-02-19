# This is for the challenge Prime Palindrome @ https://www.codeeval.com/open_challenges/3/


import sys


def pp(arg):
    # Reversed range to find biggest first
    for x in reversed(range(2, arg)):
        # Checks for palindrome first as that's easier than finding if prime.
        if str(x) == str(x)[::-1]:
            # Second for loop to check for prime
            # The top range is the square root of arg rounded down.
            for i in range(2, int(x ** 0.5)):
                if x % i == 0:
                    break
            else:
                return str(x)


prime_palindrome = pp(100000000000)


sys.stdout.write(prime_palindrome)
