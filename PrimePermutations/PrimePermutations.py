from itertools import permutations


def findPermutation(number):
    return [''.join(p) for p in permutations(str(number))]


def isPrime(x):
    if x > 1:
        for i in range(2, x + 1):
            if x % i == 0 and i != x and i != 1:
                return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    threePrimes = []
    # permutations = findPermutation(1235)
    # for el in permutations:
    #     print(isPrime(int(el)))

    for number in range(1488, 3000):
        threePrimes = []
        if isPrime(number):
            allPermutations = findPermutation(number)
            for element in allPermutations:
                if isPrime(int(element)):
                    threePrimes.append(element)
        if len(threePrimes) > 2:
            if str(number + 3330) in threePrimes and str(number + 6660) in threePrimes:
                print(f'12-digit number do you form by concatenating the three terms in this'
                      f' sequence is: {str(number) + str(number + 3330) + str(number + 6660)}')
                break
