import math


def isPentagonal(number):
    res = (1 + math.sqrt(1 + 24 * number)) / 6
    return res.is_integer()


def isHexagonal(number):
    res = (1 + math.sqrt(1 + 8 * number)) / 4
    return res.is_integer()


if __name__ == '__main__':
    res = 286
    while True:
        triangle = (res * (res + 1)) / 2
        if isPentagonal(triangle) and isHexagonal(triangle):
            print(f'E gjete ;p, it is: {int(triangle)}')
            print(f'res: {res}')
            break
        res += 1