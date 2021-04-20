import math


def isPrime(num):
    prime = True
    if num < 2: return False
    if num == 2: return True
    for factor in range(3, int(math.sqrt(num)), 2):
        if num % factor == 0: prime = False
    return prime


def testEquation(a, b):
    n = 0
    while True:
        test = n ** 2 + a * n + b
        if isPrime(test):
            n += 1
        else:
            break
    return n


if __name__ == '__main__':
    best = 0
    bestA = 0
    bestB = 0
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            c = testEquation(a, b)
            # print "Testing n^2 + " + str(a) + "x + " + str(b) + ": result" + str(c)
            if c > best: best, bestA, bestB = c, a, b

    print(f'The product of the coefficients, that produces the maximum number of primes'
          f' for consecutive values of n < 1000 is: {bestA * bestB}')
