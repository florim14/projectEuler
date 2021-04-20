# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def isPrime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i = i + 6
    return True


def elevenTruncatablePrimes():
    countTruncatable = 0
    iterator = 11
    sumOfTruncatablePrimes = 0
    while countTruncatable < 11:
        prime = True
        if isPrime(iterator):
            strIterator = str(iterator)
            for i in range(1, len(strIterator)):
                if (not isPrime(int(strIterator[:-i])) or
                        not isPrime(int(strIterator[i:]))):
                    prime = False
                    break
            if prime:
                countTruncatable += 1
                sumOfTruncatablePrimes += iterator
                print(iterator)
        iterator += 1

    print(f'The sum of the eleven primes that are both truncatable from'
          f' left to right and right to left is: {sumOfTruncatablePrimes}')


if __name__ == '__main__':
    elevenTruncatablePrimes()
