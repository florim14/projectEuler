from functools import reduce
from operator import mul


def solve():
    upper_limit = 200000
    fractional_string = "".join(["{}".format(i + 1) for i in range(upper_limit)])

    indices = [1, 10, 100, 1000, 10000, 100000, 1000000]
    digits = [fractional_string[i - 1] for i in indices]

    answer = reduce(mul, map(int, digits))

    return answer


if __name__ == '__main__':
    print(f'The solution is: {solve()}')
