
def isPandigital(Str):
    if len(Str) != 9:
        return bool(False)
    ch = "".join(sorted(Str))
    if ch == "123456789":
        return bool(True)
    else:
        return bool(False)


def solution():
    for x in range(9487, 9234, -1):
        res = 100002 * x
        if isPandigital(str(res)):
            return res
    return 0


if __name__ == '__main__':
    print(f'The solution is: {solution()}')
