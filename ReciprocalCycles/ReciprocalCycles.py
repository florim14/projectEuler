from pip._vendor.msgpack.fallback import xrange


def solve():
    num = longest = 1
    for n in xrange(3, 1000, 2):
        if n % 5 == 0:
            continue
        p = 1
        while (10 ** p) % n != 1:
            p += 1
        if p > longest:
            num, longest = n, p

    return num


if __name__ == '__main__':
    print(f'The longest recurring cycle in its decimal fraction part : {solve()}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
