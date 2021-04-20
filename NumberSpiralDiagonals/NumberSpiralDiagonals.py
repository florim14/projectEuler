
def sumOfSpiralDiagonal(number):
    sum = 1
    rightBottomNumber = 3
    addNumber = 2
    for i in range(1, int(number/2) + 1):
        sum += rightBottomNumber * 4 + 6 * addNumber
        rightBottomNumber += (2 + i * 8)
        addNumber += 2
    return sum


if __name__ == '__main__':
    print(f'The sum of the numbers on the diagonals in a 1001 by 1001'
          f' spiral is: {sumOfSpiralDiagonal(1001)}')
