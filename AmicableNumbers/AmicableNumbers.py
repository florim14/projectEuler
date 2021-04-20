import math
from pip._vendor.msgpack.fallback import xrange


def divisorGenerator(number):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(number) + 1)):
        if number % i == 0:
            yield i
            if i*i != number:
                large_divisors.append(number / i)
    for divisor in reversed(large_divisors):
        yield divisor


def findAmicableNumbers(number):
    result = 0
    for i in range(1, number):
        divisorSum = int(sum(list(divisorGenerator(i))[:-1]))
        if i > divisorSum:
            secondNumber = int(sum(list(divisorGenerator(divisorSum))[:-1]))
            if (divisorSum != secondNumber and
                i == secondNumber):
                result += divisorSum + secondNumber
                print(f'First: {divisorSum}, second; {secondNumber}')
    return result


if __name__ == '__main__':
    print(f'The sum of amicable numbers under 10000 is: {findAmicableNumbers(10000)}')
