
def findAllPalindromes():
    result = 0
    for i in range(1, 1000000):
        if str(i) == str(i)[::-1]:
            binary = bin(i)[2:]
            if binary == binary[::-1]:
                result += i
    print(f'The sum of all numbers , less than one million'
          f', which are binary in base 10 and base 2 is: {result} ')


if __name__ == '__main__':
    findAllPalindromes()
