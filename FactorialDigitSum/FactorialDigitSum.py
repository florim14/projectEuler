
def findFactorial(number):
    if number == 1:
        return 1
    else:
        return number * findFactorial(number - 1)


def findSum(number):
    sumOfLetters = 0
    for letter in number:
        sumOfLetters += int(letter)
    return sumOfLetters


if __name__ == '__main__':
    factorial = findFactorial(100)
    result = findSum(str(factorial))
    print(f'The sum of the digits in the number 100! is: {result}')
