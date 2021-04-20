
def readfile(filepath, delimiter):
    with open(filepath, 'r') as f:
        for line in f:
            return line.split(delimiter)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numberOfTriangleWords = 0
    triangleNumber = []
    for i in range(1, 25):
        triangleNumber.append(int(0.5 * i * (i + 1)))
    data = readfile("words.txt", ',')
    for word in data:
        sum = 0
        for letter in word:
            sum += ord(letter) - 64
        if sum in triangleNumber:
            numberOfTriangleWords += 1
    print(f'Number of triangle words in the file is: {numberOfTriangleWords}')
