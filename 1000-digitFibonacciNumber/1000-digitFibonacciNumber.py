
def findFibonacci():
    first = 1
    second = 1
    result = 0
    index = 2
    while len(str(result)) < 1000:
        result = first + second
        index += 1
        first = second
        second = result

    print(f'The index of the term in the Fibonacci sequence '
          f'that contains 1000 digits is: {index}')


if __name__ == '__main__':
    findFibonacci()
