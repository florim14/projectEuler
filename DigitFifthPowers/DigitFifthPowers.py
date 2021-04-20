
def fifthPower():
    sumFifthPower = 0
    for number in range(2, 1000000):
        sum = 0
        for digit in str(number):
            sum += int(digit) ** 5
        if sum == number:
            sumFifthPower += sum
    print(f'The sum of all the numbers that can be written '
          f'as the sum of fifth powers of their digits is: {sumFifthPower}')


if __name__ == '__main__':
    fifthPower()
