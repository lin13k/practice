def fib_recursive(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterate(n):
    dpTable = [0 for i in range(n)]
    dpTable[0] = 1
    dpTable[1] = 1
    for i in range(2, n):
        dpTable[i] = dpTable[i - 1] + dpTable[i - 2]
    return dpTable[-1]


if __name__ == '__main__':
    print(fib_recursive(30))
    print(fib_iterate(30))
