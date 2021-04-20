
def isPrime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':

    for a in range(7654321, 1234567, -2):
        if ''.join(sorted("%d" % a)) == '1234567':
            if isPrime(a):
                print(a)
                break
