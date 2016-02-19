# This is for the challenge Sum of Primes @ https://www.codeeval.com/open_challenges/4/


import sys


def sop():
    prime_list = []
    counter = 1
    # Length to check to make sure list of primes includes at least 1000 before moving on.
    while len(prime_list) < 1000:
        counter += 1
        # For loop to check for prime.
        for i in range(2, counter):
            if counter % i == 0:
                break
        else:
            prime_list.append(counter)
    else:
        return str(sum(prime_list))


sum_of_primes = sop()


sys.stdout.write(sum_of_primes)
