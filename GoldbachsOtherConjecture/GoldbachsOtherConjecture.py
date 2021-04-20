from collections import defaultdict
from itertools import count


if __name__ == '__main__':
    factors = defaultdict(list)
    witness = {}
    primes = set()
    for n in count(2):
        if factors[n]:
            for m in factors.pop(n):
                factors[n + m].append(m)
            if n % 2:
                for k in range(1, int((n / 2) ** .5) + 1):
                    p = n - 2 * k ** 2
                    if p in primes:
                        witness[n] = k
                        break
                if not n in witness:
                    print(f'solution is: {n}')
                    break
        else:
            factors[n * n].append(n)
            primes.add(n)
