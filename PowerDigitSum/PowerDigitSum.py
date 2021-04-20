
def powerDigitSum(power):
    result = str(pow(2, power))
    sumOfDigits = 0

    for i in result:
        sumOfDigits += int(i)
    print(f'Result: {sumOfDigits}')


if __name__ == '__main__':
    powerDigitSum(1000)
