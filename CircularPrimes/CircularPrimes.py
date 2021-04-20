
def getPrimesBelowN(n=1000000):
    from math import ceil
    primes = [True] * n
    primes[0] = False
    primes[1] = False
    primeList = []
    roundUp = lambda n, prime: int(ceil(float(n) / prime))
    for currentPrime in range(2, n):
        if not primes[currentPrime]:
            continue
        primeList.append(currentPrime)
        for multiplicant in range(2, roundUp(n, currentPrime)):
            primes[multiplicant * currentPrime] = False
    return primes


def isCircularPrime(primes, number):
    number = str(number)
    for i in range(0, len(number)):
        rotatedNumber = number[i : len(number)] + number[0:i]
        if not primes[int(rotatedNumber)]:
            return False
    return True


if __name__ == '__main__':
    primes = getPrimesBelowN(1000000)
    numberOfPrimes = 2
    for prime, isPrime in enumerate(primes):
        if (
                (not isPrime)
                or ("2" in str(prime))
                or ("4" in str(prime))
                or ("6" in str(prime))
                or ("8" in str(prime))
                or ("0" in str(prime))
                or ("5" in str(prime))
        ):
            continue
        if isCircularPrime(primes, prime):
            numberOfPrimes += 1

    print("Number of circular primes: %i" % numberOfPrimes)
