# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def solution(number):
    max = 0
    maxp = 0
    for i in range(2, number + 1, 2):
        c = 0
        for a in range(2, int(i / 3)):
            if i * (i - 2 * a) % (2 * (i - a)) == 0:
                c += 1
        if c > max:
            max = c
            maxp = i

    return maxp


if __name__ == '__main__':
    print(f'The maximum integer right triangle for p < 1000 is: {solution(1000)}')
