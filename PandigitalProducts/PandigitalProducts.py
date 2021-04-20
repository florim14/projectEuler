
def pandigitalProduct_1_9(n):
    i = 1
    while i * i <= n:
        if ((n % i == 0) and
                bool(isPandigital(str(n) +
                                  str(i) +
                                  str(n // i)))):
            return bool(True)
        i += 1
    return bool(False)


def isPandigital(Str):
    if len(Str) != 9:
        return bool(False)
    ch = "".join(sorted(Str))
    if ch == "123456789":
        return bool(True)
    else:
        return bool(False)


if __name__ == '__main__':
    sum = 0
    for i in range(100, 9999):
        if bool(pandigitalProduct_1_9(i)):
            sum += i
    print(f'The sum is: {sum}')