
def nameValue(name):
    result = 0
    for letter in name:
        result += ord(letter) - 64
    return result


def readText(fileName):
    file = open(fileName, "r+")
    text = file.readlines()
    file.close()

    allNames = text[0].replace("\"", "").split(",")
    allNames.sort()

    iteration = 1
    totalSum = 0
    for name in allNames:
        value = nameValue(name)
        totalSum += (value * iteration)
        iteration += 1

    return totalSum


if __name__ == '__main__':
    print(f'The total of all name scores in the names.txt file is: {readText("names.txt")}')
