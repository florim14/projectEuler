import itertools


def findPermutation():
    permutations = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    result = ''.join(map(str, permutations[999999]))

    print(f'The one million permutation ordered lexicographically is: {result}')


if __name__ == '__main__':
    findPermutation()
