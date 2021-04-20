import math


def checkSumPentagon(number):
    res = (1 + math.sqrt(1 + 24 * number)) / 6
    return res.is_integer()


if __name__ == '__main__':
    iterate = True
    pentagonNumbers = [1]
    checkSumPentagon(4)
    checkSumPentagon(5)
    while iterate:
        length = len(pentagonNumbers) + 1
        nextPentagon = length * ((3 * length - 1)/2)
        for element in reversed(pentagonNumbers):
            diff = nextPentagon - element
            sum = nextPentagon + element
            if diff in pentagonNumbers and checkSumPentagon(sum):
                iterate = False
                print(f'First: {nextPentagon}, '
                      f'second: {element}, '
                      f'and result: {diff}')
                break

        pentagonNumbers.append(nextPentagon)
