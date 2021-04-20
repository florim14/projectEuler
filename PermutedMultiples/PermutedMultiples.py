from itertools import count


def solution():
    for x in count(start=10):
        digits = sorted(str(2 * x))
        if all(sorted(str(x * k)) == digits for k in range(6, 2, -1)):
            return x


if __name__ == '__main__':
    print(f'The solution is: {solution()}')
