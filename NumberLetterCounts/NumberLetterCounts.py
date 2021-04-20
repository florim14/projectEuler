import inflect


def countLetters(number):
    inflectEngine = inflect.engine()
    return len((inflectEngine.number_to_words(number)).replace(" ", "").replace("-", ""))
    # print(f'Word {numberName} and its length is {len(numberName)}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    totalNumberOfLetters = 0
    for i in range(1, 1001):
        totalNumberOfLetters += int(countLetters(i))

    print(f'Total number of letters for numbers from 1 to 1000 is: {totalNumberOfLetters}')
