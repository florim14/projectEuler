
def solve():
    sum = 0
    for i in range(1, 1001):
        sum += (i**i)
    print(f'The last ten digits of sum are: {str(sum)[-10:]}')


if __name__ == '__main__':
    solve()
