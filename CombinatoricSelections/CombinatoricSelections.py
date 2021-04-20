
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def solve():
    solution = 0
    for i in range(1, 101):
        for j in range(1, i + 1):
            if factorial(i)/(factorial(j) * factorial(i - j)) > 1000000:
                solution += 1
    print(f'Solution: {solution}')

if __name__ == '__main__':
    solve()
