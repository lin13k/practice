def printBits(n):
    print(n, '\t', end='')
    tmp = n
    cnt = 0
    while tmp > 0:
        if tmp & 1 == 1:
            print('1', end='')
            cnt += 1
        else:
            print('0', end='')
        tmp = tmp >> 1
    print('\t', cnt, end='')
    print()


for i in range(20):
    printBits(i)
