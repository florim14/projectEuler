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


def abundantSum(number, abundantNumbers):
    if len(abundantNumbers) < 2:
        return True
    for abundant in abundantNumbers:
        if (number - abundant) in abundantNumbers:
            return False
    return True


# Not that efficient, it consumes a lot of time
if __name__ == '__main__':
    abundantNumbers = []
    sumOfAbundantNumbers = 0
    for i in range(1, 28123):
        divisorSum = int(sum(list(divisorGenerator(i))[:-1]))
        if divisorSum > i:
            abundantNumbers.append(i)
        if abundantSum(i, abundantNumbers):
            sumOfAbundantNumbers += i
    print(abundantNumbers)

    print(sumOfAbundantNumbers)
