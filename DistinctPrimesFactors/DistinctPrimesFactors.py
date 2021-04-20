
def solve():
    target = 4
    limit = 150000
    n_prime_divisors = [0] * limit

    run_length = 0
    for n in range(2, limit):
        if n_prime_divisors[n] == 0:
            for m in range(2 * n, limit, n):
                n_prime_divisors[m] += 1
            run_length = 0
        elif n_prime_divisors[n] == target:
            run_length += 1
        else:
            run_length = 0
        if run_length == target:
            return n - target + 1


if __name__ == '__main__':
    print(f'The first four consequence to have four distinct prime'
          f'factors each is: {solve()}')
