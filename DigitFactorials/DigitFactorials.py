import math


def digitFactorials():
    result = 0
    for i in range(10, 100000):
        factorial = 0
        for letter in str(i):
            factorial += math.factorial(int(letter))
        if i == factorial:
            result += i
            print(f'Number: {i} and his factorial is: {factorial}')

    print(f'Result is: {result}')


if __name__ == '__main__':
    digitFactorials()
