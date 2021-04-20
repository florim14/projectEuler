
def collatzSequence():
    setOfNum = []
    largestNumber = 0
    biggestNumberOfItems = 0
    for i in range(499999, 1000001, 2):
        numberOfTerms = 0
        currentNumber = i
        while currentNumber != 1:
            numberOfTerms += 1
            if currentNumber % 2 == 0:
                currentNumber = int(currentNumber / 2)
            else:
                currentNumber = 3 * currentNumber + 1
        setOfNum.append(numberOfTerms)
        if biggestNumberOfItems <= numberOfTerms:
            biggestNumberOfItems = numberOfTerms
            largestNumber = i

    return largestNumber


if __name__ == '__main__':
    print("Longest sequence is: " + str(collatzSequence()))
