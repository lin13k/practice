def isPrime(n):
    if n % 2 == 0 and n > 2 or n < 2:
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))


def primeQuery(n, first, second, values, queries):
    # Write your code here

    subs = [[] for _ in range(n + 1)]
    cache = [0 for _ in range(n + 1)]
    values = [0] + values
    path = set()
    for i in range(len(first)):
        subs[first[i]].append(second[i])
        subs[second[i]].append(first[i])

    def sumCnts(index):
        path.add(index)
        cnt = 1 if isPrime(values[index]) else 0
        cnt += sum(sumCnts(sub) for sub in subs[index] if sub not in path)
        cache[index] = cnt
        return cnt

    sumCnts(1)
    return [cache[q] for q in queries]


if __name__ == '__main__':
    for i in range(100):
        print(i, isPrime(i))
