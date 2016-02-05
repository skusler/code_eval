import sys


def rof_test():
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            double = []
            non_double = []
            count = 0
            while count < 19:
                if line[count] == ' ':
                    pass
                elif (count + 1) % 3 == 0 or (count + 1) == 1:
                    double.append(int(line[count]) * 2)
                else:
                    non_double.append(int(line[count]))
                count += 1
            if (sum(double) + sum(non_double)) % 10 == 0:
                print("Real")
            else:
                print("Fake")

rof_test()
