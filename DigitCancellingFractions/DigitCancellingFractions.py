
def digitCancellingFractions():
    result = 1
    for i in range(10, 100):
        for j in range(i + 1, 100):
            firstDiv = i / j
            for letter in str(i):
                if letter in str(j):
                    first = int(str(i).replace(letter, "")) if str(i).replace(letter, "") else int(letter)
                    second = int(str(j).replace(letter, "")) if str(j).replace(letter, "") else int(letter)
                    if first > 0 and second > 0 and letter != "0":
                        secondDiv = first / second
                        if firstDiv == secondDiv:
                            result *= second
                            print(f'i: {i}, j: {j}')
                        # print(f'First: {firstDiv}, second: {secondDiv}, numbers: first: {first}, second: {second}')
    print(f'Result: {result}')


if __name__ == '__main__':
    digitCancellingFractions()
