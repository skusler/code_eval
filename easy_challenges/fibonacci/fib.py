# This is for the challenge Fibonacci Series @ https://www.codeeval.com/open_challenges/22/

import sys


fib_sequence = open(sys.argv[1], 'r')

for line in fib_sequence:
    result = 0
    if line:
        def fibfib(n):
            if n == 0 or n == 1:
                return n
            else:
                # Recursive loop until n == 1.
                return fibfib(n - 1) + fibfib(n - 2)
        result = fibfib(int(line))
    sys.stdout.write(str(result))
    sys.stdout.write('\n')


fib_sequence.close()
