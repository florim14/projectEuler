import math


def numberPower(number):
    allNumber = []
    for i in range(2, number + 1):
        for j in range(2, number + 1):
            allNumber.append(i ** j)
    print(f'The number of distinct terms in the sequence is: '
          f'{len(sorted(set(allNumber)))}')


if __name__ == '__main__':
    numberPower(100)
