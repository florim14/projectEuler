
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


def latticePaths(number):
    return int(factorial(2 * number) / (factorial(number) * factorial(number)))


if __name__ == '__main__':
    number = 20
    print(f'Lattice Paths -- the number of routes for the number: {number} is: {latticePaths(number)}')
